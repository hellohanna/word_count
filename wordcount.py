import sys

file_input = sys.argv

def counting_word(file_name):
    file_log = open(file_name)
    word_count={}
    for line in file_log:
        list_words = line.split()
        for word in list_words:
            word = word.lower()
            if word[len(word)-1] in [',', '.', '!', '?', '...', ':', ';']:
                word = word[0:len(word)-1]
            word_count[word]= word_count.get(word,0) + 1


    for word in word_count:
        print(word, word_count[word])
    


counting_word(file_input[1])



