import sys
import pygit2
import re
import string
import subprocess
import os
import math


""" assuming that we have a txt file which is named 
author_contribution.txt that includes all the written 
code by the contributor who is named "author", we want to 
count how many items he imported, functions and classes he
built or called and which of them"""


""" firstly we have to remove the comments"""




author = "author"


list_of_functions = []
list_of_classes = []
imported_items=[]

count_imports = {}
count_functions = {}
count_classes = {}

count_imports[author] = 0
count_functions[author] = 0
count_classes[author] = 0







with open('author_contribution.txt', 'r') as f1:
	for line in f1:
		line = str(line)
		if "def " in line:
			list_of_functions.append(line.split("def"))
			count_functions[author] = count_functions[author] + 1
		
f1.close()


with open('author_contribution.txt', 'r') as f1:
	for line in f1:
		line = str(line)
		if "class " in line:
			list_of_classes.append(line.split("class"))
			count_classes[author] = count_classes[author] + 1
		
f1.close()




document_text = open('author_contribution.txt', 'r')
text_string = str(document_text.read().lower())
words = text_string.split()
for i,w in enumerate(words):
    if w == "import":
        imported_items.append(words[i+1])
        count_imports[author] = count_imports[author] + 1




f = open("author_code_analysis.txt", 'w')
sys.stdout = f



print("the number of functions for the given author is given in the below line")
print(count_functions)
print("the functions that he wrote are given in the list below")
print(list_of_functions)
print("the number of imports by the given author is given in the below line")
print(count_imports)
print("the imported items are given below")
print(imported_items)
print("the number of classes by the given author is given in the below line")
print(count_classes)
print("the names of the classes are given below")
print(list_of_classes)




f.close()





