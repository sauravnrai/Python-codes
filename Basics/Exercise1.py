# The task wants to check in a patient named john smith whose age is 20 years old and is a new patient.
# if he is new, displaY all details else print no record

name = 'John Smith'
age = 20
new_patient = True

if new_patient:
    print( name + " is a " + str(age) +" years old new patient")
else:
    print("No record found")