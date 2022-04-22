from dataclasses import replace
import re

phrase1 = input('Entrez une phrase ')
phrase2 = input('Entrez une phrase ')



#test2 = phrase2.replace('*', '')

phraseConverti = re.search("orme$", phrase2)

print(phraseConverti)

# test = re.search(phrase1 )

# if test:
#     print("yeeees")
# else:
#     print("no match")

#print(phrase1)
#print(phrase2)
#findall() pour rechercher les caractere speciaux