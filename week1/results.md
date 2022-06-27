1. Do you understand the steps involved in creating and deploying an LTR model?  Name them and describe what each step does in your own words.

Following are the steps involved in creating and deploying LTR model -

1. Do Exploratory Data Analysis (EDA) of available dataset. Identify fields, types, missing values, ranges, distribution, skewness of data etc.
2. Create a baseline performance using the traditional approaches. For the given problem, we had a hand-crafted query accounting for the domain and having specific boost for each of the query blocks. We also had a Simple MRR using the default Search Engine approach.
3. Create a very simple featureset as LTR baseline. For e.g. for the given problem we identified name_match as the feature in featureset to start.
4. Using the extension, calculate the weights for the featureset by querying the search engine and log it into the document itself. Also extract these logs to create a judgement data to train the model.
5. Train your model using judgement data collected in above step.
6. Measure performance of above LTR featureset against other identified baselines. Use the model to rescore queries and enhance its relevance ranking.
7. Include more feature iteratively by referencing the baseline hand tuned query keeping track of performance improvement.

---

2. What is a feature and featureset?

Feature: Single signal over a field

Featureset: Collection of features

---
3. What is the difference between precision and recall?

Precision = Count of Relevant Items retrieved / Total Items Retrieved

Recall = Count of Relevant Items retrieved / Total Relevant Items in Database

---
4. What are some of the traps associated with using click data in your model?

Data is very skewed as well as uncleaned. The click data is synthesized, so the real-world user behaviour might be very different from this data.

---
5. What are some of the ways we are faking our data and how would you prevent that in your application?

We synthesized impression data by querying the search engine and marking top results are impression. This is one way of faking data.

There are other machine learning methods to augment the data, so that we have more number of data points but do not skew the data distribution.

---
6. What is target leakage and why is it a bad thing?

When testing data is used to train the model, it introduces target leakage. This makes the model to overfit or memorize the data rather than actually learn the trends.

---
7. When can using prior history cause problems in search and LTR?

History can't be accurate prediction of future trends. Many of the events like discounts, festivals, and other macro factors might vary. Hence relying on or not accounting for prior history can give incorrect results for future trends

---
8. Submit your project along with your best MRR scores

```
Simple MRR is 0.386
LTR Simple MRR is 0.451
Hand tuned MRR is 0.448
LTR Hand Tuned MRR is 0.453

Simple p@10 is 0.135
LTR simple p@10 is 0.163
Hand tuned p@10 is 0.214
LTR hand tuned p@10 is 0.173
Simple better: 650      LTR_Simple Better: 665  Equal: 14
HT better: 808  LTR_HT Better: 696      Equal: 19
```
