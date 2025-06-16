from variables import firstname

number = 45 #Integer
second = 34.98 #float
greeting = "Good Morning"#String
isPythonInteresting = True #Boolean

#Data Structures
fruits = ["apple","banana","orange"] # list
cars = ("jeep","BMW","Tesla","Toyota") # Tuple
countries = {"Kenya", "Maldives", "Canada"} #Set
student = {
    "firstname" : "Victory",
    "lastname" : "Smith",
    "age": 21,
    "nationality": "Kenyan"
} # Dictionary - key-value pair

print(number)
print(isPythonInteresting)
print(fruits)
print(cars)
print(countries)
print(student["nationality"])


# Typecasting - Converting one datatype  to another
print(float (number))
print(int(second))
