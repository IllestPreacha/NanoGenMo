#!/usr/bin/env python
# coding: utf-8

# In[31]:


import random
import nltk


from nltk.corpus import wordnet as wn
food = wn.synset('food.n.02')
foodlist = list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))

place = wn.synset('place.n.02')
placelist = list(set([w for s in place.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))

location = ["In California, ", "Outside of Earth, ","On the Safari Grounds "]
subject = [" Timmy ", " Pluto ", " Zeus ", " Manopunk ", "Erica", "DegaTron"]
action = [" voted against "," eats "," flies with ", " destroys "]
transition = [" while holding a ", " during times of conflict with a ", " instead of eating a "]

with open("Adjectives.txt", "r") as adj:  #open and read the text file
    adjectives = adj.read()  #give the file a variable name 
    adjectivesUsed = list(map(str,adjectives.split())) #individuals words

with open("ManoPunk.txt", "r") as file:  #open and read the text file
    allText = file.read()  #give the file a variable name 
    words = list(map(str,allText.split())) #individuals words
    
with open("AppleCrisp_Clean.txt", "r") as cs_1:
    csdip_1 = cs_1.read()
    cs_1_1 = list(map(str,csdip_1.split())) #individuals words

with open("MealFact_Class_Nature_WordAssc_Clean.txt", "r") as cs_MF:
    csdip_MF = cs_MF.read()
    MF_1_1 = list(map(str, csdip_MF.split())) #individuals words
    

for x in location * 10 :
    print(random.choice(location) + random.choice(subject) + random.choice(action) + " " + random.choice(adjectivesUsed) + " " + random.choice(foodlist) + " " +  random.choice(transition) + random.choice(foodlist))
    print(random.choice(words) + " " +  random.choice(words) + " " +  random.choice(adjectivesUsed) + " " +  random.choice(words) + " "+ random.choice(MF_1_1) + " " +  random.choice(words))
    print(random.choice(transition) + random.choice(placelist) + " " + random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " "+ random.choice(adjectivesUsed)+ " "+ random.choice(MF_1_1) + " " +  random.choice(words))


# In[22]:


import nltk
nltk.download('wordnet')


# In[23]:


from nltk.corpus import wordnet as wn
food = wn.synset('food.n.02')
list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))


# In[ ]:




