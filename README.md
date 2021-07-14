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

https://github.com/nayakapoorva/Text-Summerization/blob/main/Text.jfif

# Design

<p align="center">
  <img src="https://github.com/nayakapoorva/Text-Summerization/blob/main/Text.jfif" width="500" height="500" title="hover text">
</p>

# Conclusion
Automated summarization is an important area in NLP (Natural Language Processing). It consists of automatically creating a summary of one or more texts. The purpose of extractive document summarization is to automatically select a number of indicative sentences, passages, or paragraphs from the original document. Most summarization techniques are based on extractive methods. Abstractive method is similar to summaries made by humans.




