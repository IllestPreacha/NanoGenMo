#!/usr/bin/env python
# coding: utf-8

# In[10]:


import random
import nltk
import math
import json     #allows us to use the json file as it is without having to convert to text 

filename = input("what is the name of this diary ")
fileNameFile = filename +  ".txt" #
f = open(filename + ".txt", "a")


from nltk.corpus import wordnet as wn

class wordnet: #making a class to simplify the code
    def __new__(self,wordnetting): #new allows return to be used by a different value unlike _init'
        wordnetting = wn.synset(wordnetting +'.n.02')
        wordnetting = list(set([w for s in wordnetting.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))    
        
        return wordnetting #returns the list
    
foodlist = wordnet("food") #the list of the food is being called into the class
placelist = wordnet("place") #list of place is being called into the class
spacelist = wordnet("space") 

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
subject  = termsUsed("Names_nanogen")
words = termsUsed("ManoPunk")
cs_1_1 = termsUsed("AppleCrisp_Clean")
MF_1_1 = termsUsed("MealFact_Class_Nature_WordAssc_Clean")
inhabitants = termsUsed("Classes")

#phrases that help the novel read better

location = ["While Chewing on a heavy breakfast in the dinner, ""Being in the underwater City of  Aquapolis, ","In California, ", "Outside of Earth, ","On the Safari Grounds, ", "At the Extension of the Tundra, ", "Within the Breeze on a lonely day at the beach, ", "While hiking the grandest of underwater Volcanoes, ", "Looking for the windiest village to maintain wind energy, ", "Hiding in the depths of Quicksand, ", "Flying at the higher limits of the atmosphere the Speed of the Light, "]
action = [" voted against "," eats "," flies with ", " destroys ", "fights", "voted with", "danced with", "mimics", "transform into"]
transition = [" while holding a ", " during times of conflict with a ", " instead of eating a ", "playing with ", "joking as ", "dressing up as ", "cosplaying as ", "checking up on ", "fighting with ", "fighting against "]

#intro

reader_name = input ("What is your travellers name? ") #user prompt to get some interactive components 
    
print("Welcome to the lost diaries of different worlds, " + reader_name + " !" + "\n" + "Our goal is to try to put the pieces together",file=f)
print("located within this document of lost text: are the diary entries, dates and at times: an inventory list",file=f)
print("Enjoy your reading, enjoy your time. May the thing you are looking , be found in these lines" + "\n",file=f)
  
#counters    
    
counter = 0 #set the counter outside the loop
chapter = 1 #chapter counter

  
for x in location * 130 : #for loop that runs 100 times the amount of items in the list of location
    
    #using modulo to set condiitons with the if/elif/else  statements
        
    if counter %15 == 0: #setting the amountof chapters
        print("\n", file=f)
        #to get the chapters flowing right and not jump numbers, in float notation but could be useful for later
        Heading = "CHAPTER " + str(math.trunc(chapter / 15)) #matches the modulo loop & stripping the floating value for now
        print(Heading.center(88,"-") + "\n",file=f) # padding for the heading to occur on both sides
        print("\n", file=f)
        
    
    if Heading.endswith('7') or Heading.endswith('3') == True: #for the strings in the heading variable that end with a 7 and 3 
        Beware = "Beware of Changes in This World, "
        print(Beware.rjust(random.randrange(90,144)) + "\n",file=f) # padding for right adjustment
        
        #also adding the reader's input from earlier to give them a personal warning of these worlds
        
        print(Beware.rjust(random.randrange(7,37)).upper() + reader_name.upper() + " !" +  "\n",file=f) # padding for right adjustment
        print(Beware.rjust(random.randrange(44,78)) + "\n",file=f) # padding for right adjustment
    
    if counter %45 == 0: #setting the random list of dates
        print(random.choice(dates) + ": " + random.choice(Adjectives).upper() + " & " + random.choice(cs_1_1).upper() + " in a " + random.choice(spacelist) + "\n",file=f) 
        
    if counter %90 == 0:
        print("These are the inventory items located in this realm: ",file=f)
        
        for items in range(5): #print 5 times
            print(random.choice(cs_1_1).center(10,"*"),file=f) #padding the inventory to stick out
        
        print("\n",file=f)

            
        Compass = ["N","E","W","S"] #part of the Latitude + Longitude thing
    
        print("Planetary information pertaining to the where the diary entry was found" + "\n",file=f)
        print("World Version: " + str(random.randrange(150, 570)),file=f)
        print("Latitude in this realm: " + str(random.randrange(0,90)) + " " + str(random.randrange(0,360)) + " " + str(random.randrange(0,90)) + random.choice(Compass),file=f)
        print("Longitude in this realm: " + str(random.randrange(0,180)) + " " + str(random.randrange(0,360)) + " " + str(random.randrange(0,90)) + random.choice(Compass) + "\n",file=f)
        print("Number of Inhabitants: " + str(random.randrange(100000,400000)),file=f)
        
        for items in range(5): #print 5 times
            print("Number of " + random.choice(inhabitants) + ": " + str(random.randrange(1000,10000)),file=f)
        print("\n",file=f)
    
    
    if counter  % 10 < 5 :
        print(random.choice(location) + random.choice(subject) + " " + random.choice(action) + " " + random.choice(Adjectives) + " " + random.choice(foodlist) + " " +  random.choice(transition) + " " +  random.choice(foodlist),file=f)
        
        for phrases in range(3):
            print(random.choice(transition) + random.choice(placelist) + " " + random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " "+ random.choice(Adjectives)+ " "+ random.choice(MF_1_1) + " " +  random.choice(words),file=f)
            print(random.choice(words) + " " +  random.choice(words) + " " +  random.choice(Adjectives) + " " +  random.choice(words) + " "+ random.choice(MF_1_1) + " " +  random.choice(words),file=f)
        
        print(random.choice(transition) + random.choice(placelist) + " " + random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " "+ random.choice(Adjectives)+ " "+ random.choice(MF_1_1) + " " +  random.choice(words) + "\n",file=f)
    
    elif counter % 10 > 5 and counter % 10 < 8:
        
        print(random.choice(Adjectives) + " " + random.choice(subject) + " " + random.choice(action) + " " + random.choice(MF_1_1) + " " + random.choice(Adjectives) +  " " +  random.choice(foodlist),file=f)
        print(random.choice(Adjectives) + " " + random.choice(subject) + " " + random.choice(action) + " " + random.choice(MF_1_1) + " " + random.choice(MF_1_1) + " " + random.choice(Adjectives) +  " " +  random.choice(foodlist),file=f)
        print(random.choice(Adjectives) + " " + random.choice(subject) + " " + random.choice(action) + " " + random.choice(MF_1_1) + " " +  random.choice(foodlist) + "\n",file=f)
    
    else: 
    
        print(random.choice(location) + random.choice(subject) + " " + random.choice(action) + " " + random.choice(Adjectives) + " " + random.choice(foodlist) + " " +  random.choice(transition) + " " +  random.choice(foodlist),file=f)
        print(random.choice(words) + " " +  random.choice(words) + " " +  random.choice(Adjectives) + " " +  random.choice(words) + " "+ random.choice(MF_1_1) + " " +  random.choice(words),file=f)
        print(random.choice(transition) + " " + random.choice(MF_1_1) + " "+ random.choice(placelist) + " " + random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " " +  random.choice(words) + " "+ random.choice(Adjectives)+ " "+ random.choice(MF_1_1) + " " +  random.choice(words) + "\n",file=f)
        
    counter += 1 #counter increment
    chapter += 1 #increment for chapter
    
    
f.close()

#This will take the above text and use the lolcat tranzlashun to change the component of the text into another form
#previously written code that seem like a good fit for the nanogenmo


with open("tranzlashun.json") as json_file:
    my_dict = json.load(json_file)   #bindings noted in the dictionary are used as a dictionary
    
    split_filename = fileNameFile.split(".") #seperate the file name and the file type
    filename_lolz = split_filename[0] + "_LostInTranslation.txt"    #changes the name of the file to its lolcat counterpart

    
    file_test = open(fileNameFile, "r") # code block that reads and close the files
    contents = file_test.read()
    file_test.close()

print(contents) #a print to make sure it works 

word_intake2 = contents.split(" ") #makes the words into a list of their own

f = open(filename_lolz, "x") #make a new empty, placeholder for the words that are about to come


for counter in range(len(word_intake2)):    # this block of code users a counter and index to see if the words in the text file are similar to the json file
    index = counter
    if word_intake2[index] in list(my_dict): #if they are they are then entered into the new file as their lolcat counterpart else , they are entered as they are now
        translate = word_intake2[index]
        print(my_dict[translate])
        f = open(filename_lolz, "a")
        f.write(my_dict[translate] + " ")
        f.close
    else: 
        f = open(filename_lolz, "a")
        f.write(word_intake2[index] + " ")
        f.close

f = open(filename_lolz,"r") #re read the the file, might be a bit overkill but just direct confirmation that the new file works alongside 
print(f.read())


# In[ ]:





# In[ ]:




