#!/usr/bin/env python
# coding: utf-8

# In[39]:


import random
import nltk

from nltk.corpus import wordnet as wn

class wordnet: #making a class to simplify the code
    def __new__(self,wordnetting): #new allows return to be used by a different value unlike _init'
        wordnetting = wn.synset(wordnetting +'.n.02')
        wordnetting = list(set([w for s in wordnetting.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))    
        
        return wordnetting #returns the list
    
    
foodlist = wordnet("food") #the list of the food is being called into the class
placelist = wordnet("place") #list of place is being called into the class


class termsUsed: #making a class to simplify the code
    def __new__(self,name): #new allows return to be used by a different value unlike _init
        with open(name + ".txt", "r") as obj:  #open and read the text file
            name = obj.read()  #give the file a variable name
            name = name
            name = list(map(str,name.split())) #individuals words
        return name #returns the list of words to be used 

"""
text files below are used to form the procedural novel
"""
    
Adjectives = termsUsed("Adjectives") 
dates = termsUsed("dates")
names1  = termsUsed("Names_nanogen")
allText = termsUsed("ManoPunk")
cs_1_1 = termsUsed("AppleCrisp_Clean")
MF_1_1 = termsUsed("MealFact_Class_Nature_WordAssc_Clean")
inhabitants = termsUsed("Classes")


#phrases that help the novel read better

location = ["While Chewing on a heavy breakfast in the dinner, ""Being in the underwater City of  Aquapolis, ","In California, ", "Outside of Earth, ","On the Safari Grounds, ", "At the Extension of the Tundra, ", "Within the Breeze on a lonely day at the beach, ", "While hiking the grandest of underwater Volcanoes, ", "Looking for the windiest village to maintain wind energy, ", "Hiding in the depths of Quicksand, ", "Flying at the higher limits of the atmosphere the Speed of the Light, "]
action = [" voted against "," eats "," flies with ", " destroys ", "fights", "voted with", "danced with", "mimics", "transform into"]
transition = [" while holding a ", " during times of conflict with a ", " instead of eating a ", "playing with ", "joking as ", "dressing up as ", "cosplaying as ", "checking up on ", "fighting with ", "fighting against "]


#intro
    
print("Welcome to the lost diaries of different worlds, our goal is to try to put the pieces together")
print("located within this document of lost text: are the diary entries, dates and at times: an inventory list")
print("Enjoy your read, enjoy your time. May the thing you are looking , be found in these lines" + "\n")
  

#counters    
    
counter = 0 #set the counter outside the loop
chapter = 0 #chapter counter

print(random.choice(transition) + random.choice(placelist) + " " + random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " "+ random.choice(Adjectives)+ " "+ random.choice(MF_1_1) + " " +  random.choice(words))
print(random.choice(words) + " " +  random.choice(words) + " " +  random.choice(Adjectives) + " " +  random.choice(words) + " "+ random.choice(MF_1_1) + " " +  random.choice(words))
    
for x in location * 130 : #for loop that runs 100 times the amount of items in the list of location
    
    chapter = chapter + 1 #increment for chapter
    
    #using modulo to set condiitons with the if/elif/else  statements
        
    if counter %15 == 0: #setting the amountof chapters
        print("CHAPTER " + str(chapter)[:-1] + "\n") #slicing the last digit, so chapter 10 isnt chapter 101
        
    if counter %45 == 0: #setting the random list of dates
        print(random.choice(dates) + ": " + random.choice(Adjectives).upper() + " & " + random.choice(cs_1_1) + "\n") 
        
    if counter %90 == 0:
        print("These are the inventory items located in this realm: ")
        
        for items in range(5): #print 5 times
            print(random.choice(cs_1_1))
        
        print("\n")
        
        Compass = ["N","E","W","S"] #part of the Latitude + Longitude thing
    
        
        print("Planetary information pertaining to the where the diary entry was found" + "\n")
        print("World Version: " + str(random.randrange(150, 570)))
        print("Latitude in this realm: " + str(random.randrange(0,90)) + " " + str(random.randrange(0,360)) + " " + str(random.randrange(0,90)) + random.choice(Compass))
        print("Longitude in this realm: " + str(random.randrange(0,180)) + " " + str(random.randrange(0,360)) + " " + str(random.randrange(0,90)) + random.choice(Compass) + "\n")
        print("Number of Inhabitants: " + str(random.randrange(100000,400000)))
        
        for items in range(5): #print 5 times
            print("Number of " + random.choice(inhabitants) + ": " + str(random.randrange(1000,10000)))
        print("\n")
    
    
    
    if counter  % 10 < 5 :
        print(random.choice(location) + random.choice(subject) + " " + random.choice(action) + " " + random.choice(Adjectives) + " " + random.choice(foodlist) + " " +  random.choice(transition) + " " +  random.choice(foodlist))
        
        for phrases in range(3):
            print(random.choice(transition) + random.choice(placelist) + " " + random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " "+ random.choice(Adjectives)+ " "+ random.choice(MF_1_1) + " " +  random.choice(words))
            print(random.choice(words) + " " +  random.choice(words) + " " +  random.choice(Adjectives) + " " +  random.choice(words) + " "+ random.choice(MF_1_1) + " " +  random.choice(words))
        
        print(random.choice(transition) + random.choice(placelist) + " " + random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " "+ random.choice(Adjectives)+ " "+ random.choice(MF_1_1) + " " +  random.choice(words) + "\n")
    
    elif counter % 10 > 5 and counter % 10 < 8:
        
        print(random.choice(Adjectives) + " " + random.choice(subject) + " " + random.choice(action) + " " + random.choice(MF_1_1) + " " + random.choice(Adjectives) +  " " +  random.choice(foodlist))
        print(random.choice(Adjectives) + " " + random.choice(subject) + " " + random.choice(action) + " " + random.choice(MF_1_1) + " " + random.choice(MF_1_1) + " " + random.choice(Adjectives) +  " " +  random.choice(foodlist))
        print(random.choice(Adjectives) + " " + random.choice(subject) + " " + random.choice(action) + " " + random.choice(MF_1_1) + " " +  random.choice(foodlist) + "\n")
    
    else: 
    
        print(random.choice(location) + random.choice(subject) + " " + random.choice(action) + " " + random.choice(Adjectives) + " " + random.choice(foodlist) + " " +  random.choice(transition) + " " +  random.choice(foodlist))
        print(random.choice(words) + " " +  random.choice(words) + " " +  random.choice(Adjectives) + " " +  random.choice(words) + " "+ random.choice(MF_1_1) + " " +  random.choice(words))
        print(random.choice(transition) + " " + random.choice(MF_1_1) + " "+ random.choice(placelist) + " " + random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " "+ random.choice(Adjectives)+ " "+ random.choice(MF_1_1) + " " +  random.choice(words) + "\n")
    
    
    counter += 1 #counter increment


# In[17]:


import nltk
nltk.download('wordnet')


# In[23]:


from nltk.corpus import wordnet as wn
food = wn.synset('food.n.02')
list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))


# In[ ]:




