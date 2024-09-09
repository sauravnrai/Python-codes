# python by default accepts a string. So, use appropriate conversions

integer = int(input("Enter an integer: " )) # takes integer as input
stringy = str(integer) # Converts integer to string and stores in variable stringy
print("Integer is " + stringy)

floater = float(input("Enter an floating value: "))
stringy = str(floater)
print("Floating value is " + stringy)

# bool() converts string to boolean value

boolean = input("Enter a boolean value: ") # give True or False as it accepts string
stringy = str(boolean)
if boolean:
    print("Boolean value is " + stringy)
else:
    print("Boolean value is " + stringy)
