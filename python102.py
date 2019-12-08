#!/bin/python3

#Import

print("Importing is important:")

import sys#system functions and parameters

from datetime import datetime 
print(datetime.now())

from datetime import datetime as dt

print(dt.now())



def new_line():
	print('\n')


new_line()

#Advanced Strings
print("Advanced strings")
my_name="Joro"
print(my_name[0])#first initial
print(my_name[-1])	

sentence="This is a sentence."
print(sentence[0:4])     #first word
print(sentence[-9:-1])#last word

print(sentence.split()) #split the sentence by delimiter (space)

sentence_split=sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
print('\n'.join(sentence_split))





quoteception = "I said, 'give me all the money'"
print(quoteception)

quoteception = "I said, \"give me all the money\""
print(quoteception)

print("pp" in "Apple")#true

letter = "a"#lowercase doesn't work(False)
word = "Apple"
print(letter in word)



letter = "a"
word = "Apple"
print(letter.lower() in word.lower())


word_two = "Bingo"
print((letter.lower() in word.lower()) and not (letter.lower() in word_two.lower()))

too_much_space = "                      hi                 "
print(too_much_space.strip())#space is default

full_name="enelin Atanasov"
print(full_name.replace("enelin","Venelin"))
print(full_name.find("Atanasov"))



movie = "The Hangover"
print("My favourite movie is {}.".format(movie))

def favourite_book(title,author):
	fav = "My favourite book is \"{}\", which is written by {}".format(title,author)
	return fav
print(favourite_book("The foundation","A.Asiimov"))

new_line()

#Dictionaries
print("Dictionaries are keys and values:")

#{} 
drinks = {"White Russians":7, "Old Fashion":10, "Lemon drop":8,"Buttery Nipple":6,"RAKIA":0.12}#key:value
print(drinks)

employees = {"Finance":["BOB","Linda","Tina"], "IT":["Gene","Gosho","Kiro"],"HR":["Jimmy","Suzuki"]}
print(employees)

employees['Legal']=["Mr.Frond"]#add new key value pair
print(employees)

employees.update({"Sales":["Andie","Ollie"]})
print(employees)


drinks["White Russians"]=8
print(drinks)


print(drinks.get("White Russians"))
print(drinks.get("Kiselo Vino"))#None



#List and dictionaries

movies = ["When Harry met Sally","The Hangover","The perks of being a wallflower","The exorcist"]
person = ["Heath","Bob","Leah","Jeff"]
combined = zip(movies,person)
movie_dictionary = {key:value for key, value in combined}
print(movie_dictionary)
























































































































