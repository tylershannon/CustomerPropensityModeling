# Customer Propensity Modeling

## Project Scope

### Business Context
Imagine that you have been tasked with helping a marketing executive at a large bank understand
which characteristics of potential customers are the best predictors of purchasing of one of the bank’s
products.
<br>
<br>
Ultimately, the client is interested in using a predictive model to score each potential customer’s
propensity to purchase, as well as understanding which customer characteristics are most important in
driving purchasing behavior, in order to inform future marketing segmentation personalization, etc.

### The Dataset
For this project, use the specific dataset bank-additional-full.csv available at https://archive.ics.uci.edu/ml/datasets/Bank+Marketing
<br>
Note: This dataset contains the outcome variable (y) but you are not limited to using only this dataset
for this project

### Versioning and Packages
This data preprocessing done makes use of some helper funcions found in the ixis.py file.
Below are the packages used and their versions:
seaborn==0.10.0
scikit-learn==0.22.1
pydotplus==2.0.2
pandas==1.2.3
numpy==1.20.1
matplotlib==3.3.4
graphviz==0.16

### EDA Summary
* Data contains a mix of continuous and categorical variables. One-hot-encoding will be needed.
* Dataset is imbalance, where a majority of our records are classified as non-subscribers. This puts the subscriber class in the minority. This is important because certain algorithms will place too much emphasis on the majority class. We'll need to address this. We could undersample the majorty class to make the dataset more even but that may result in some information loss. Instead, I think I will attempt to oversample the minority class, keeping in mind that this could result in overfitting. Something for us to keep in mind.

### Data Pre-Processing Methodology

1. Convert target class from strings to binary (0/1)
2. Complete a random oversampling of the data so that there are equal counts of each target class. Note: this will result in overfitting.
3. Feature engineering of 'Jobs' variable. There are 12 different jobs in the dataset, these can be compressed into 10 job types.
4. Drop 'Duration' variable from the dataset. This is recommended in the data documenation.
5. One-hot-encode the categorical variables and drop one of each of the binary variables.
6. Split into training and testing, holding 20% of the dataset for testing.

### Feature Selection
I used a decision tree to assist with feature selection. I trained both a single decision tree and a random forest model. Specs are below for each:

#### Single Decision Tree Parameters
1. Critereon: entropy
2. Max Depth: 4
3. Random State: 40

#### Random Forest Parameters
1. Critereon: entropy
2. Max Depth: 4
3. Random State: 40
4. Number of Estimators: 100

#### Model Performance
![test](https://github.com/tylershannon/CustomerPropensityModeling/blob/main/images/AUC_ROC_dt_rf.png?raw=true)

Here we can see that the random forest model performs slightly better, but not by much. We'll use the single decision tree to explore the feature importances.

#### Feature Importance
1. poutcome_success	0.493724
2. contact_unknown	0.265159
3. housing_yes	0.111819
4. month_aug	0.066816
5. month_mar	0.023784
6. month_oct	0.015026
7. marital_married	0.011819
8. day_18	0.002834
9. balance	0.002188
10. pdays	0.001697

* The success of previous marketing initiative is a good inidicator as to whether someone will subscribe. Our tree is telling us that if there is a past success, the customer is more likely to subscribe. In a business context this suggests that marketers should place high value on existing contacts to help drive future subscriptions.
* It also appears that age, house loan status, marital status and bank account balance are other good indicators of subscriptions.
* It appears that spring and fall are better times for subscription conversions.

With these results from the decision tree suggesting some important features, I'll use those features to build a logistic regression classification algorithm
