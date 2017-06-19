import sys
import re
import string


f = open("commits_number_by_order.txt", 'w')
sys.stdout = f

list_of_words = []
list_of_commits = []
frequency = {}
document_text = open('commit_details.txt', 'r')
text_string = document_text.read().lower()
text_string = str(text_string)
match_pattern = re.findall(r'\b[0-9A-Fa-f]{10,12}\b', text_string)
counter = 0
for word in match_pattern:
    list_of_commits.append(word)
    counter = counter +1
    
print("There are " + str(counter) + " commits in total.")
print(list_of_commits)
        
f.close()






