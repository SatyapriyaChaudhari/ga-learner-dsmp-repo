# --------------
# import the libraries
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

# Code starts here
df = pd.read_csv(path)
print(df.head())
X = df.drop(['insuranceclaim'], 1)
y = df['insuranceclaim'].copy()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 6)

# Code ends here


# --------------
import matplotlib.pyplot as plt

# Code starts here
plt.boxplot(X_train['bmi'])
plt.title("BMI")
plt.show()

q_value = X_train['bmi'].quantile(0.95)
print("q_value: ", q_value)
print(y_train.value_counts())

# Code ends here


# --------------
# Code starts here
relation = X_train.corr()
print("Feature Correlation:\n", relation)
g = sns.pairplot(X_train)


# Code ends here


# --------------
import seaborn as sns
import matplotlib.pyplot as plt

# Code starts here
cols = ['children','sex','region','smoker']
dataframe = df[cols]
fig, axes = plt.subplots(2, 2)

for i in range(0,2):
    for j in range(0,2):
        col = cols[i*2 + j]
        axes[i,j] = sns.countplot(x=X_train[col], hue = y_train)
        #plt.set_title(col)

plt.tight_layout()

# Code ends here


# --------------
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# parameters for grid search
parameters = {'C':[0.1,0.5,1,5]}

# Code starts here
lr = LogisticRegression()
grid = GridSearchCV(lr, parameters)
grid.fit(X_train, y_train)
y_pred = grid.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy Score: ", accuracy_score)

# Code ends here


# --------------
from sklearn.metrics import roc_auc_score
from sklearn import metrics

# Code starts here
score = roc_auc_score(y_pred, y_test)
print("ROC-AUC Score: ", round(score, 4))
#ones = sum(y_test == 1)
#total = len(y_test)
#y_pred_proba = round((ones / total), 2)

y_pred_proba = grid.predict_proba(X_test)[:, 1]

print("Probability for y_test = 1 is ", y_pred_proba)
fpr, tpr, _ = metrics.roc_curve(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)
print(roc_auc)
plt.plot(fpr, tpr, label="Logistic model, auc="+str(roc_auc))
plt.show()

# Code ends here


