1. Do you understand the steps involved in creating and deploying an LTR model?  Name them and describe what each step does in your own words.

---

2. What is a feature and featureset?

Feature: Single signal over a field

Featureset: Collection of features

---
3. What is the difference between precision and recall?

Precision = Count of Relevant Items / Total Items Retrieved

Recall = Count of Relevant Items / Total Relevant Items

---
4. What are some of the traps associated with using click data in your model?


---
5. What are some of the ways we are faking our data and how would you prevent that in your application?

---
6. What is target leakage and why is it a bad thing?

---
7. When can using prior history cause problems in search and LTR?

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