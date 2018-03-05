import nltk
from operator import itemgetter

class FileReader:
    
    stop_words=[]
    words_list=[]

    def __init__(self):
        stop_words = self.read_stopwords()



    def read(self):
        for i in range(1, 15):
            file = open("episodes/%d.txt"%i,"r")
            # print(" ### FILE", i)     
            self.read_a_file(file)               
        self.words_list.sort(key=itemgetter(1), reverse=True)

    def read_a_file(self, file):
        stemmer = nltk.PorterStemmer()        
        
        for line in file:
            for word in line.split():

                # lower case the word
                word = word.lower()

                # remove punctuation
                word = self.remove_punc(word)

                # normalize word
                word = stemmer.stem(word)

                # check if it's not a stop word
                temp_words_list = [obj[0] for obj in self.words_list]
                if word not in temp_words_list:
                    if word not in self.stop_words:
                        tml=[word,1]
                        self.words_list.append(tml)            
                else:
                    x = [x for x in self.words_list if word in x][0]
                    x[1] += 1



    def read_stopwords(self):
        file = open("stopwords.txt","r")     
        for line in file:
            line=line.replace("\n","")
            self.stop_words.append(line)


    def remove_punc(self, word):
        if ',' in word:
            word = word.replace(',','')
        if '.' in word:
            word = word.replace('.','')
        if '[' in word:
            word = word.replace('[','')
        if ']' in word:
            word = word.replace(']','')
        if '(' in word:
            word = word.replace('(','')
        if ')' in word:
            word = word.replace(')','')
        if '?' in word:
            word = word.replace('?','')
        if '!' in word:
            word = word.replace('!','')
        if ':' in word:
            word = word.replace(':','')
        if '-' in word:
            word = word.replace('-','')
        if '\"' in word:
            word = word.replace('\"','')
        if '\'' in word:
            word = word.replace('\'','')

        if "$" in word:
            word = ""
        if "https" in word:
            word = ""
        if "13" in word:
            word = ""
        if len(word)==0:
            word=""
        return word