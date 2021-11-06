#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import nltk


from nltk.corpus import wordnet as wn
food = wn.synset('food.n.02')
foodlist = list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))

place = wn.synset('place.n.02')
placelist = list(set([w for s in place.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))


location = ["While Chewing on a heavy breakfast in the dinner, ""Being in the underwater City of  Aquapolis, ","In California, ", "Outside of Earth, ","On the Safari Grounds, ", "At the Extension of the Tundra, ", "Within the Breeze on a lonely day at the beach, ", "While hiking the grandest of underwater Volcanoes, ", "Looking for the windiest village to maintain wind energy, ", "Hiding in the depths of Quicksand, ", "Flying at the higher limits of the atmosphere the Speed of the Light, "]
action = [" voted against "," eats "," flies with ", " destroys ", "fights", "voted with", "danced with", "mimics", "transform into"]
transition = [" while holding a ", " during times of conflict with a ", " instead of eating a ", "playing with ", "joking as ", "dressing up as ", "cosplaying as ", "checking up on ", "fighting with ", "fighting against "]


with open("Adjectives.txt", "r") as adj:  #open and read the text file
    adjectives = adj.read()  #give the file a variable name 
    adjectivesUsed = list(map(str,adjectives.split())) #individuals words
    
with open("dates.txt", "r") as dates_txt:  #open and read the text file
    dates = dates_txt.read()  #give the file a variable name 
    dateslist = list(map(str,dates.split())) #individuals words
    
with open("Names_nanogen.txt", "r") as names:
    names1 = names.read()
    subject = list(map(str,names1.split())) #individuals words

with open("ManoPunk.txt", "r") as file:  #open and read the text file
    allText = file.read()  #give the file a variable name 
    words = list(map(str,allText.split())) #individuals words
    
with open("AppleCrisp_Clean.txt", "r") as cs_1:
    csdip_1 = cs_1.read()
    cs_1_1 = list(map(str,csdip_1.split())) #individuals words

with open("MealFact_Class_Nature_WordAssc_Clean.txt", "r") as cs_MF:
    csdip_MF = cs_MF.read()
    MF_1_1 = list(map(str, csdip_MF.split())) #individuals words
    
with open("Classes.txt", "r") as classes:
    inhabitant = classes.read()
    inhabitants = list(map(str, inhabitant.split())) #individuals words
    
print("Welcome to the lost diaries of different worlds, our goal is to try to put the pieces together")
print("located within this document of lost text: are the diary entries, dates and at times: an inventory list")
print("Enjoy your read, enjoy your time. May the thing you are looking , be found in these lines" + "\n")
  

counter = 0 #set the counter outside the loop
chapter = 0 #chapter counter

for x in location * 130 : #for loop that runs 100 times the amount of items in the list of location
    
    chapter = chapter + 1 #increment for chapter
    
    #using modulo to set condiitons with the if/elif/else  statements
        
    if counter %15 == 0: #setting the amountof chapters
        print("CHAPTER " + str(chapter)[:-1] + "\n") #slicing the last digit, so chapter 10 isnt chapter 101
        
    if counter %45 == 0: #setting the random list of dates
        print(random.choice(dateslist) + ": " + random.choice(adjectivesUsed).upper() + " & " + random.choice(cs_1_1) + "\n") 
        
    if counter %90 == 0:
        print("These are the inventory items located in this realm: ")
        print(random.choice(cs_1_1))
        print(random.choice(cs_1_1))
        print(random.choice(cs_1_1))
        print(random.choice(cs_1_1))
        print(random.choice(cs_1_1) + "\n")
        
        """
        Degrees minutes seconds

        Uses the format "DDD MM SS + compass direction (N, S, E, or W)." 
        Latitudes range from 0 to 90 and longitudes range from 0 to 180. 
        The last degree, minute, or second or a latitude or longitude may contain a decimal portion.
        
        41 25 01N, 120 58 57W

        41º25'01"N, 120º58'57"W

        S17 33 08.352, W69 01 29.74
        """
        
        Compass = ["N","E","W","S"] #part of the Latitude + Longitude thing
    
        
        print("Planetary information pertaining to the where the diary entry was found" + "\n")
        print("World Version: " + str(random.randrange(150, 570)))
        print("Latitude in this realm: " + str(random.randrange(0,90)) + " " + str(random.randrange(0,360)) + " " + str(random.randrange(0,90)) + " " + random.choice(Compass))
        print("Longitude in this realm: " + str(random.randrange(0,90)) + " " + str(random.randrange(0,360)) + " " + str(random.randrange(0,90)) + " " + random.choice(Compass) + "\n")
        print("Number of Inhabitants: " + str(random.randrange(100000,400000)))
        print("Number of " + random.choice(inhabitants) + ": " + str(random.randrange(1000,10000)))
        print("Number of " + random.choice(inhabitants) + ": " + str(random.randrange(1000,10000)))
        print("Number of " + random.choice(inhabitants) + ": " + str(random.randrange(1000,10000)))
        print("Number of " + random.choice(inhabitants) + ": " + str(random.randrange(1000,10000)) + "\n")
    
    if counter  % 10 < 5 :
        print(random.choice(location) + random.choice(subject) + " " + random.choice(action) + " " + random.choice(adjectivesUsed) + " " + random.choice(foodlist) + " " +  random.choice(transition) + " " +  random.choice(foodlist))
        print(random.choice(words) + " " +  random.choice(words) + " " +  random.choice(adjectivesUsed) + " " +  random.choice(words) + " "+ random.choice(MF_1_1) + " " +  random.choice(words))
        print(random.choice(transition) + random.choice(placelist) + " " + random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " "+ random.choice(adjectivesUsed)+ " "+ random.choice(MF_1_1) + " " +  random.choice(words))
        print(random.choice(words) + " " +  random.choice(words) + " " +  random.choice(adjectivesUsed) + " " +  random.choice(words) + " "+ random.choice(MF_1_1) + " " +  random.choice(words))
        print(random.choice(transition) + random.choice(placelist) + " " + random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " "+ random.choice(adjectivesUsed)+ " "+ random.choice(MF_1_1) + " " +  random.choice(words))
        print(random.choice(words) + " " +  random.choice(words) + " " +  random.choice(adjectivesUsed) + " " +  random.choice(words) + " "+ random.choice(MF_1_1) + " " +  random.choice(words))
        print(random.choice(transition) + random.choice(placelist) + " " + random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " "+ random.choice(adjectivesUsed)+ " "+ random.choice(MF_1_1) + " " +  random.choice(words) + "\n")
    
    elif counter % 10 > 5 and counter % 10 < 8:
        
        print(random.choice(adjectivesUsed) + " " + random.choice(subject) + " " + random.choice(action) + " " + random.choice(MF_1_1) + " " + random.choice(adjectivesUsed) +  " " +  random.choice(foodlist))
        print(random.choice(adjectivesUsed) + " " + random.choice(subject) + " " + random.choice(action) + " " + random.choice(MF_1_1) + " " + random.choice(MF_1_1) + " " + random.choice(adjectivesUsed) +  " " +  random.choice(foodlist))
        print(random.choice(adjectivesUsed) + " " + random.choice(subject) + " " + random.choice(action) + " " + random.choice(MF_1_1) + " " +  random.choice(foodlist) + "\n")
    
    else: 
    
        print(random.choice(location) + random.choice(subject) + " " + random.choice(action) + " " + random.choice(adjectivesUsed) + " " + random.choice(foodlist) + " " +  random.choice(transition) + " " +  random.choice(foodlist))
        print(random.choice(words) + " " +  random.choice(words) + " " +  random.choice(adjectivesUsed) + " " +  random.choice(words) + " "+ random.choice(MF_1_1) + " " +  random.choice(words))
        print(random.choice(transition) + " " + random.choice(MF_1_1) + " "+ random.choice(placelist) + " " + random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " "+ random.choice(adjectivesUsed)+ " "+ random.choice(MF_1_1) + " " +  random.choice(words) + "\n")
    
    
    counter += 1 #counter increment


# In[22]:


import nltk
nltk.download('wordnet')


# In[23]:


from nltk.corpus import wordnet as wn
food = wn.synset('food.n.02')
list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))


# In[ ]:




