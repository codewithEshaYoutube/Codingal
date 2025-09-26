#1importing libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt


# 2 data set
X=np.array([[1,2],[2,3],[4,8],[3,6],[6,7]])
y=np.array([0,1,1,0,1])

#3 spliting the dataset
X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.25, random_state=0)
#4 choosing and training of model
model=LogisticRegression()
model.fit(X_train,y_train)

#5 making predictions 
y_pred=model.predict(X_test)

#6 evaluating the model
print(classification_report(y_test,y_pred))

#7 visualization of all the metrics
plt.scatter(X[y==0][:,0],X[y==0][:,1],c='blue',label='Class 0')
plt.scatter(X[y==0][:,0],X[y==0][:,1],c='red',label='Class 1')
plt.scatter(X_test[:,0],X_test[:,1],edgecolors="k",facecolors="none",label="test samples")
plt.legend()
plt.title("Binary Logistic Classification")
plt.show()
