from PyDictionary import PyDictionary
import pandas as pd 
from itertools import permutations, combinations


letter_combinations_list=[]
letter_permutations_list=[]
potential_words_list=[]
words_list=[]
df_words=pd.read_csv("dictionary.txt",header=None)

user_letters= input("Please enter the letters you have: ").upper()
user_letters=''.join(user_letters.split())
while True:
    if len(user_letters)>9:
        user_letters=input("Please Enter 9 letters or less: ")
        user_letters=''.join(user_letters.split())
    elif any(char.isdigit() for char in user_letters):
        user_letters=input("Please only enter letters:  ")
        user_letters=''.join(user_letters.split())
    else: 
        break


    print(user_letters)

#chnage this to 1 when you get the image processing to be able to get
#the combination of existing letters 
n=2
while n<=len(user_letters):
    combination=combinations(user_letters,n)
    letter_combinations_list.append(list(combination))
    n+=1
    
    

for lists in letter_combinations_list:
     for comb in lists:
         letters=''.join(comb)
         permutation=permutations(letters)
         letter_permutations_list.append(permutation)





for lists in letter_permutations_list:
    for perm in lists:
        words=''.join(perm)
        potential_words_list.append(words)


words_df=df_words[df_words[0].isin(potential_words_list)]
print(words_df)



#         words_list.append(word)
#         print(f"{word} added to the list")

# print(words_list)








tiles_frequency={
    "A":9,
    "B":2,
    "C":2,
    "D":4,
    "E":12,
    "F":2,
    "G":3,
    "H":2,
    "I":9,
    "J":1,
    "K":1,
    "L":4,
    "M":2,
    "N":6,
    "O":8,
    "P":2,
    "Q":1,
    "R":6,
    "S":4,
    "T":6,
    "U":4,
    "V":2,
    "W":2,
    "X":1,
    "Y":2,
    "Z":1,
    "Blank":2}

tiles_score={
    "A":1,
    "B":3,
    "C":3,
    "D":2,
    "E":1,
    "F":4,
    "G":2,
    "H":4,
    "I":1,
    "J":8,
    "K":5,
    "L":1,
    "M":3,
    "N":1,
    "O":1,
    "P":3,
    "Q":10,
    "R":1,
    "S":1,
    "T":1,
    "U":1,
    "V":4,
    "W":4,
    "X":8,
    "Y":4,
    "Z":10,
    "Blank":0}















