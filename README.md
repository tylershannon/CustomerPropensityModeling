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
2. Complete a random oversampling of the data so that there are equal counts of each target class
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


