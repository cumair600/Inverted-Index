import pickle
import sys
import os

# Load Inverted Index and Term Info pickles

with open('Inverted-Index.pickle', 'rb') as handle:
    a = pickle.load(handle)
    
with open('Term-Info.pickle', 'rb') as handle:
    b = pickle.load(handle)

# Take argument from cmd line

argv = sys.argv
method = argv[1]
term = argv[2]

# Answer Query

if method == "--term":
    print("Listing for term : " + str(term))
    print("TERM-ID : " + str(b[term][0]))
    print("Number of documents containing term : " + str(b[term][2]))
    print("Term frequency in corpus : " + str(b[term][1]))
else:
    print("Error : Invalid Method!")
  