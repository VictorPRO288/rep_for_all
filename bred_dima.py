def get_prediction(sl, model):
    sl = sl.split(",")
    sl = pd.DataFrame([sl],columns= data.columns)
    
    sl = data_preprocessing(sl)
    sl = sl.drop(["heartdisease"], axis=1)

    otv = model.predict(sl)
    return str(otv)

import numpy as np
import pandas as pd
from catboost import CatBoostClassifier
from sklearn.preprocessing import  LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score , recall_score

data = pd.read_csv(r"data\heart_failure_prediction.csv")


def data_preprocessing(data):
    columns = data.columns
    for i in columns:
        if data[i].dtype!=object:
            data[i] = data[i].astype(float)
        else:
            le = LabelEncoder()
            data[i] = le.fit_transform(data[i])
    return data

data = data_preprocessing(data)


X = data.drop(["heartdisease"], axis=1)
y = data["heartdisease"]



X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, test_size=0.3)

scaler= StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

model = CatBoostClassifier(iterations=1000, learning_rate=0.01, depth=8)
model.fit(X_train, y_train)


pred = model.predict(X_test)
accuracy = model.score(X_test, y_test)
print(f"Accuracy stroke: {accuracy}")
print(precision_score(pred, y_test))
print(recall_score(pred, y_test))


import joblib
# load the model 
# save
joblib.dump(model, "model_old.pkl") 