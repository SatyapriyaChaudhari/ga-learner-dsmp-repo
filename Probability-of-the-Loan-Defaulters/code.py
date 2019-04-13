# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
p_a = len(df[df.fico > 700]) / len(df)
p_b = len(df[df.purpose == 'debt_consolidation']) / len(df)
df1 = df.loc[df.purpose == 'debt_consolidation']
p_a_b = len(df1[df1.fico > 700]) / len(df1)
result = (p_a_b == p_a)
print("Debt Consolidation is independent if Fico Credit Score: ", result)



# code ends here


# --------------
# code starts here
prob_lp = len(df[df['paid.back.loan'] == "Yes"]) / len(df)
prob_cs = len(df[df['credit.policy'] == "Yes"]) / len(df)

new_df = df.loc[df['paid.back.loan'] == "Yes"]
prob_pd_cs = len(new_df[new_df['credit.policy'] == "Yes"]) / len(new_df)

bayes = prob_pd_cs * prob_lp / prob_cs
print(bayes)


# code ends here


# --------------
# code starts here

(df['purpose'].value_counts()).plot.bar()
plt.xlabel("Purpose")
plt.ylabel("Number of Customer")
plt.title("Distribution of Feature")
plt.show()

df1 = df.loc[df['paid.back.loan'] == "No"]

(df1['purpose'].value_counts()).plot.bar()
plt.xlabel("Purpose")
plt.ylabel("Number of Customer")
plt.title("Distribution of Feature where paid.back.loan is No")
plt.show()
# code ends here


# --------------
# code starts here

inst_median = df['installment'].median()
inst_mean = df['installment'].mean()
print("Meadian: ", inst_median)
print("Mean: ", inst_mean)

df['installment'].hist()
plt.xlabel("Installlment")
plt.ylabel("Frequency")
plt.title("Distribution of Instalment")
plt.show()

df['log.annual.inc'].hist()
plt.xlabel("Log Annual Income")
plt.ylabel("Frequency")
plt.title("Distribution of Log Annual Income")
plt.show()

# code ends here


