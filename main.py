from filereader import *
import time

filereader = FileReader()
start = time.time()
print("Reading scripts...")
filereader.read()
end = time.time()

words_file = open('answer.txt', 'w')
for word in filereader.words_list:
    print(word)
    words_file.write("%s\n" % word)

print("\n\n### TOTAL LOADING TIME:", end - start, "\n")
