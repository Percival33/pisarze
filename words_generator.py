import os
import shutil

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(THIS_FOLDER, 'Prus2.txt')

LENGHT_OF_WORD = 4

char_to_remove = [' ', '.', '?', '!', ',', ';',':','"',')','(','*']

def print_list(list_name):
    print(len(list_name))
    # for word in list_name:
    #     print(word)

def process(name):
    file = os.path.join(THIS_FOLDER, name)
    words = set()

    f = open(file, 'r')
    
    for line in f:
        curr_string = ""
        for char in line:
            if char in char_to_remove:
                if len(curr_string) == MINIMAL_LENGHT_OF_WORD:
                    words.add(curr_string.lower())
                curr_string = ""
            else:
                curr_string += char
    
    return words

def unique(setA, setB):
    if len(setA) > len(setB):
        setA, setB = setB, setA
    
    # print("przed: ", len(setA)," <> ", len(setB))

    # num_of_common_words = 0

    words_to_remove = []
        
    for word in setA:
        if word in setB:
            # num_of_common_words += 1
            words_to_remove.append(word)

    for word in words_to_remove:
        setA.remove(word)
        setB.remove(word)

    # print("po: num=", num_of_common_words," ",len(setA)," <> ", len(setB))

def create_file(dir_name, name, sett):
    file_name = os.path.join(dir_name, name+".txt")
    with open(file_name, 'w') as f:
        # f.write(name)
        f.write(name+'={')
        
        for word in sett:
            f.write('"'+word+'",')
        f.write('}')
        return

def main():
    # name = 'Prus.txt'
    prus = process('Prus.txt') 
    mickiewicz = process('Mickiewicz.txt')
    sienkiewicz = process('Sienkiewicz.txt')

    unique(prus,mickiewicz)
    unique(prus,sienkiewicz)
    unique(mickiewicz,sienkiewicz)

    # print(prus)

    dir_name = os.path.join(THIS_FOLDER, "unique_words")
    
    shutil.rmtree(dir_name)
    os.mkdir(dir_name)
    # print(dir_name)
    create_file(dir_name,"prus_lista", prus)
    create_file(dir_name,"mickiewicz_lista", mickiewicz)
    create_file(dir_name,"sienkiewicz_lista", sienkiewicz)

main()
