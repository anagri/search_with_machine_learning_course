import os
import argparse
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import csv

# Useful if you want to perform stemming.
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

categories_file_name = r'/workspace/datasets/product_data/categories/categories_0001_abcat0010000_to_pcmcat99300050000.xml'

queries_file_name = r'/workspace/datasets/train.csv'
output_file_name = r'/workspace/datasets/labeled_query_data.txt'

parser = argparse.ArgumentParser(description='Process arguments.')
general = parser.add_argument_group("general")
general.add_argument("--min_queries", default=1000,  help="The minimum number of queries per category label (default is 1)")
general.add_argument("--output", default=output_file_name, help="the file to output to")

args = parser.parse_args()
output_file_name = args.output

if args.min_queries:
    min_queries = int(args.min_queries)

# The root category, named Best Buy with id cat00000, doesn't have a parent.
root_category_id = 'cat00000'

tree = ET.parse(categories_file_name)
root = tree.getroot()

# Parse the category XML file to map each category id to its parent category id in a dataframe.
categories = []
parents = []
for child in root:
    id = child.find('id').text
    cat_path = child.find('path')
    cat_path_ids = [cat.find('id').text for cat in cat_path]
    leaf_id = cat_path_ids[-1]
    if leaf_id != root_category_id:
        categories.append(leaf_id)
        parents.append(cat_path_ids[-2])
categories.append(root_category_id)
parents.append(root_category_id)
parents_df = pd.DataFrame(list(zip(categories, parents)), columns =['category', 'parent'])

# Read the training data into pandas, only keeping queries with non-root categories in our category tree.
df = pd.read_csv(queries_file_name)[['category', 'query']]
df = df[df['category'].isin(categories)]

# IMPLEMENT ME: Convert queries to lowercase, and optionally implement other normalization, like stemming.
df['query'] = df['query'].str.strip().str.lower()
df['query'] = df['query'].str.replace(r"[^a-zA-Z0-9\s]", " ", regex=True)
df['query'] = df['query'].str.replace(r"\s{2,}", " ", regex=True)
df['query'] = df.apply(lambda x: stemmer.stem(x['query']), axis=1)
df['count'] = 1

# IMPLEMENT ME: Roll up categories to ancestors to satisfy the minimum number of queries per category.
category_lookup = parents_df.set_index('category').sort_index()

def new_cats_for(cats_with_lowq):
    def find_parent(x):
        if x['category'] in cats_with_lowq:
            return category_lookup.loc[x['category']]['parent']
        return x['category']
    return find_parent

print('initial total rows: ', len(df))
print('initial unique cats: ', len(df['category'].unique()))

complete = False
while not complete:
    df_gbc = df[['category', 'count']].groupby(['category']).sum()
    cats_with_lowq = df_gbc[df_gbc['count'] < min_queries].index
    new_categories = df.apply(new_cats_for(cats_with_lowq), axis=1)
    complete = df['category'].equals(new_categories)
    df['category'] = new_categories
    print('unique cats: ', len(df['category'].unique()))

# Create labels in fastText format.
df['label'] = '__label__' + df['category']

# Output labeled query data as a space-separated file, making sure that every category is in the taxonomy.
df = df[df['category'].isin(categories)]
df['output'] = df['label'] + ' ' + df['query']
df[['output']].to_csv(output_file_name, header=False, sep='|', escapechar='\\', quoting=csv.QUOTE_NONE, index=False)
