import time
import random
#adding some lists to use in randomness later in the game.
weather = ["stormy", "extremely hot", "unbearable", "hot", "freezing"]
sound =  ["a wolf", "a snake", "thunder", "a dog", "wild animal"]
food = ["camel meat and bread",
        "sheep meat and bread",
        "plane bread, you are hungry you can't complain",
        "fruit salad",
        "plate of rice",
        "salad",
        "goat cheese",
        "chicken and bread",
        "strange sandwich, it smells like goat cheese,"
        "lets hope it tastes good.",
        "coconut slice",
        "watermelon slice"]
drink = ["warm water",
         "water",
         "cold water",
         "a..smoothie? How did it come here?",
         "orange juice",
         "coctail",
         "coconut water",
         "tea? that may do",
         "green juice.."]
pet = ["a cat",
       "a parrot",
       "a rabbit",
       "a turtle",
       "a..goat?",
       "a bird",
       "a monkey",
       "a cactus, it may be your imagination"
       "or dehydration but"] #make a pets list to use in random.
pet_condition =["it looks hungry",
                "it looks like it has a broken bone",
                "it looks like it likes you",
                "it is trying hard to keep up with your wide footsteps",
                "It looks lonly",
                "It looks like it is still a baby"]#and pet conditions too.
pet_condition_2 = ["it is trying hard to keep up with your wide footsteps",
                   "it looks like it loves you now",
                   "it looks hungry",
                   "it is hopping behind you happily"]
pet_status =["it is asleep, sshhhh",
             "It is happy to be with you.",
             "it is chewing on a random stick on the ground"
             ".. it is an ice-cream stick, yuck.",
             "it is just chilling",
             "it is eating.. your backup food,"
             "it is its now."] #and pet's status.
#some trivia questions for bonus score.
trivia_questions = [
    {"question":"What do you use to write on a blackboard?",
     "answer":"chalk"},
    {"question":"What’s the name of the organ that helps you breathe?",
     "answer":"lungs"},
    {"question":"What’s the colored part of your eye called?",
     "answer":"iris"},
    {"question":"What do you call a house made of ice?",
     "answer":"igloo"},
    {"question":"What is the hardest natural substance on Earth?",
     "answer":"diamond"},
    {"question":"What planet is known for its rings?",
     "answer":"saturn"},
    {"question":"What is H2O more commonly known as?",
     "answer":"water"},
    {"question":"What do we call molten rock after it erupts from a volcano?",
     "answer":"lava"},
    {"question":"What part of the body pumps blood?",
     "answer":"heart"},
    {"question":"What tool tells you which direction is north?",
     "answer":"compass"},
    {"question":"In a website browser address bar, what does 'www' stand for?",
     "answer": "world wide web"},
    {"question":"In what year was the Internet opened to the public?",
     "answer": "1993"},
    {"question":"What’s the largest animal on Earth?",
     "answer":"whale"},
    {"question":"What is the largest desert on Earth?",
     "answer":"antarctica"},
    {"question":"What color do you get if you mix red and yellow?",
     "answer":"orange"},
    {"question":"What do cows drink?",
     "answer":"water"},
    {"question":"What season comes after winter?",
     "answer":"spring"},
    {"question":"What has hands but no arms or legs?",
     "answer":"clock"},
    {"question":"What plant is famous for surviving in deserts?",
     "answer":"cactus"},
    {"question":"What animal is known as the 'ship of the desert'?",
     "answer":"camel"},
    {"question":"What’s the main gas in the air we breathe?",
     "answer":"nitrogen"},
    {"question":"What’s the name of the red planet?",
     "answer":"mars"},
    {"question":"What is full of holes but still holds water?",
     "answer":"sponge"},
    {"question":"What’s something you break before you use it?",
     "answer":"egg"},
    {"question":"What language do people speak in Brazil?",
     "answer":"portuguese"},
    {"question":"What fruit has its seeds on the outside?",
     "answer":"strawberry"},
    {"question":"What’s the term for an oasis-dwelling nomadic group?",
     "answer":"bedouin"},
    {"question":"What kind of reptile often lives in deserts?",
     "answer":"lizard"},
]
total_score = 0 #Score variable.
lose_count = 0 #Variable to keep tracj of how much did the player lose.
inventory = [] #The Inventory.
pet_name = "" #Pet's name.
endings = [] #List of endings.
def print_pause(x): #Make it easier to print and wait.
    print(x) #prints the text in brackets.
    time.sleep(2) #waits for 2 secs.
    print("") #make an empty line between each line and the other.
def check_inventory(): #For offering the player to check what they have.
    #checking if the inventory is empty or not, if not views it.
    if not inventory:
        print_pause("Your inventory is empty!")
    else:
        print_pause(f"You have {inventory} in your inventory.")
def found_item(item): #function for when the player finds anything.
    global total_score #working with the global score var.
    while True: #making a loop.
        #taking the player's choice.
        take = input("Take it? (Y/N)").lower().strip()
    #checking the player's choice.
        if take in ["y", "yes"]:
            inventory.append(item) #adding the item to the inventory.
            print_pause (f"The {item} has been added" " "
                         "to your inventory successfully!")
            total_score += 10 #adding points if the player took it.
            print_pause(f"You get 10 points for taking the {item}!")
            #keeping the player on track with there score.
            print_pause (f"Your total score now is {total_score}")
            #calling the function that asks the player
            #to check what they have in the inventory.
            check_inventory_got_something()
            break
        elif take in ["n", "no"]:
            print_pause(f"You left the {item} behind")
            check_inventory_got_something()
            break
        else:
            print_pause("Invalid input. Please type"" "
                        "'Y' for Yes or 'N' for No.")
def new_ending(x): #A function to add endings to the list easily.
    #checking if the player already unlocked the ending, if not:
    if x not in endings:
        endings.append(x) #adds it to the endings list.
        print_pause(f"You have unlocked a new ending:'{x}'")
    else:
        pass
        play_again()
#Check inventory function when the player gets stuff.
def check_inventory_got_something():
    i = input("Enter I if you want to check the items"" "
              "in your inventory, press" " "
              "ENTER to skip.").strip().lower() #Taking input
    if inventory and i == "i": #if the inventory isn't empty and input is "i".
        #tells the player their inventory items.
        print_pause(f"You have {inventory}"" "
                    "in your inventory.")
    elif not inventory and i == "i": #If inventory is empty and inpuy is "i".
        #tells the player that their inventory is empty.
        print_pause ("Your inventory is empty!")
    else: #if input isn't "i".
        pass  #do nothing.
def choice(question): #Make a function for choices.
    #making a variable with strip to del
    #the unwanted spaces and lower to make letters lower case.
    while True: #a loop.
        player_choice = input(question).strip().lower()
    #if it the choice isn't a thing from the list it
    #will keep looping till the player enters a suitable entery.
        if player_choice in ["1", "2", "i"]:
            return player_choice
        else:
            print_pause("Invaild input, please enter '1', '2' or 'i' only")
def game_over(reason): #Function for when the player loses.
    global lose_count #working with the global lose var.
    global total_score #working with the global score.
    total_score = 0 #Restarting score by setting it to 0 again.
    print_pause(f"Game Over! You {reason}!") #telling the player why they lost.
    lose_count += 1 #increasing the lose count by 1.
    #telling the player how many times did they die.
    print_pause(f"You have lost {lose_count} times!")
    play_again() #calling the function of replaying.
def play_again(): #Function for replaying.
    global total_score
    global inventory
    global pet_name
    total_score = 0
    pet_name = ""
    inventory = []
    #telling the player the endings they got till now.
    print_pause(f"You have unlocked these endings: {endings}")
    while True: #making a loop.
        answer = input("Want to play again?"" "
                       "Enter (Y/N).").strip().lower() #taking input/answer.
        if answer.lower() in ["y", "yes"]: #checking the answer.
            beginning() #calling the function of the beginning of the game.
            break #breaks the loop.
            #checking the answer if it is not "y" or "yes".
        elif answer.lower() in ["n", "no"]:
            exit() #closing the program (exitting it).
        else:
            #asking again if the input is wrong.
            print_pause("Invalid input. Please type 'Y'"" "
                        "for Yes or 'N' for No.")
#Function for the beginning choices because I had to use it in multiple places.
def beginning_choices():
    while True: #making a loop.
        #offering choices.
        print_pause("Enter 1 to walk toward the water pond.")
        print_pause("Enter 2 to go toward the jeep.")
        print_pause("Enter I to Check your inventory")
        choice_b = choice("What will you do?") #taking choice.
        #checking choice.
        if choice_b == "i":
            check_inventory()
        #changing routes based on the choice.
        elif choice_b == "1":
            mirage()
            break
        elif choice_b == "2":
            jeep()
            break
def trivia(): #trivia questions function.
    global total_score #working with the global score variable.
    #getting a random question from the trivia_questions list.
    question = random.choice(trivia_questions)
    print_pause(question["question"]) #printing the question.
    correct_answer = question["answer"] #storing the correct answer.
    #taking the player's answer.
    player_answer = input("What is your"" "
                          "answer?").strip().lower()
    #checking the player's answer.
    if player_answer == correct_answer: #if it is right:
        print_pause("Correct! You got 5 points!")
        total_score += 5  #increasing the total score by 5.
        print_pause(f"Your total score now is {total_score}"" "
                    "points!")#telling the player their score.
    else: #if the answer is wrong:
        print_pause(f"Wrong! The correct answer was {correct_answer}!")
        total_score -= 5 #decreasing the total score by 5.
        if total_score >= 0:
            #telling the player their score.
            print_pause(f"Your score total now is {total_score} points!")
        else: #if they have less than 0 points.
            print_pause(f"Your score total now is {total_score}"" "
                        "points! You lost!")
            game_over("have less than 0 points! Do better.")
#function for the cactus (the character asking the trivia quizes).
def cactus_questions(comment, cactus_last_line):
    while True: #making a loop.
        #taking input.
        trivia_play = input("Will you agree?"" "
                            "(Y/N)").strip().lower()
        #checking input.
        if trivia_play in ["y","yes"]:
            print_pause("You agree to the floating cactus offer"" "
                        ", it grins widely and askes:")
            trivia_warning()
            trivia()
            print_pause("Next round!")
            trivia()
            print_pause("And here is the last round!")
            trivia()
            print_pause(cactus_last_line)
            print_pause(comment)
            break
        elif trivia_play in ["n","no"]:
            print_pause("You refuse as a normal sane human being.")
            print_pause("it poutes and says 'fine! I will"" "
                        "be back!' then it vanishes.")
            print_pause(comment)
            break
        else:
            print_pause("Invalid input. Please type"" "
                        "'Y' for Yes or 'N' for No.")
def trivia_warning():
    #a warning that comes once before trivia games.
    print_pause("Answer these questions and earn 5 points"" "
                "for each right one, if you answered wrongly"" "
                "you will lose 5 points!")
    print_pause("Note:check your spelling and keep"" "
                "in mind that all the answers are singular"" "
                "plain words without 'the' or 'a'!")
def beginning(): #The intro of the game.
    #descriping the surroundings.
    #getting a random weather from the weather list.
    desert_weather = random.choice(weather)
    print_pause("You find yourself in the middle of the desert.")
    #called the var that has the ran weather.
    print_pause(f"You don’t remember how you got here. Your head is foggy,"
                " " f"and the weather is {desert_weather}.")
    print_pause("You’re thirsty.")
    print_pause("Hungry.")
    print_pause("Dizzy.")
    print_pause("The sand stretches endlessly in every direction.")
    print_pause("You hear a strange sound, you look and"
                " " "spot a grinning floating cactus.")
    print_pause("Yes, it has a face.")
    print_pause("You don't know if it is just dehydration"
                " " "or that you have lost your mind")
    print_pause("'Hi there! Do you want to play"
                " " "a small trivia game? :D' it says")
    print_pause("'It will be 3 trivia questions,"
                " " "if you get 1 right you will earn 5 points!"
                " " "That is a great way to increase your total score!'")
    print_pause("'fun right? :D'")
    #calling cactus trivia function.
    cactus_questions("That was weird.","'That was soooo much fun!'"
                     " " "it said 'see you later!' said before vanishing")
    #offering the player choices that changes in the routes of the game.
    print_pause("You looked around you and there was an empty bucket,"
                " " "you remembered something about having to fill it.")
    found_item("bucket") #calling found item function.
    print_pause("In the distance, you spot two things:")
    print_pause("-A shimmering water pond far to your left.")
    print_pause("-A black jeep, strange and unmoving, off to the right.")
    print_pause("You have to choose. You can’t just sit here"
                " " "and wait for the sun to finish you off.")
    beginning_choices() #calling the function of the choices.
def mirage(): #One of the routes of the game.
    #descriping what is happening.
    global total_score #working wit the global score.
    #describing what is happening.
    print_pause("You start walking toward the water pond.")
    print_pause("But with every step, the distance"
                " " "seems to stretch farther away.")
    print_pause("You keep walking... and walking...")
    #asking the player if they want to complete walking.
    #taking choice.
    while True:
        #checking choices.
        keep_walking = input("Do you want to continue walking or return back?"
                             " " "Enter 1 to continue."
                             " " "Enter 2 to return.").strip()
        if keep_walking == "1":
            rare_event_mirage = random.randint(1, 15) #making a rare event.
            if rare_event_mirage == 1:
                print_pause("You heard a strange sound, as you looked"
                            " " "it turned out to be the"
                            " " "floating cactus again..")
                print_pause("'Hi there :D' it said.")
                print_pause("'What are you doing here? As far"
                            " " "as I know, this place is empty.'")
                print_pause("'Do you want a drive to the jeep?"
                            " " "there is a guy there that may help you!'")
                while True:#mking a loop.
                    #taking input.
                    cactus_help = input("'Yes :D?' (Y/N)").strip().lower()
                    if cactus_help in ["y", "yes"]: #checking it.
                        print_pause("It holds you happily and you"
                                    " " "arrive there in a couple of minutes.")
                        print_pause("'Here you go!' it said happily.")
                        print_pause("'Also, here is 20 points! They may help"
                                    " " "you :D' it said before vanishing")
                        total_score += 20 #adding score.
                        print_pause(f"Your total score now is {total_score}.")
                        print_pause("Well, it turned out to be helpful.")
                        jeep() #calling jeep route function.
                        break #breaking the loop.
                    elif cactus_help in ["n", "no"]:
                        print_pause("It pouts and says 'fine! I shouldn't"
                                    " " "have offered you help from the"
                                    " " "beginning!' then it vanishes")
                        print_pause("The pond never gets any closer.")
                        print_pause("It's a mirage.")
                        print_pause("You're more lost than before,"
                                    " " "the heat pressing down"
                                    " " "on you like a weight.")
                        print_pause("Exhausted, dizzy, and drained"
                                    " " "from the endless walk")
                        print_pause("You collapse in the sand.")
                    #adding a new ending.
                        new_ending("Collapsed on the hot sand")
                    #game over function.
                        game_over("collapsed on the hot sand, you don't feel"
                                  " " "your body or hear anything,"
                                  " " "everything is blurry.")
                        break
                    else:
                        print_pause("Invalid input. Please type 'Y'"
                                    " " "for Yes or 'N' for No.")
            else:
                print_pause("The pond never gets any closer.")
                print_pause("It's a mirage.")
                print_pause("You're more lost than before,"
                            " " "the heat pressing down on you like a weight.")
                print_pause("Exhausted, dizzy, and"
                            " " "drained from the endless walk")
                print_pause("You collapse in the sand.")
                new_ending("Collapsed on the hot sand") #adding a new ending.
            #calling the function of losing.
                game_over("collapsed on the hot sand, you don't feel your"
                          " " "body or hear anything, everything is blurry.")
        elif keep_walking == "2":
            total_score -= 5 #decreasing score.
            print_pause("You lost 5 points because you"
                        " " "went this way from the beginning!")
            print_pause(f"Your total score now is {total_score}!")
            print_pause("You returned to the same spot that you waked up in.")
            print_pause("In the distance, you spot two things:")
            print_pause("-A shimmering water pond far to your left.")
            print_pause("-A black jeep, strange and"
                        " " "unmoving, off to the right.")
            print_pause("You have to choose. You can’t just sit"
                        " " "here and wait for the sun to finish you off.")
            beginning_choices() #calling the function of the previous choices.
            break
        else:
            print("inviald input, please enter 1 or 2 only.")
def jeep(): #One of the routes of the game.
    #descriping what is happening.
    global total_score #Working with the global score.
    print_pause("You walk toward the jeep.")
    print_pause("When you reach it, you see a man inspecting the engine.")
    print_pause("It looks like the jeep is broken.")
    #Giving the player choices.
    while True: #making a loop.
        print_pause("Enter 1 to talk to the man")
        print_pause("Enter 2 to go back")
        print_pause("Enter I to check your inventory")
        talk_jeep_man = choice("What will you do?") #taking choice.
    #checking choice, this one has 2 choices, the first one has
    #2 differnt questions based on the player taking the bucket,
    #every question has 2 choices, and the 2nd one has 2 choices.
        if talk_jeep_man == "1":
            print_pause("You approach him and explain that"
                        " " "you're lost and don’t remember how you got here.")
            print_pause("He nods and tells you that he was headed to a nearby"
                        " " "village, but the jeep broke down"
                        " " "in the middle of the road.")
            print_pause("He says it needs water to start"
                        " " "again, but he has nothing to fetch it with.")
            print_pause("“There’s a well nearby,” he says with"
                        " " "a strange dialect, “but no bucket.”")
            print_pause("If you help him, he might"
                        " " "take you with him to the village.")
            #checking if the player got the bucket then give them choices.
            if "bucket" in inventory:
                while True:
                    print_pause("Enter 1 to give him the"
                                " " "empty bucket to fetch water.")
                    print_pause("Enter 2 go back to where you woke up.")
                    print_pause("Enter I to check your inventory.")
                    bucket_use = choice("What will you do?") #taking choice.
            #checking choices.
                    if bucket_use == "1":
                        #removing the bucket from the inventory.
                        inventory.remove("bucket")
                #descriping what is happening.
                        print_pause("You hand him the bucket.")
                        print_pause("He takes it, walks off toward the well.")
                        print_pause("As you wait you hear a strange"
                                    " " "sound, when you looked you"
                                    " " "spot it again.")
                        print_pause("The floating cactus.")
                        print_pause("'Hey there again!:D'"
                                    " " "it said with a grin.")
                        print_pause("'Do you want to play"
                                    " " "another trivia game?'")
                        print_pause("'Just like the last time!"
                                    " " "you earn 5 points"
                                    " " "when you answer correctly and lose"
                                    " " "5 when you answer wrongly!")
                        print_pause("Remember that can easily increase"
                                    " " "your score if you are smart enough!")
                        #trivia
                        cactus_questions("That may be your"
                                         " " "life now.",
                                         "'Till the next time!:D'"
                                         " " "it says before vanishing.")
                        print_pause("The man comes back"
                                    " " "with the bucket filled.")
                        print_pause("After pouring the water into the engine,"
                                    " " "he fiddles with it for a"
                                    " " "while—and the jeep starts.")
                        print_pause("You have earned 10 points"
                                    " " "for choosing right!")
                        total_score += 10 #adding score.
                        print_pause("Your total score now is"
                                    " " f"{total_score} points!")
                        print_pause("'Get in,' he says.")
                        print_pause("You hop into the jeep.")
                        print_pause("The two of you drive through"
                                    " " "the desert in silence.")
                        print_pause("After about an hour, you"
                                    " " "reach the entrance of a village.")
                        print_pause("'Here we are,' he says."
                                    " " "'I’ve got some business"
                                    " " "to take care of. I have"
                                    " " "to go. See you around.'")
                        while True:
                            print_pause("Enter 1 to ask him to"
                                        " " "take you with him.")
                            print_pause("Enter 2 to thank him"
                                        " " "and go explore the village.")
                            #taking choices.
                            man_village = choice("What will you do?")
                #checking choices.
                            if man_village == "1":
                                print_pause("'Sorry,' he replies,"
                                            " " "'it’s part of my work.'"
                                            " " "I can’t take you with me"
                                            " " "… but here.'")
                                print_pause("He hands you a"
                                            " " "strange-looking coin.")
                                print_pause("'You can use this to buy"
                                            " " "yourself something."
                                            " " "You look hungry.'")
                                print_pause("He drives away, leaving"
                                            " " "you at the village gates.")
                                print_pause("You pocket the coin"
                                            " " "and go explore.")
                                #adding the coin to the inventory.
                                inventory.append("coin")
                                print_pause("The coin is added"
                                            " " "to your inventory!")
                                check_inventory_got_something()
                                #calling the function of finding the pet.
                                pet_found()
                                break
                            elif man_village == "2":
                                print_pause("You thank him and decide to"
                                            " " "explore the village on"
                                            " " "your own.")
                                #calling the function of finding the pet.
                                pet_found()
                                break
                            else:
                                print_pause("Invalid input. Please choose"
                                            " " "from '1', '2' or 'I'.")
                    elif bucket_use == "2":
                        print_pause("You walked back to the"
                                    " " "spot that you woke up in")
                        #calling the function of the choices of the beginning.
                        beginning_choices()
                        break
                    else:
                        print_pause("Invalid input. Please"
                                    " " "choose from '1', '2' or 'I'.")
                        #another choices if the player didn't
                        #get the bucket from the beginning.
            if "bucket" not in inventory:
                while True:
                    print_pause("Enter 1 to try to help in another way.")
                    print_pause("Enter 2 to go back to where you woke up.")
                    print_pause("Enter I to check your inventory.")
                    no_bucket_choice = choice("What will you do?")
            #checking choice.
                    if no_bucket_choice == "1":
                        #taking a random voice from the sound list.
                        strange_sound = random.choice(sound)
                        print_pause("You both try everything to fix"
                                    " " "the jeep, but nothing works.")
                        print_pause("You're too hungry to think straight.")
                        #used random sound.
                        print_pause("You hear a strange sound in the distance"
                                    " " f"—{strange_sound} sound.")
                        print_pause("It doesn't look safe to stay here.")
                        print_pause("Night falls.")
                        print_pause("The man crawls into the jeep.")
                        print_pause("He looks exhausted—maybe he"
                                    " " "passed out, maybe worse.")
                        print_pause("You lie on the sand, eyes"
                                    " " "heavy, body aching.")
                        print_pause("Everything fades.")
                        print_pause("The stars blur.")
                        print_pause("You don’t hear anything anymore.")
                        new_ending("You had to get the bucket.")
                        game_over("You collapsed on the sand")
                        break
                    elif no_bucket_choice == "2":
                        beginning_choices()
                        break
                    elif no_bucket_choice == "i":
                        check_inventory()
                        print_pause("Enter 1 to try to help in another way.")
                        print_pause("Enter 2 to go back to where you woke up.")
                        print_pause("Enter I to check your inventory.")
                        print_pause("What will you do?")
                    else:
                        print_pause("Invalid input. Please choose"
                                    " " "from '1', '2' or 'I'.")
        elif talk_jeep_man == "2":
            print_pause("You walked back to the spot that you woke up in")
            beginning_choices() #calling the beginning choices.
            break
        elif talk_jeep_man == "i":
            check_inventory()
            print_pause("Enter 1 to talk to the man")
            print_pause("Enter 2 to go back")
            print_pause("Enter I to check your inventory")
            print_pause("What will you do?")
        else:
            print_pause("Enter 1 to talk to the man")
            print_pause("Enter 2 to go back")
            print_pause("Enter I to check your inventory")
            print_pause("Invalid input. Please choose from '1', '2' or 'I'.")
def pet_found(): #function for the finding pet scenario.
    global pet_name #calling global pet name var.
    #descriping what is happening.
    the_pet = random.choice(pet) #getting a random animal from the pet list.
    #taking a random pet codition from the pet list.
    the_pet_condition = random.choice(pet_condition)
    #Describing what is happening.
    print_pause("As you walk through the dusty streets,"
                " " "you hear footsteps behind you.")
    print_pause("You turn around—it’s"
                " " f"{the_pet} {the_pet_condition}.")
    #giving the player choices.
    print_pause("Enter 1 to adopt it.")
    print_pause("Enter 2 to leave it behind.")
    while True:
        adopt = input("What will you do?").strip().lower() #taking choice
        #checking choice.
        if adopt == "1":
            print_pause("You adopted it!")
            #making the player name the pet.
            pet_name = input("What will you name it?").strip()
            print_pause(f"Now little {pet_name} is"
                        " " "following you like a little shadow.")
            #calling the function of pet's menu.
            pet_view()
            village() #next scene function.
            break #break the loop.
        elif adopt == "2":
            print_pause(f"You leave the {the_pet} behind.")
            print_pause("It watches you walk away.")
            print_pause("It looked… kind of sad.")
            village() #the next scene.
            break
        else:
            print_pause("Invalid input, please enter '1' or '2'.")
def pet_view(): #pet's name and type list.
    global pet_name #calling global pet name.
    #getting random pet status per time
    player_pet_status = random.choice(pet_status)
    #taking choice.
    view_pet = input("Enter P to view your pet's name"
                     " " "and status or press ENTER to skip.").strip().lower()
    #checking choice.
    if view_pet == "p":
        #checking if there is a pet name, because if there
        #is one then the pplayer already have a pet else they don't.
        if pet_name:
            print_pause(f"Your pet name is: {pet_name}, {player_pet_status}")
        elif not pet_name: #if there is no pet name.
            print_pause("You don't have any pets :(")
        else: #else do nothing.
            pass
def village(): #a scene from the game scenes.
    global total_score #calling the global score.
    #describing what is happening.
    print_pause("You walk through the village streets, stomach"
                " " "growling, throat dry — you're desperate for"
                " " "something, anything, to eat or drink.")
    if pet_name: #if there is a string in pet name var.
        #used a random pet condition from the second list.
        print_pause(f"{pet_name} follows behind,"
                    f"{random.choice(pet_condition_2)},"
                    " " "Just when you're about to drop,"
                    "you spot a small shop.")
    else: #another description without the pet.
        print_pause("Just when you're about to drop, you spot a small shop.")
    print_pause("You rush toward it.")
    print_pause("An old woman stands behind the counter.")
    print_pause("'How can I help you?' she asks.")
    if "coin" in inventory: #checking if the player have the coin.
        print_pause("You suddenly remember — you only have one coin.")
        print_pause("No idea what it can get you in this strange place.")
        while True:
            inventory.remove("coin")
            print_pause("Enter 1 to ask for only food or drink.")
            print_pause("Enter 2 to ask for both and hope for the best.")
            buy = choice("What will you do?")
            if buy == "1":
                print_pause("'Will you like some food or drink?' she askes.")
                print_pause("Enter 1 to buy food.")
                print_pause("Enter 2 to buy a drink.")
                food_or_drink = input("What will you choose?").strip().lower()
                while True:
                    if food_or_drink == "1":
                        print_pause("You ask for food.")
                        #used random food from the list.
                        print_pause("The old woman hands you some"
                                    f"{random.choice(food)},"
                                    " " "then gives you a few coins back.")
                        print_pause("Turns out your coin is"
                                    " " "worth more than you thought!")
                        #used a random drink from the list.
                        print_pause("With the change, you"
                                    " " "ask for a drink too," " "
                                    "and she gives you"
                                    " " f"{random.choice(drink)}.")
                        village_eating() #calling another scene of the game.
                        break #breaking the loop.
                    elif food_or_drink == "2":
                        print_pause("You ask for a drink.")
                        #used a random drink from the list.
                        print_pause("She nods and hands you a"
                                    " " f"{random.choice(drink)},"
                                    " " "then gives you some change.")
                        #used a random food from the list.
                        print_pause("With it, you ask for food, and she"
                                    " " f"gives you {random.choice(food)}"
                                    " " "too.")
                        print_pause("What a win.")
                        village_eating() #calling the next scene.
                        break #breaking the loop.
                    else:
                        print_pause("Invail input, enter '1' or '2'.")
            elif buy == "2":
                print_pause("You ask for both food and drink.")
                #used both random food and a random drink from the lists.
                print_pause("The woman surprisingly, hands you"
                            " " f"{random.choice(food)}"
                            " " f"and {random.choice(drink)}.")
                print_pause("Looks like generosity still"
                            " " "exists in this world.")
                print_pause(f"You get 10 points as you had chosen this!")
                total_score += 10 #adding points as the player chose right.
                print_pause(f"Your total score now is {total_score}")
                village_eating() #calling the next scene.
                break #breaking the loop.
            else:
                print_pause("Invaild input, enter '1' or '2'.")
    else: #if the player doesn't have the coin.
        #descriing.
        print_pause("You remember that you don't have any money.")
        print_pause("Too weak to care anymore,"
                    " " "you walk up to the woman anyway.")
        print_pause("“I think I can help you,” she says.")
        print_pause("“But with one condition.”")
        print_pause("“I’ll take 20 points from your score"
                    " " "instead of money. In exchange, I’ll give you"
                    " " "food and a drink.” she says.")
        if total_score >= 20: #checking if score is less than 20 points.
            while True:
                #taking input.
                score_buy_1 = input("Will you agree? (Y/N)").strip().lower()
                if score_buy_1 in ["y", "yes"]:
                    #used both random food and dring from the lists.
                    print_pause("“Here you go,” she says, handing you"
                                " " f"{random.choice(food)} and"
                                " " f"{random.choice(drink)}.")
                    print_pause(f"Your total score is now {total_score}.")
                    village_eating() #calling the next scene.
                    break #break teh loop.
                    #if player disagrees to the deal.
                elif score_buy_1 in ["n", "no"]:
                    print_pause("You leave the shop empty-handed,"
                                " " "everything around you spinning.")
                    print_pause("You’re too weak to go on.")
                    print_pause("The village blurs around you.")
                    print_pause("You can’t hear, can’t think.")
                    print_pause("You collapse.")
                    new_ending("Broke and hungry.")
                    game_over("collapsed from hunger and thirst.")
                    break #break the loop.
                else: #if score is less than 20 points.
                    print_pause("Invaild input, enter 'Y'"
                                " " "for yes or 'N' for no only please.")
        else:
            #describing.
            print_pause("'It seems you don’t have enough points.' she said")
            print_pause("You leave the shop empty-handed,"
                        " " "everything around you spinning.")
            print_pause("You’re too weak to go on.")
            print_pause("The village blurs around you.")
            print_pause("You can’t hear, can’t think.")
            print_pause("You collapse.")
            new_ending("Broke and hungry.") #adding a new ending.
            game_over("collapsed from hunger and thirst.") #losing function.
def village_eating(): #another scene.
    global total_score #working with the global score.
    #describing what is happening.
    print_pause("You sit down behind a nearby wall to eat and drink in peace.")
    if pet_name: #if there is a string in the pet name var.
        print_pause("Your pet sneaks a few crumbs too (of course).")
        pet_view()
    else: #if not nothing happens.
        pass
    print_pause("You're finally starting to feel human again"
                " " "... when suddenly, a familiar voice calls out.")
    print_pause("You look up")
    print_pause("It’s the floating catus... again.")
    print_pause("You don’t know if it's real, dehydration"
                " " "or full-on madness at this point, but you go with it.")
    print_pause("“Want to play another trivia game?"
                " " ":D” it says with a wide grin.")
    cactus_questions("Maybe you just have to get used to it.",
                     "That was sooooo much fun! till the next time :D!")
    #Choosing the ending based on the score.
    if total_score >=95:  #the highest score.
        best_end()
    elif 95 > total_score >= 40: #a good score.
        mid_end()
    else: #the worst score (anything less than 50)
        bad_end()
#the best ending (95 points or more),
#it lets the player know the character's backstory.
def best_end():
    #describing. player can get it only if thy got the rare event.
    print_pause("After finishing your meal,"
                " " "you stood up and walked back through"
                " " "the village streets.")
    print_pause("The sun beat down, and your"
                " " "steps felt heavy—until you suddenly"
                " " "heard someone call your name.")
    print_pause("You turned around,"
                " " "half-expecting that weird floating cactus again—but no.")
    print_pause("This time, it was someone else.")
    print_pause("“Finally! There you are! We were"
                " " "all so worried,” he said, breathless.")
    print_pause("“I met someone who told me"
                " " "about a lost traveler who didn’t"
                " " "remember anything… I knew it had to be you.”")
    print_pause("You stare at him.")
    print_pause("There’s something familiar about his face.")
    print_pause("“You look exhausted."
                " " "Mom and Dad are worried sick. Let’s get you home.”")
    print_pause("You hesitate.")
    print_pause("He notices.")
    print_pause("“…You don’t remember me?” He pauses,"
                " " "then gently adds, “Do you remember the bucket?"
                " " "Dad told you to fill it and you never came back."
                " " "We were camping in the desert—me, you,"
                " " "Mom, Dad, and our little sister?”")
    print_pause("That hit something.")
    print_pause("Memories rush back, hazy at first… then clearer.")
    print_pause("You remember.")
    print_pause("You remember everything.")
    if pet_name: #if the player has a pet.
        #chose a random condition from the 2nd list for the pet.
        print_pause(f"You glance down at your side, you see {pet_name},"
                    " " f"it is {random.choice(pet_condition_2)}.")
        print_pause("No way you are leaving without"
                    " " "it, so you take it with you")
        print_pause("you, hop into your brother’s car,"
                    " " "and begin the long, warm drive home.")
        print_pause("You’re safe.")
        print_pause("You’re home again.")
        new_ending("Finally Home") #adding a new ending.
        play_again() #retraying function.
    else: #if doesn't have a pet.
        print_pause("you, hop into your brother’s car,"
                    " " "and begin the long, warm drive home.")
        print_pause("You’re safe.")
        print_pause("You’re home again.")
        new_ending("Finally Home") #adding a new ending.
        play_again() #retraying function.
        #a good ending, the normal one
        #(less than 95 points and more than 50 points),
        #it gives the player's chracter a new good life,
        #not fully knowing the backstory of the character.
def mid_end():
    #describing.
    print_pause("After finishing your food, you started wandering again.")
    print_pause("Just as the streets began to blur together,"
                " " "a familiar voice called out.")
    print_pause("It was the same guy from the jeep who helped you earlier.")
    print_pause("“Hey! Still wandering, huh? I’ve been looking for you."
                " " "There’s a small shop nearby looking for help—they’ll"
                " " "give you a room and two meals a day. First person"
                " " "I thought of was you. So... you in?”")
    time.sleep(3) #for drama.
    print_pause("You agreed, unsure of what else life had to offer.")
    print_pause("After a week..")
    time.sleep(5) #for transition effect.
    if pet_name: #if the player has a pet.
        print_pause(f"You and {pet_name} now work in the cozy little shop.")
        print_pause(f"it is {random.choice(pet_status)}.") #random pet status.
        print_pause("You’ve built a new rhythm, a quiet joy.")
        print_pause("The past is still foggy, but atleast have got some peace")
        print_pause("The End.")
        new_ending("New Life.") #adding a nw ending.
        play_again() #retraying function.
        #The worst ending (score less than 50),
        #the player's character is alive but not knowing
        #there backstory and they are lonley.
def bad_end():
    global total_score #calling global score var.
    #describing.
    print_pause("A little more energy returns to you after eating.")
    print_pause("Just as you're about to decide where to go next…")
    print_pause("you hear that voice again.")
    print_pause("“Hey there! Still lost? :D”")
    print_pause("You look up. Yep. It’s the same floating cactus"
                " " "with a face, hovering and grinning.")
    if pet_name: #if player has a pet.
        print_pause("“Soooo here’s the thing—you’ve got, like,"
                    " " "zero money, no family around,"
                    " " "no idea where you are… OH!"
                    " " f"But you do have {pet_name}! Cute little thing!”")
        print_pause("You tense up.")
        print_pause("“Here’s the deal,” it continues.")
        print_pause("“I know a nearby shop that needs a worker."
                    " " "You get a room and one meal a day!"
                    " " "Pretty sweet, right? Buuuuuut—”")
        print_pause("It pauses dramatically.")
        print_pause(f"“—I get to keep {pet_name}."
                    " " "I’m already attached. You understand.”")
        print_pause("What will you d-")
        time.sleep(5) #for drama.
        print_pause("“Oh, never mind! You don’t get to choose this time."
                    " " "You always choose. It’s my turn now :)”")
        print_pause("There's a blinding flash.")
        print_pause("When it clears, you’re inside a small shop.")
        print_pause(f"Alone. No {pet_name} in sight.")
        print_pause("A week passes.")
        print_pause("You work every day.")
        print_pause("You eat.")
        print_pause("You sleep.")
        print_pause("You're alive…")
        new_ending("Alive.")
        print_pause("The End.") #adding a new ending.
        play_again() #retraying function.
    else: #if the player doesn't have a pet.
        print_pause("“Soooo here’s the thing—you’ve got, like,"
                    " " "zero money, no family around,"
                    " " "no idea where you are… OH!"
                    " " "But you do have some score,"
                    " " f"around {total_score}, right?")
        print_pause("You tense up.")
        print_pause("it grins “Here’s the deal,” it continues.")
        print_pause("“I know a nearby shop that needs a worker."
                    " " "You get a room and one meal a day!"
                    " " "Pretty sweet, right? Buuuuuut—”")
        print_pause("It pauses dramatically.")
        print_pause("“—I get to keep all your points,"
                    " " "you know, mutual benefit”")
        print_pause("What will you d-")
        time.sleep(5) #for dramatic effect.
        print_pause("“Oh, never mind! You don’t get to choose this time."
                    " " "You always choose. It’s my turn now :)”")
        print_pause("There's a blinding flash.")
        print_pause("When it clears, you’re inside a small shop.")
        print_pause("Alone.")
        print_pause("A week passes.")
        print_pause("You work every day.")
        print_pause("You eat.")
        print_pause("You sleep.")
        print_pause("You're alive…")
        new_ending("Alive.") #adding a new ending.
        print_pause("The End.")
        play_again() #calling retrying function.
if __name__ == "__main__":
    beginning()