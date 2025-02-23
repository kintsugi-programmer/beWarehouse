from sklearn.neighbors import (NeighborhoodComponentsAnalysis, KNeighborsClassifier)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import pandas as pd
import joblib

file_path = 'data.xlsx'
data = pd.read_excel(file_path)

# x = features, y=labels
X = data.iloc[:, :-1].values  # Assuming all columns except the last are features
y = data.iloc[:, -1].values   # Assuming the last column is the label
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.7, random_state=42)
nca = NeighborhoodComponentsAnalysis(random_state=42)
knn = KNeighborsClassifier(n_neighbors=3)
nca_pipe = Pipeline([('nca', nca), ('knn', knn)])
nca_pipe.fit(X_train, y_train)
print(nca_pipe.score(X_test, y_test))

pkl_path='knnModel.pkl'
joblib.dump(nca_pipe, pkl_path)
