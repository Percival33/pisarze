# Writers (Pisarze)

Scripts used to generate solution to task [Writers](https://szkopul.edu.pl/problemset/problem/v2Y2_UW56ENMcbwP22tkTb7a/site/?key=statement) from **XXVII Polish Olympiad in Informatics**.

## Task
There are three masterpieces of Polish literature:
* “Pan Tadeusz” by Adam Mickiewicz,
* “Quo Vadis” by Henryk Sienkiewicz,
* “The Doll” by Bolesław Prus.

Implement program which can answer whose quote is given, from three aforementioned books.

### Additional informations
There are $T$ testcases, each containing excerpt from one of the three aforementioned books. The excerpt is stripped of Polish diacritics, contains between $10$ and $2000$ words, and both begins and ends with a complete word (or punctuation mark)

### Limits
* code size limit is $10kB$.

## Strategy & attempts :smile:

1. Save lists of unique words of length $4$ - Score $43$

    * [solution.cpp](https://github.com/Percival33/pisarze/blob/main/solution.cpp)
    * [words_generator.py](https://github.com/Percival33/pisarze/blob/main/words_generator.py)

2. Save lists of words of length $4$ which occur in one text more than $70%$ of all occurences - Score $28$
    * [words_generator2.py](https://github.com/Percival33/pisarze/blob/main/words_generator2.py)

3. Save lists of unique strings of length $4$ - Score $73$
    * [words_generator3.py](https://github.com/Percival33/pisarze/blob/main/words_generator3.py)
    * [solution3.py](https://github.com/Percival33/pisarze/blob/main/solution3.py)

