# --------------
# code ends here

loan_groupby = bank.groupby(['Loan_Status'])[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()
print(mean_values)



# code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(bank, values = ['LoanAmount'], index = ['Gender', 'Married', 'Self_Employed'], aggfunc = np.mean)
print(round(avg_loan_amount,2))

# code ends here



# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print("Categorical Variables:\n", categorical_var.head())
numerical_var = bank.select_dtypes(include = 'number')
print("========================================================================")
print("Numerical Variables:\n", numerical_var.head())

# code ends here


# --------------
# code starts here

# code for loan aprroved for self employed
loan_approved_se = bank.loc[(bank["Self_Employed"]=="Yes")  & (bank["Loan_Status"]=="Y"), ["Loan_Status"]].count()
loan_approved_se= loan_approved_se.values[0]
print(loan_approved_se)

# code for loan approved for non self employed
loan_approved_nse = bank.loc[(bank["Self_Employed"]=="No")  & (bank["Loan_Status"]=="Y"), ["Loan_Status"]].count()
loan_approved_nse= loan_approved_nse.values[0]
print(loan_approved_nse)
# percentage of loan approved for self employed
percentage_se = (loan_approved_se * 100 / 614)

# print percentage of loan approved for self employed
print(percentage_se)

#percentage of loan for non self employed
percentage_nse = (loan_approved_nse * 100 / 614)

#print percentage of loan for non self employed
print (percentage_nse)

# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)

big_loan_term = (loan_term >= 25).value_counts()[True]
print("Total number of applicants having loan amount term greater than or equal to 25 years: \n", big_loan_term)


# code ends here


# --------------
# code starts here
banks = bank.drop(labels = ['Loan_ID'], axis = 1)
print("Null Values:\n", banks.isnull().sum())
bank_mode = banks.mode().ix[0]
print(bank_mode)
#for column in banks.columns:
#    banks[column].fillna(bank_mode[column][0], inplace = True)

banks.fillna(bank_mode, inplace = True)

print("======================================================")
print("Null Values:\n", banks.isnull().sum())
#code ends here


