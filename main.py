import nltk

from modules.info_extraction import getNamedEntity,getphrase
from modules.determine_answer_type import determineAnswerType
from modules.get_vectors import getQueryVector

##-----Main----
isActive = True
while isActive:
    text = input('Enter your query: ')
    quest = determineAnswerType(text)
    print ("---question classified: ",quest)
    # print ("1. getNamedEntity:  ",getNamedEntity(text))
    # print ("2. getphrase: ",getphrase(text))
    # ques = (nltk.word_tokenize(text))
    # qvect = getQueryVector(ques)
    # print ("3. question vect ",qvect)
    # query1 = input('do you wanna exit? yes/no:   ')
    # if query1 == "yes":
    #     isActive = False