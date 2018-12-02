# --------------
#Code starts here
age = census[:, 0]
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)

print("Maximum Age: ", max_age)
print("Minimum Age: ", min_age)
print("Mean Age: ", age_mean)
print("Std. Dev. Age: ", age_std)


# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

#Code starts here
data = np.genfromtxt(path, delimiter = ",", skip_header = 1)
print(data.shape)
print(new_record.shape)
census = np.concatenate((data, new_record), axis = 0)


# --------------
#Code starts here
filt = [census[:,0]>60]
senior_citizens = census[filt]
working_hours_sum = np.sum(senior_citizens[:,6])
print("Working Hours Sum: ", working_hours_sum)
senior_citizens_len = len(senior_citizens)
print("Number of Senior Citizens: ", senior_citizens_len)
avg_working_hours = working_hours_sum/senior_citizens_len
print("Average Working Hours: ", avg_working_hours)


# --------------
#Code starts here
race_0 = np.array([])
race_1 = np.array([])
race_2 = np.array([])
race_3 = np.array([])
race_4 = np.array([])

#print(census.shape)
#print(len(census))
for i in range(0, len(census)):
    if census[i,2] == 0:
        race_0 = (np.append(race_0, census[i,:]))
    elif census[i,2] == 1:
        race_1 = (np.append(race_1, census[i,:]))
    elif census[i,2] == 2:
        race_2 = (np.append(race_2, census[i,:]))
    elif census[i,2] == 3:
        race_3 = (np.append(race_3, census[i,:]))
    elif census[i,2] == 4:
        race_4 = (np.append(race_4, census[i,:]))

race_0.resize(int(len(race_0)/8), 8)
race_1.resize(int(len(race_1)/8), 8)
race_2.resize(int(len(race_2)/8), 8)
race_3.resize(int(len(race_3)/8), 8)
race_4.resize(int(len(race_4)/8), 8)

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

len1 = np.array([len_0, len_1, len_2, len_3, len_4])
print(len1)
print(type(race_0))
print(race_0.shape)
minority_race = np.argmin(len1)

print("Minority Race:", minority_race)



# --------------
#Code starts here

filt_high = [census[:,1]>10]
high = census[filt_high]

filt_low = [census[:,1]<=10]
low = census[filt_low]

avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])

print("Average Pay High: ", avg_pay_high)
print("Average Pay Low: ", avg_pay_low)

if avg_pay_high > avg_pay_low:
    print("There is truth in better education leads to better pay.")
else:
    print("There is no truth in better education leads to better pay.")


