
import sys
import pygit2
import re
import string
import tokenize
import io
import subprocess
import os
import math


""" changing the .py into .txt we transform the source code into text"""

# firstly we remove the comments from the source code


def remove_all_comments(text_string):
    prev_toktype = tokenize.INDENT
    last_lineno = -1
    last_col = 0
    io_obj = io.StringIO(text_string)
    out = ""
    for tok in tokenize.generate_tokens(io_obj.readline):
        token_type = tok[0]
        token_string = tok[1]
        start_line, start_col = tok[2]
        end_line, end_col = tok[3]
        ltext = tok[4]
        if start_line > last_lineno:
            last_col = 0
        if start_col > last_col:
            out += (" " * (start_col - last_col))
        if token_type == tokenize.COMMENT:
            pass
        elif token_type == tokenize.STRING:
            if prev_toktype != tokenize.INDENT:
                if prev_toktype != tokenize.NEWLINE:
                    if start_col > 0:
                        out += token_string
        else:
            out += token_string
        prev_toktype = token_type
        last_col = end_col
        last_lineno = end_line
    return out

""" calling the above function we transform the source code, 
which now is a .txt file into a .txt file without comments"""

f = open("source_code_without_comments.txt", 'w')

sys.stdout = f
document_text = open('source_code.txt', 'r')
text_string = str(document_text.read().lower())
print(remove_all_comments(text_string))

f.close()






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







with open('source_code_without_comments.txt', 'r') as f1:
	for line in f1:
		line = str(line)
		if "def " in line:
			list_of_functions.append(line.split("def"))
			count_functions[author] = count_functions[author] + 1
		
f1.close()


with open('source_code_without_comments.txt', 'r') as f1:
	for line in f1:
		line = str(line)
		if "class " in line:
			list_of_classes.append(line.split("class"))
			count_classes[author] = count_classes[author] + 1
		
f1.close()




document_text = open('source_code_without_comments.txt', 'r')
text_string = str(document_text.read().lower())
words = text_string.split()
for i,w in enumerate(words):
    if w == "import":
        imported_items.append(words[i+1])
        count_imports[author] = count_imports[author] + 1




f = open("source_code_analysis.txt", 'w')
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






