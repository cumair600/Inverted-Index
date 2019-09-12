import pickle
import sys
import os
from nltk.stem import PorterStemmer

# Load Inverted Index and Term Info pickles

with open('Inverted-Index.pickle', 'rb') as handle:
    a = pickle.load(handle)
    
with open('Term-Info.pickle', 'rb') as handle:
    b = pickle.load(handle)

# Take argument from cmd line

argv = sys.argv
method = argv[1]
term = argv[2]
s = term

ps = PorterStemmer()

term = ps.stem(term)
term = term.replace("'", "")

# Answer Query

if method == "--term":
    print("Listing for term : " + str(s))
    print("TERM-ID : " + str(b[term][0]))
    print("Number of documents containing term : " + str(b[term][2]))
    print("Term frequency in corpus : " + str(b[term][1]))
else:
    print("Error : Invalid Method!")
  