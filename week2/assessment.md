
1. For classifying product names to categories:

a. What precision (P@1) were you able to achieve?

`0.964`

b. What fastText parameters did you use?

`-lr 1.0 -epoch 25 -wordNgrams 2`

c. How did you transform the product names?

Used commandline sed script to lowercase and remove non-alphanumeric characters

d. How did you prune infrequent category labels, and how did that affect your precision?

Using pandas, group by category, aggregate on count, sort by count and pick categories where count greater than equal to 500. Use these categories to filter on products dataframe and output data as `pruned_labeled_products.txt`

e. How did you prune the category tree, and how did that affect your precision?

Did not attempt

---

2. For deriving synonyms from content:

a. What were the results for your best model in the tokens used for evaluation?

```
Query word? iphone
4s 0.83084
3gs 0.776334
apple 0.757744
ipadÂ 0.727652
ipod 0.711501
```

b. What fastText parameters did you use?

`skipgram`

c. How did you transform the product names?

Using commandline sed script to lowercase and remove non-alphanumeric characters

---

3. For integrating synonyms with search:

a. How did you transform the product names (if different than previously)?

Same

b. What threshold score did you use?

`0.75`

c. Were you able to find the additional results by matching synonyms?

Yes

---

4. For classifying reviews:

**Did not attempt**

a. What precision (P@1) were you able to achieve?


b. What fastText parameters did you use?

c. How did you transform the review content?

d. What else did you try and learn?
