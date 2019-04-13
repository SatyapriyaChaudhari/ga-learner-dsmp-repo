# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 
data = pd.read_csv(path)
data['Gender'].replace('-', 'Agender', inplace = True)
gender_count = data['Gender'].value_counts()
plt.bar(gender_count.index, gender_count.values)
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Distribution of Gender")
plt.show()



# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
plt.pie(alignment, labels = alignment.index)
plt.title("Character Alignment")
plt.show()


# --------------
#Code starts here
sc_df = data[['Strength','Combat']]
sc_covariance = np.cov(sc_df.Strength, sc_df.Combat)[0,1]
sc_strength = sc_df.Strength.std()
sc_combat = sc_df.Combat.std()
sc_pearson = sc_covariance / (sc_strength * sc_combat)
print("Correlation between Strength and Combat: %.2f" %sc_pearson)

ic_df = data[['Intelligence','Combat']]
ic_covariance = np.cov(ic_df.Intelligence, ic_df.Combat)[0,1]
ic_intelligence = ic_df.Intelligence.std()
ic_combat = ic_df.Combat.std()
ic_pearson = ic_covariance / (ic_intelligence * ic_combat)
print("Correlation between Intelligence and Combat: %.2f" %ic_pearson)


# --------------
#Code starts here
total_high = data['Total'].quantile(0.99)
super_best = data[data['Total'] > total_high]
super_best_names = super_best['Name'].tolist()
print("The Overpowered Super Beings are: \n", super_best_names)


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows=1, ncols=3)
ax_1.boxplot(super_best.Intelligence)
#ax_1 = plt.title("Intelligence")
ax_2.boxplot(super_best.Speed)
#ax_2 = plt.title("Speed")
ax_3.boxplot(super_best.Power)
#ax_3 = plt.title("Power")
plt.tight_layout()
plt.show()



