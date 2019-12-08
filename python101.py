#!/bin/python3

#Print string

print("Strings")
print('Hello world')

print("""Hello, this
is multi line string""")

print("This is" + " string")

print('\n') #new line

#MATH

print("Math time:")
print(50+50) #add
print(50-50) #substract
print(50*50) #multiply
print(50/50) #div
print(50+50*50/50) #pemdas
print(50 ** 2) #exponents
print(50%2) #modulo
print(50//6) #number without leftover

#variables and methods

print("Fun with variables and methods")

quote = 'All is fair and love and war'

print(len(quote)) #lenght

print(quote.upper())
print(quote.title())


name = "KIRO"
age = 60 #int
mark = 5.5 #float

print(int(age))
print(int(29.9))#does not round
print("My name is " + str(name) + " AND I AM " + str(age) + " years old")
print('\n')

age+=1
print(age)

birthday=1
age+=birthday
print(age)
#functions
print("Now, some functions")

def who_am_i():
	name1="Kiro"
	age=29
	print("My name is " + str(name1) + " AND I AM " + str(age) + " years old")


who_am_i()


#adding in parameters
def add_one_hundred(num):
	print(num+100)
add_one_hundred(100)

#add in multiple parameters
def add(x,y):
	print(x+y)
add(7,7)
add(1,302)

#using return

def multiply(x,y):
	return x*y

print(multiply(7,7))

def square_root(x):
	return x ** 0.5
print(square_root(64))

print('\n')

#Boolean expressions (True or False)


print("BOOLEANS")
bool1=True
bool2=3*3==9
bool3=False
bool4=3*3!=9

print(bool1,bool2,bool3,bool4)
print(type(bool1))
bool5="True"
print(type(bool5))


#relational and boolean operators

greater_than=7>5
less_than=5<7
greater_than_equal_to=7>=7
less_than_equal_to=7<=7

print(greater_than,less_than,greater_than_equal_to,less_than_equal_to)


test_and = (7>5) and (8<7)
test_or = (7>5) or (5<7)
test_not=not True
print(test_and,test_or,test_not)

print('\n')

#Conditional statements
print("Conditional statements")
def soda(money):
	if(money>=2):
		return "Bought"
	else:
		return "unsifficient funds"
print(soda(3))
print(soda(1))


def alcohol(age,money):
	if((age>=18) and (money>=5)):
		return "rakia sold legally"
	elif((age>18) and (money<5)):
		return "no money, rakia gifted"
	elif (age<18) and (money>=5):
		return "rakia sold illegally"
	else:
		return "no money to buy illegal rakia"
print(alcohol(18,5))
print(alcohol(19,4))
print(alcohol(17,4))

print('\n')
#LIST


print("List\n")
print("Lists have brackets")

movies=["The Hangover", "Krum", "Selski boi", "azis"]

print(movies[1])

print(movies[0:4])

print(movies[1:])#slicing from 1 to the end

print(movies[:1])#slicing - the opposite

print(movies[:-1])

print(len(movies))

movies.append("Jaws")

print(len(movies))

print(movies)

movies.pop()#removes the last

print(movies)

movies.pop(1)

print(movies)

movies=["The Hangover", "Krum", "Selski boi", "azis"]
person=["Kiro", "vylio", "gorio"]

combined=zip(movies,person)

print(list(combined))

#2:49:00

#Tuples
print("Tuples have parentheses and cannot change")

grades=("A","B","C","D","E","F")
print(grades[1])

#Looping

print("For loops - start to fonish of iterate:")


vegetables = ["tomato","onion","rqpa","spinach"]

for x in vegetables:
	print(x)

print("While loops - execute as long as true")

i=1;
while(i<10):
	print(i)
	i+=1


#3:05:50





























































































































































































