import random
import os

def get_word():
    words = []
    with open("./ahorcado/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line)
    return random.choice(words)

def coincidence2(word,letter):
    word_list = list(word)
    new_list = ["_" if word_list[i] != letter else letter.upper() for i in range(0,len(word_list)-1)]
    return new_list

def run():
    title = """

            $$ |                                                                                                                        
            $$$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$$$$$$\         $$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\  
            $$  __$$\  \____$$\ $$  __$$\ $$  __$$\ $$  _$$  _$$\  \____$$\ $$  __$$\       $$  __$$\  \____$$\ $$  _$$  _$$\ $$  __$$\ 
            $$ |  $$ | $$$$$$$ |$$ |  $$ |$$ /  $$ |$$ / $$ / $$ | $$$$$$$ |$$ |  $$ |      $$ /  $$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |
            $$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |      $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|
            $$ |  $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$ |$$ |  $$ |      \$$$$$$$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\ 
            \__|  \__| \_______|\__|  \__| \____$$ |\__| \__| \__| \_______|\__|  \__|       \____$$ | \_______|\__| \__| \__| \_______|
                                        $$\   $$ |                                        $$\   $$ |                                  
                                        \$$$$$$  |                                        \$$$$$$  |                                  
                                        \______/                                          \______/
            """
    print( title)
    #Print part of screen where shows letters that are incomplete
    word = get_word()
    word_list = list(word)
    letter = input("Type a letter: ")
    new_list = coincidence2(word, letter)
    os.system ("clear")
    while "_" in new_list:
        print(*new_list, sep=' ')
        letter = input("Type a letter: ")
        os.system ("clear")
        for i in range(0,len(new_list)):
            if new_list[i] == "_":
                if letter == word_list[i]:
                    new_list[i] = letter.upper()
    print("Congratulations!! :)")
    print(*new_list, sep=' ')

if __name__=='__main__':
    run()
