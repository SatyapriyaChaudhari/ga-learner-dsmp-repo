### Project Overview

 Build a linear regression model to predict the price of a new released Lego set.


### Learnings from the project

 Concepts applied:

- [ ] Correlation between the features
- [ ] Linear Regression
- [ ] MSE andR^2 Evaluation Metrics


### Approach taken to solve the problem

 Steps Involved:
1. To check if the mean of installment falls in the range of the confidence interval.
2. Check if Central Limit Theorem holds for installment column.
3. To check the one-sided hypothesis that people with purpose as 'small_business' have been given int.rate more due to the risk assosciated.
4. To check the two-sided hypothesis that monthly installments customers have to pay might have some sort of effect on loan defaulters.
5. Perform a Chi-square test to check if there is a strong association between purpose of the loan of a person and whether that person has paid back loan.


### Challenges faced

 Steps Involed:
1. Check the scatter_plot for different features vs target variable list_price. This tells us which features are highly correlated with the target variable list_price and help us predict it better.
2. Features highly correlated with each other adversely affect our lego pricing model. Thus we keep a inter-feature correlation threshold of 0.75. If two features are correlated and with a value greater than 0.75, remove one of them.
3. Use linear regression to predict the price. We will check the model accuracy using r^2 score and mse.
4. Visualize the error.


