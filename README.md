# Prediction of if a patient with thyroid cancer can expect a reccurence of the cancer

In this project I have used a Kaggle data set (https://www.kaggle.com/datasets/jainaru/thyroid-disease-data) which is obtained from the UCI machine learning repository. The data set contains 13 features, mostly categorical, which are used to predict whether thyroid cancer will recur in the patient. Data analysis as well as data preparation, model creation and model tuning were done for the data set. All these steps are shown in this repository Jupyter notebook. Since the data was mostly categorical feature encoding was important and a mix of one hot encoding and ordinal encoding (depending on the features) was used and is explained. The final model which was decided on was the XGBoost machine learning model, which is essentially ensemble, specifically boosted, decision trees. The model was put through grid search with many hyperparameters and using stratified k fold cross validation to find the best model hyperparameters. The metric used to grade the models was the Recall. This is because maximizing recall with minimise the number of false negatives. False negatives can be detrimental to human lives as this means a prediction of 'not recurring' is made so the patient will not receive help, but the cancer does recur and may cause death. For these reasons recall was chosen as the main metric, however the other metrics were also high on both the test and the train data (Not there was a 30% split for test data). After the hyperparameters were found, the model was then fitted to the whole dataset then exported.