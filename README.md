# Text-Summerization
In Extractive Summarization, we are identifying important phrases or sentences from the original text and extract only these phrases from the text. These extracted sentences would be the summary.

This process can be divided into two steps: Pre-Processing step and
Processing step. 
Pre-Processing is structured representation of the original text. It usually includes:

a)	Sentences boundary identification. In English, sentence boundary is identified with presence of dot at the end of sentence. 

b)	Stop-Word Elimination—Common words with no semantics. 

c)	Stemming—The purpose of stemming is to obtain the stem or radix of each word, which emphasize its semantics.

In Processing step, features influencing the relevance of sentences are decided and calculated and then weights are assigned to these features using weight learning method. Final score of each sentence is determined using Feature-weight equation. Top ranked sentences are selected for final summary.

# Libraries Required
Front-end – Tkinter Library.

Summarization - NLTK, SPACY, SUMY, GENSIM.



