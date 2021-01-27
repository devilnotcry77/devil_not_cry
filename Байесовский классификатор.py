
#P(x/y)=P(x1/y)*P(x2/y)*...*P(xd/y)
#Наивный байесовский классификатор

import numpy as np 
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
clf.predict([[-0.8, -1]])
