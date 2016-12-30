#This program puts every word within an array based on the length of the word
#The arrays are put inside a dictionary(object)
#Outputs to a json file
#Created by: TheOnionSeed-Tri Do
import json

file = open("dictionary.txt", "r")
outputFile = open("dictionary.json","w")

#read the original file by getting each line
contents=file.readlines()#contents is a list with all the lines
file.close()

dict = {}

#add each word to its corresponding list based on its length
for word in contents:
	word = word.strip('\n')
	length = len(word)
	if not(length in dict):
		dict[length] = []
	dict[length].append(word)
	
json.dump(dict, outputFile, ensure_ascii=False)#write the dictionary to json file