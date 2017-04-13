from nltk.stem import SnowballStemmer 
from nltk.corpus import wordnet as wn
import re
import sys

stemmer = SnowballStemmer("english")
regx = re.compile("[^a-zA-Z]")

def ScanLine(line, wordset):
    
    strings = regx.split(line)
    for str in strings:
        size = len(str)
        if size <= 2:  
            continue
        else:
            str = stemmer.stem(str)
            wordset[str] = 1

def ComputerOverlap(signature, context):
    overlap = 0
    for word, val in signature.items():
        v = context.get(word, 0)
        if v != 0:
            overlap = overlap + 1
    return overlap
    
def GetWordSense(word, sentense):
    
    context = {}
    ScanLine(sentense, context)
    
    senses = wn.synsets(word, wn.NOUN)
    if len(senses) > 0:
        max_overlap = -1     
        result = ''
        
        for s in senses:
            info = s.definition()
            for example in s.examples():
                info = info + ' ' + example
            
            
            signature = {}
              
            ScanLine(info, signature)
            overlap = ComputerOverlap(signature, context)
            if overlap > max_overlap:
                max_overlap = overlap 
                result = s.definition();
        
        print ('Result is: ' + result)
    else:
        print (word + " is not NOUN!")


if len(sys.argv) != 3:
    print ("Usage: python lesk.py word sentence")
    sys.exit(0)

GetWordSense(sys.argv[1], sys.argv[2])
