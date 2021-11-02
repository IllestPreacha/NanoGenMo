#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random
import nltk


from nltk.corpus import wordnet as wn
food = wn.synset('food.n.02')
foodlist = list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))

place = wn.synset('place.n.02')
placelist = list(set([w for s in place.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))

location = ["In California, ", "Outside of Earth, ","On the Safari Grounds, ", "At the Extension of the Tundra, ", "Within the Breeze on a lonely day at the beach, ", "While hiking the grandest of underwater Volcanoes, ", "Looking for the windiest village to maintain wind energy, ", "Hiding in the depths of Quicksand, ", "Flying at the higher limits of the atmosphere the Speed of the Light, "]
action = [" voted against "," eats "," flies with ", " destroys ", "fights", "voted with", "danced with", "mimics", "transform into"]
transition = [" while holding a ", " during times of conflict with a ", " instead of eating a ", "playing with ", "joking as ", "dressing up as ", "cosplaying as ", "checking up on ", "fighting with ", "fighting against "]

with open("Adjectives.txt", "r") as adj:  #open and read the text file
    adjectives = adj.read()  #give the file a variable name 
    adjectivesUsed = list(map(str,adjectives.split())) #individuals words
    
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
    

for x in location * 100 :
    print(random.choice(location) + random.choice(subject) + " " + random.choice(action) + " " + random.choice(adjectivesUsed) + " " + random.choice(foodlist) + " " +  random.choice(transition) + " " +  random.choice(foodlist))
    print(random.choice(words) + " " +  random.choice(words) + " " +  random.choice(adjectivesUsed) + " " +  random.choice(words) + " "+ random.choice(MF_1_1) + " " +  random.choice(words))
    print(random.choice(transition) + random.choice(placelist) + " " + random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " "+ random.choice(adjectivesUsed)+ " "+ random.choice(MF_1_1) + " " +  random.choice(words))
    print(random.choice(words) + " " +  random.choice(words) + " " +  random.choice(adjectivesUsed) + " " +  random.choice(words) + " "+ random.choice(MF_1_1) + " " +  random.choice(words))
    print(random.choice(transition) + random.choice(placelist) + " " + random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " "+ random.choice(adjectivesUsed)+ " "+ random.choice(MF_1_1) + " " +  random.choice(words))
    print(random.choice(words) + " " +  random.choice(words) + " " +  random.choice(adjectivesUsed) + " " +  random.choice(words) + " "+ random.choice(MF_1_1) + " " +  random.choice(words))
    print(random.choice(transition) + random.choice(placelist) + " " + random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " "+ random.choice(adjectivesUsed)+ " "+ random.choice(MF_1_1) + " " +  random.choice(words) + "\n")


# In[22]:


import nltk
nltk.download('wordnet')


# In[23]:


from nltk.corpus import wordnet as wn
food = wn.synset('food.n.02')
list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))


# In[ ]:




