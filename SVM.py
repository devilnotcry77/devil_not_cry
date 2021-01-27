import numpy as np 
from sklearn.pipeline import make_pipeline
from sklean.preprocessing import StandartScaler
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
from sklearn.svm import SVC
clf = make_pipeline(StandartScaler(), SVC(gamma="auto"))
clf.fit(X, y)
clf.predict([[-0.8, -1]])
