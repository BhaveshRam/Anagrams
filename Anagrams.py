from collections import Counter

## DECLARATION SECTION ##

list2=[]  #List to store seperated anagrams
list3=[] # temporary list for checking purpose

## INPUT SECTION ##

s=input("Enter anagrams:")
list11= s.split(",") 
list1=[x.strip() for x in list11] #List for storing input anagrams

## ANAGRAM VERIFICATOION SECTION ##

def check(s1, s2):
    if(Counter(s1)==Counter(s2)): #Checking frequency of each character
        return True     #returning true in case if the frequencies are matching
    else:
        return False    #Returning Flase in case frequency mismatch

## ANAGRAM SEPERATION SECTION ##

count=-1
for i in range(len(list1)): #To loop for all words in the list of anagrams
    if(list1[i] in list3):   #In case the word is already taken it moves to another word
        continue
    else:
        count+=1    #Count is used for index of seperated anagrams list
        list3.append(list1[i]) #To crosscheck we are appending into list3
        list2.append([])
        list2[count].append(list1[i]) 
    for j in list1:     
        if(j not in list3):     #Checking whether already an entry is made in th list or not
            if(check(list1[i],j)): #Cheking whether it is an anagram of the current word or not 
                list2[count].append(j) #Appending if it is anagram 
                list3.append(j)     #Appending into list3 that it is already completed to prevent duplicate entries.

## PRINTING SECTION ##

print(list2) #Printing List of anagrams.
