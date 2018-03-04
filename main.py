from filereader import *
import time

filereader = FileReader()
start = time.time()
print("Reading scripts...")
filereader.read()
end = time.time()
for word in filereader.words_list:
    print(word)

print("\n\n### TOTAL LOADING TIME:", end - start, "\n")
