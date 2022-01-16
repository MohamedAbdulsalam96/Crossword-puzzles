import random

Words_list = [
    {"word": "Yemen", "question": "Arabic Country?"},
    {"word": "easy", "question": "simple think?"},
    {"word": "Frog", "question": " Animal live in the sea?"},
    {"word": "Ring", "question": "something worn by hand?"},
    {"word": "YearZ", "question": "12 months ?"},
    {"word": "CPU", "question": "Brain of computer is?"},
    {"word": "Camel", "question": "Which animal has hump on its back?"},
    {"word": "Jasmine", "question": "flower is white in colour?"},
    {"word": "Oval", "question": "Shape of Egg is?"},
    {"word": "Winter", "question": " In which season we wear warm clothes?"},
    {"word": "Seven", "question": "colors are there in a rainbow?"},
    {"word": "Red", "question": "primary color?"},
    {"word": "Sun", "question": "principal source of energy for earth?"},
    {"word": "Africa", "question": "continent is known as ‘Dark’ continent?"},
    {"word": "Asia", "question": "the largest continent in the world?"},
    {"word": "Bahrain", "question": "A gulf country that starts with \'b\'"},
    {"word": "Brazil", "question": "A country that hosted World Cup in 2014"},
    {"word": "Cheap", "question": "Opposite of expensive"},
    {"word": "Ready", "question": "A word describing a state"},
    {"word": "Nivada", "question": "The state where Las Vegas is located"},
    {"word": "House", "question": "Where you live"},
    {"word": "Bus", "question": "A form of public transportation"},
    {"word": "Canada", "question": "A country in South America that starts with the letter \'C\'"},
    {"word": "Need", "question": "A word similar to require"},
    {"word": "Die", "question": "The opposite of \'live\'"},
    {"word": "Friday", "question": "the last day from week?"},
    {"word": "seven", "question": "number of days in week"},
    {"word": "france", "question": "where is effil tower"},
    {"word": "sanaa", "question": "the capital of yemen"},
    {"word": "Cairo", "question": "the capital of Egypt"},
    {"word": "iraq", "question": "Baghdad is a capital of"},
    {"word": "cars", "question": "a taxi is a type of?"},
    {"word": "Egypt", "question": " where is The Nile River'"},
    {"word": "Yemen", "question": "where is Socotra Island"},
    {"word": "Amina", "question": " mother of our massenger"},
    {"word": "Tokyo", "question": "Asia's largest city"},
    {"word": "Australia", "question": "The largest island in the world"},
    {"word": "Washington", "question": "What is the capital of America"},
    {"word": "Nile", "question": "The longest river in the world"},
    {"word": "Whale", "question": "The heaviest animal on earth"},
    {"word": "Jupiter", "question": "The largest planet in the solar system"},
    {"word": "Algorithm", "question": "Founder of Algebra"},
    {"word": "Asia", "question": "Largest continents"},
    {"word": "Ostrich", "question": "The fastest bird in the world"},
    {"word": "London", "question": "The city is located the famous Big Ben Watch"},
    {"word": "songs", "question": "which You listen everyday?"},
    {"word": "lion", "question": "who is the king of the jungle?"},
    {"word": "Om Klthom", "question": "The Lady of Arabic Singing?"},
    {"word": "Oval", "question": "Shape of Egg is?"},
    {"word": "aluto", "question": " It is one of the planets of the solar system?"},
    {"word": "china", "question": "From Southeast Asian countries?"},
    {"word": "purple", "question": "it is mean I trust You?"},
    {"word": "Sun", "question": "the biggest start in our galaxy?"},
    {"word": "Roma", "question": "one of Italia country?"},
    {"word": "sponge pop", "question": "Who lives in the sea and people are loved it ?"},
    {"word": "Sky", "question": "something is starting with s \'b\'"},
    {"word": "Sedney", "question": "A capital city of Australia"},
    {"word": "Popup", "question": "Alert message"},
    {"word": "FTP", "question": "standard for File Transfer Protocol"},
    {"word": "Taxes", "question": "The position of Dallas"},
    {"word": "Islam", "question": "What your religion"},
    {"word": "Team", "question": "meaning of co-workers"},
    {"word": "Koyoto", "question": "The name of Japan anime city \'C\'"},
    {"word": "Vaccine", "question": "Synonym of medicine"},
    {"word": "Dark", "question": "The opposite of \'light\'"},
    {"word": "lago", "question": " What is the name of the main antagonist in the Shakespeare play Othello "},
    {"word": "four", "question": "How many human players are there on each side in a polo match ?"},
    {"word": "feb", "question": " Which month of the year has the least number of days"},
    {"word": "sty", "question": " Where does a pig live?"},
    {"word": "Znose", "question": " We smell with our?"},
    {"word": "tibet", "question": " Which place is known as the roof of the world?"},
    {"word": "tin", "question": " What element is denoted by the chemical symbol Sn in the periodic table?"},
    {"word": "krone", "question": " What is the currency of Denmark?"},
    {"word": "knee", "question": " In which part of your body would you find the cruciate ligament?"},
    {"word": "east", "question": " In which direction does the sun rise ?"},
    {"word": "left", "question": "Which way is anti-clockwise, left or righ?"},
    {"word": "lgloo", "question": " What do you call a house made of ice?"},
    {"word": "nile", "question": " Which is the longest river on the earth?"},
    {"word": "Japan", "question": "Which country is called the land of rising sun?"},
    {"word": "mars", "question": " Which planet is known as the Red Planet?"},
    {"word": "skin", "question": " Which is the most sensitive organ in our body?"},
    {"word": "India", "question": " The largest ‘Democracy’ in the world?"},
    {"word": "water", "question": "What makes up (approx.) 80% of our brain’s volume?"},
    {"word": "Ghana", "question": " Which African nation is famous for chocolate?"},
    {"word": "red", "question": "What is the top color in a rainbow?"},
    {"word": "eAlolo", "question": "What is the top color in a rainbow?"}
]

Words_Chose = []
PuzzleList = [["-" for a in range(0, 6)] for b in range(0, 6)]


def printPuzzle():
    for i in range(0, 6):
        print(*PuzzleList[i])


index_dic = 0
word_dic = ""

####################################
def word_From_dic():
    global word_dic, index_dic
    if index_dic == len(Words_list):
        word_dic = "#######"
        index_dic = 0
        return False
    word_dic = Words_list[index_dic]["word"]
    while len(word_dic) < 6:
        word_dic = word_dic + "#"
    index_dic += 1

chick_pop = False
####################################
def pop_dic():
    global index_dic
    global chick_pop
    if chick_pop:
        Words_Chose.append(Words_list[index_dic - 1])
        Words_list.pop(index_dic - 1)
        index_dic = 0
        chick_pop = False
####################################

def InputPuzzle():
    global word_dic
    global index_dic
    global chick_pop
    for row in range(0, 2):
        word_From_dic()
        for clo in range(0, len(word_dic)):
            if row == 0:
                PuzzleList[row][clo] = word_dic[clo]
                chick_pop = True
            elif row == 1:
                while PuzzleList[row - 1][0] != word_dic[0] or word_dic == "#######":
                    word_From_dic()
                PuzzleList[clo][0] = word_dic[clo]
                chick_pop = True

        pop_dic()

    for row in range(1, 6):
        for clo in range(1, 6):
            if row == 1:
                while PuzzleList[row][0] != word_dic[0] or word_dic == "#":
                    word_From_dic()
                    # print(PuzzleList[row][0] +" <>" + word_dic)
                PuzzleList[row][clo] = word_dic[clo]
                chick_pop = True
            elif row == 2:
                while PuzzleList[row][0] != word_dic[0] or word_dic == "#":
                    word_From_dic()
                    # print(PuzzleList[row][0] +" <>" + word_dic)
                PuzzleList[row][clo] = word_dic[clo]
                chick_pop = True
            elif row == 3:
                while PuzzleList[row][0] != word_dic[0] or word_dic == "#":
                    word_From_dic()
                    # print(PuzzleList[row][0] +" <>" + word_dic)
                PuzzleList[row][clo] = word_dic[clo]
                chick_pop = True
            elif row == 4:
                while PuzzleList[row][0] != word_dic[0] or word_dic == "#":
                    word_From_dic()
                PuzzleList[row][clo] = word_dic[clo]
                chick_pop = True
        pop_dic()

    # for row in range(2, 3):
    #     for clo in range(1, len(word_dic)):
    #         if row == 2:
    #             while PuzzleList[row][0] != word_dic[0]:
    #                 word_From_dic()
    #                 # print(PuzzleList[row][0] +" <>" + word_dic)
    #             PuzzleList[row][clo] = word_dic[clo]
    #     pop_dic()
    #     # print(Words_list[0])


InputPuzzle()
printPuzzle()
print(Words_Chose)
# InputPuzzle()
# printPuzzle()


