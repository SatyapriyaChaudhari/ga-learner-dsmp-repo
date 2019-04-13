# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  


# path        [File location variable]

#Code starts here

data = pd.read_csv(path)
data_sample = data.sample( n = sample_size, random_state = 0)
sample_mean = data_sample['installment'].mean()
sample_std = data_sample['installment'].std()
margin_of_error = z_critical * sample_std / math.sqrt(sample_size)
confidence_interval = [sample_mean - margin_of_error, sample_mean + margin_of_error]
true_mean = data['installment'].mean()
print("95% Confidence Interval: ", confidence_interval)
print("True Mean: ", true_mean)

if ((confidence_interval[0] <= true_mean) & (confidence_interval[1] >= true_mean)):
    print("True Mean falls in the range of Confidence Interval")
else:
    print("True Mean does not fall in the range of the Confidence Interval")





# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here

fig, axes = plt.subplots(nrows = 3, ncols = 1)

for i in range(len(sample_size)):
    m = []
    for j in range(1000):
        data_sample = data.sample( n = sample_size[i])
        m.append(data_sample['installment'].mean())
    mean_series = pd.Series(m)    
    axes[i].hist(mean_series)

plt.tight_layout()
plt.show()



# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here

data['int.rate'] = data['int.rate'].map(lambda x: x.rstrip('%'))
data['int.rate'] = data['int.rate'].apply(pd.to_numeric)
data['int.rate'] = data['int.rate'] / 100

z_statistic, p_value = ztest(x1 = data[data['purpose']=='small_business']['int.rate'], value = data['int.rate'].mean(), alternative = 'larger')

if p_value < 0.05:
    print("Reject the Null Hypothesis.")
else:
    print("Do not reject the Null Hypothesis.")


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
z_statistic, p_value = ztest(x1 = data[data['paid.back.loan']=='No']['installment'], x2 = data[data['paid.back.loan']=='Yes']['installment'], alternative = 'two-sided')

print(z_statistic)
if p_value < 0.05:
    print("Reject the Null Hypothesis.")
else:
    print("Do not reject the Null Hypothesis.")


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes = data[data['paid.back.loan'] == 'Yes']['purpose'].value_counts()
no = data[data['paid.back.loan'] == 'No']['purpose'].value_counts()

observed = pd.concat([yes.transpose(), no.transpose()], axis = 1, keys = ['Yes', 'No'])
print(observed)
chi2, p, dof, ex = chi2_contingency(observed)

if chi2 > critical_value:
    print("Reject the Null Hypothesis.")
else:
    print("Do not reject the Null Hypothesis.")


