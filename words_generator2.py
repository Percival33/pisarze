import os
import shutil

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(THIS_FOLDER, 'Prus2.txt')

LENGHT_OF_WORD = 4

char_to_remove = {'.', '?', '!', ',', ';',':','"',')','(','*','\''}
                   
# print("Slowo: ", curr_string, " wypisuje", words[curr_string])

def process(texts, folder):
    words = {}
    for name,num in texts:
        file = os.path.join(folder, name)
        f = open(file, 'r')
        for line in f:
            # print("linia: ", line)
            curr_string = ""
            for char in line:
                if char == ' ':
                    # print("slowo: ", curr_string, end ="\n\n")
                    # old_string = curr_string
                    for c in char_to_remove:
                        curr_string = curr_string.replace(c,'')

                    # print("s: ", old_string)
                    # print("n: ", curr_string)
                    # print(end="\n\n")
                    if len(curr_string) == LENGHT_OF_WORD:
                        if curr_string not in words:
                            words[curr_string] = (0,0,0)
                        words[curr_string] = (words[curr_string][0] + (0 == num), words[curr_string][1] + (1 == num), words[curr_string][2] + (2 == num))
                    curr_string = ""
                else:                        
                    curr_string += char.lower()
    return words

def create_lists(texts, words):
    common_word = [[] for i in range(len(texts))]
    # for i in range(len(texts)):
    #     common_word.append([])

    print("common_word: ", common_word)
   
    for word in words:
        sum_of_occurence = words[word][0] + words[word][1] + words[word][2]
        # if word == "moja":
        #     print("moja w M: ", words[word][0], " P: ", words[word][1], " S: ", words[word][2])
        for num in range(0,3):
            if words[word][num] >= 0.7 * sum_of_occurence:
                common_word[num].append(word)

    return common_word
               
def create_files(texts, list_of_words):
    folder = os.path.join(THIS_FOLDER, "lista_slow")
    os.mkdir(folder)

    for file, num in texts:
        file_name = os.path.join(folder, file[0]+".txt")

        print("nazwa pliku: ", file_name)

        with open(file_name, 'w') as f:
            f.write(file[0]+'={')
            
            for word in list_of_words[num]:
                f.write('\'')
                f.write(word)
                f.write('\'')
                if word != list_of_words[num][-1]:
                    f.write(',')
            f.write('}')

def create_solution(texts):
    file = os.path.join(THIS_FOLDER,"sol.txt")
    print("79: ", file)
    f = open(file,'r')
    lines = f.readlines()
    f.close()
    
    print("linie sol: ", len(lines))
       
    try:
        os.remove(os.path.join(THIS_FOLDER,'solution.py'))
    except:
        print("solution.py not exists")

    folder_with_lines = os.path.join(THIS_FOLDER,'lista_slow')

    list_of_words = [[] for i in range(len(texts))]

    for text,num in texts:
        a = open(os.path.join(folder_with_lines, text[0] + '.txt'))
        # print(text[0]+'.txt')
        list_of_words[num] = a.readlines()
        a.close()

    f = open(os.path.join(THIS_FOLDER,'solution.py'), 'w')
    for num in range(len(list_of_words)):
        for i in list_of_words[num]:
            f.write(i)
        f.write('\n')

    for i in lines:
        f.write(i)
    
    f.close()

def main():
    folder = os.path.join(THIS_FOLDER, "teksty")
    texts_names = os.listdir(folder)
    
    # texts_names = ['Mickiewicz2']
    
    num = 0
    texts = []
    for name in texts_names:
        texts.append((name,num))
        num += 1
        
    print("texts: ", texts)

    words = process(texts, folder)

    # print("pliki w folderze", os.listdir(teksty))

    common_words = create_lists(texts, words)

    try:
        shutil.rmtree(os.path.join(THIS_FOLDER,"lista_slow"))
        print("dir removed")
    except:
        print("dir cannot be removed")

    create_files(texts, common_words)
    create_solution(texts)

main()