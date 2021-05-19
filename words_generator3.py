import os
import shutil

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(THIS_FOLDER, 'Prus2.txt')

LENGHT_OF_WORD = 4
LENGTH_OF_LIST = 485

def process(texts, folder):
    words = {}
    for name,num in texts:
        file = os.path.join(folder, name)
        f = open(file, 'r')
        for line in f:
            curr_string = ""
            for char in line:                    
                curr_string += char
                if len(curr_string) == LENGHT_OF_WORD:
                    if curr_string not in words:
                        words[curr_string] = (0,0,0)
                    words[curr_string] = (words[curr_string][0] + (0 == num), words[curr_string][1] + (1 == num), words[curr_string][2] + (2 == num))
                    curr_string = ""
    return words

def create_lists(texts, words):
    common_word = [[] for i in range(len(texts))]

    sorted_words = []

    for word in words:
        sum_of_occurence = words[word][0] + words[word][1] + words[word][2]
        sorted_words.append((word, sum_of_occurence))

    sorted_words = sorted(sorted_words, key = lambda sorted_words: sorted_words[1], reverse=True)

    one_before = False
    for word,num in sorted_words:
        if num == 1:
            one_before = True
        if num > 1 and one_before:
            raise("Sorting went wrong!")

    print("common_word: ", common_word)
   
    for word, occur in sorted_words:
        sum_of_occurence = words[word][0] + words[word][1] + words[word][2]
        for num in range(0,len(texts)):
            occurences = sum_of_occurence - words[word][num]
            if words[word][num] >= 3 * occurences and len(common_word[num]) < LENGTH_OF_LIST:
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
    file = os.path.join(THIS_FOLDER,"sol3.txt")
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

    f = open(os.path.join(THIS_FOLDER,'solution3.py'), 'w')
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
       
    num = 0
    texts = []
    for name in texts_names:
        texts.append((name,num))
        num += 1
        
    print("texts: ", texts)

    words = process(texts, folder)

    common_words = create_lists(texts, words)

    try:
        shutil.rmtree(os.path.join(THIS_FOLDER,"lista_slow"))
        print("dir removed")
    except:
        print("dir cannot be removed")

    create_files(texts, common_words)
    create_solution(texts)

main()