# --------------
# Code starts here
mathematics = {'Geoffrey Hinton' : 78 , 'Andrew Ng' : 95 , 'Sebastian Raschka' : 65 , 'Yoshua Benjio' : 50 , 'Hilary Mason' : 70 , 'Corinna Cortes' : 66 , 'Peter Warden' : 75 }
topper = max(mathematics,key = mathematics.get)
print (topper)

# Code ends here  


# --------------
# Given string
topper = 'andrew ng'


# Code starts here
first_name = topper.split()[0]
last_name = topper.split()[1]
full_name = last_name + " " + first_name

print("Full Name: ", full_name)

certificate_name = full_name.upper()

print("Certificate Name: ", certificate_name)

# Code ends here


# --------------
# Code starts here
class_1 = ['Geoffrey Hinton', 'Andrew Ng', 'Sebastian Raschka', 'Yoshua Bengio']
class_2 = ['Hilary Mason', 'Carla Gentry', 'Corinna Cortes']
new_class = class_1 + class_2
print("New Register: \n", new_class)

new_class.append('Peter Warden')
print("Updated New Register: \n", new_class)

new_class.remove('Carla Gentry')
print("Updated New Register, after removing Carla: \n", new_class)
# Code ends here


# --------------
# Code starts here
courses = {'Math' : 65 , 'English' : 70 , 'History' : 80 , 'French' : 70 , 'Science' : 60}
print("Marks obtained in each subject: \n", courses)
total = sum(courses.values())
print("Total Marks Scored: ", total)
percentage = total/500 * 100
print("Percentage: ", percentage)

# Code ends here


