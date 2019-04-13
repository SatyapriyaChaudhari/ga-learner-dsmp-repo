# --------------
import pandas as pd
from sklearn.cross_validation import train_test_split

# code starts here
df = pd.read_csv(path)
print(df.head())
X = df.drop(columns = 'list_price')
y = df.list_price
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 6)

# code ends here



# --------------
import matplotlib.pyplot as plt

# code starts here 
#cols = X_train.iloc[:,:].copy()
#cols = list(X_train.head(0))
cols = X_train.columns
fig, axes = plt.subplots(nrows = 3, ncols = 3)

for i in range(3):
    for j in range(3):
        col = cols[i*3 + j]
        axes[i,j].scatter(X_train[col], y_train)
        axes[i,j].set_title(col)

plt.tight_layout()
plt.show()


# code ends here



# --------------
# Code starts here
import numpy as np

corr = round(X_train.corr(), 2)
print("Correlation Table:\n", corr)
print("===============================================")
X_train.drop(['play_star_rating', 'val_star_rating'], axis = 1, inplace = True)
X_test.drop(['play_star_rating', 'val_star_rating'], axis = 1, inplace = True)

print("X_train: \n", X_train.head())
print("===============================================")
print("\nX_test: \n", X_test.head())
# Code ends here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error: ", round(mse, 4))
r2 = r2_score(y_test, y_pred)
print("R Squared: ", round(r2, 4))

# Code ends here


# --------------
# Code starts here
residual = y_test - y_pred
plt.hist(residual, bins = 50)
plt.title("Residual")
plt.show()

# Code ends here


