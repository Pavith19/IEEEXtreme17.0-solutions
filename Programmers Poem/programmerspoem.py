"""
Author: Pavith Bambaravanage
URL: https://github.com/Pavith19
"""

num_families, num_lyrics = map(int, input().split())	

current_letter = 'A'

families = {}

for i in range(num_families):
	line = input()
	words = line.split()
	for word in words:
		families[word.lower()] = i
  
input()
  
last_words = []

for i in range(num_lyrics):
	last_words.append(input().split()[-1].lower())
 
for i in range(num_lyrics):
    if last_words[i] not in families:
        continue
    
    family = families[last_words[i]]
    found = False
    
    for j in range(num_lyrics):
        if i != j and last_words[j] in families and  family == families[last_words[j]]:
            found = True
            break
        
    if not found:
        families.pop(last_words[i])

family_letter_mapping = {}

for i in range(num_lyrics):
    word = last_words[i]
    
    if word in families:
        if families[word] not in family_letter_mapping:
            family_letter_mapping[families[word]] = current_letter
            current_letter = chr(ord(current_letter) + 1) if current_letter != 'X' else 'Y'
        print(family_letter_mapping[families[word]], end='')
        
    else:
        print("X", end='') 
