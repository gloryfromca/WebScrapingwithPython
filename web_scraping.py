import nltk
from  nltk import sent_tokenize,word_tokenize,Text,pos_tag
# from nltk.book import  *

sample1="Strange women lying in ponds distributing swords is no\
basis for a system of government. Supreme executive power derives from a mandate\
from the masses, not from some farcical aquatic ceremony."
sample2="The dust was thick so he had to dust"
sample3="Google is one of the best companies in the world.\
I constantly google myself to see what I'm up to."
nouns=['NN', 'NNS', 'NNP', 'NNPS']

sentences=sent_tokenize(sample3)
for sentence in sentences:
    if "google" in sentence.lower():
        taggedwords=pos_tag(word_tokenize(sentence))
        for  word in taggedwords:
            if word[0].lower()=="google" and word[1] in nouns:
                print(sentence)





