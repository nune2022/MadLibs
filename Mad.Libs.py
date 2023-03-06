import random
def text1():
    number= input("Type a number")
    Measure_of_time = input("input Measure of time")
    Mode_of_Transportation = input("Mode of Transportation")
    Adjective = input("Adjective")
    Adjective2 = input("Adjective2")
    noun= input("noun")
    Color= input("color")
    part_of_the_body = input("part of the body")
    Verb= input("verb")
    Number2 = input("Type number")
    Noun2 = input("noun")
    Noun3 = input("noun")
    part_of_the_body2 = input("part of the body")
    verb = input("verb")
    Noun4 = input("noun")
    Adjective3 = input("adjective")
    Silly_Word = input("Silly Word")

    text1 = f'''It was about {number} {Measure_of_time} ago when I arrived at the hospital in a 
{Mode_of_Transportation}. The hospital is a/an {Adjective} place, there are a lot of {Adjective2} {noun} 
here. There are nurses here who have {Color} {part_of_the_body}. If someone wants to come into my room I told them that they have to 
{Verb} first. I’ve decorated my room with {Number2} {Noun2}. Today I talked to a doctor and they were wearing a {Noun3} on their 
{part_of_the_body2}. I heard that all doctors {verb} {Noun4} every day for breakfast. The most {Adjective3}
 thing about being in the hospital is the {Silly_Word} {noun} !
'''
    print(text1)



def text2():
    name = input("Type your favorit name")
    noun = input("noun")
    feeling = input("Feeling")
    verb = input("verb")
    feeling2 = input("Feeling")
    animal = input("animal")
    verb2 = input("verb")
    color = input("color")
    verb3 = input("verb +ing")
    averb = input("avaerb + ly")
    number = input("number")
    Measure_of_time = input("input Measure of time")
    color1 = input("color")
    animal2 = input("animal")
    number2 = input("number")
    Silly_Word = input("Silly Word")
    noun2 = input("noun")


    text2 = f''' This weekend I am going camping with {name}. 
I packed my lantern, sleeping bag, and {noun}. I am so {feeling} to {verb} in a tent. 
I am {feeling2} we might see a(n) {animal}, I hear they’re kind of dangerous.
While we’re camping, we are going to hike, fish, and {verb2}. I have heard that the {color} lake is great
for {verb3}. Then we will {averb} hike through the forest  
for {number} {Measure_of_time}. If I see a {color1} {animal2} while hiking, I am going 
to bring it home as a pet! At night we will tell {number2} {Silly_Word} stories and roast 
{noun2} around the campfire!!
'''
    print(text2)

def text3():
    name = input("Type your favorit name")
    adjective = input("adjective")
    color = input("color")
    animal = input("animal")
    place = input("place")
    adjective2 = input("adjective")
    Magical_Creature_plural = input("Magical Creature (Plural)")
    adjective3 = input("adjective")
    Magical_Creature_plural1 = input("Magical Creature (Plural)")
    room = input("room in a house")
    noun = input("noun")
    noun1 = input("noun")
    noun_plural = input("Noun(Plural)")
    adjective4 = input("adjective")
    noun_plural1 = input("Noun(Plural)")
    number = input("number")
    Measure_of_time = input("input Measure of time")
    verb = input("verb +ing")
    adjective5 = input("adjective")
    noun2 = input("noun")


    text3 = f''' Dear {name}, I am writing to you from a {adjective} 
castle in an enchanted forest. I found myself here one day after going for a ride on a 
{color} {animal} in {place}. There are {adjective2} {Magical_Creature_plural} and {adjective3}
{Magical_Creature_plural1} here! In the {room} there is a pool full of {noun}.
I fall asleep each night on a {noun1} of {noun_plural} and dream of {adjective4} {noun_plural1}. 
It feels as though I have lived here for {number} {Measure_of_time}. I hope one day you can visit, 
although the only way to get here now is {verb} on a {adjective5} {noun2}!!
'''
    print(text3)

choice = input("please input number 1, 2, 3 or 4")
if choice == '1':
    text1()
elif choice == "2":
    text2()
elif choice =='3':
    text3()
elif choice =='4':
    if random.randrange(1, 3) == 1:
        text1()
    elif random.randrange(1, 3) == 2:
        text2()
    else:
        text3()
else:
    print("tipe a correct number, please")



