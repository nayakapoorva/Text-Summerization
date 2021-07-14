import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import en_core_web_sm

nlp = spacy.load('en_core_web_sm')

def summarizer_text(raw_doc):
    raw_text = raw_doc
    doc = nlp(raw_text)
    stopwords = list(STOP_WORDS)
    word_frequencies={}
    for word in doc:
        if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text]=1
            else:
                word_frequencies[word.text] +=1

    max_freq = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/max_freq)

    sentence_text = [sentence for sentence in doc.sents]

    sentence_score = { }
    for sent in sentence_text:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' '))<30:
                    if sent not in sentence_score.keys():
                        sentence_score[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_score[sent] += word_frequencies[word.text.lower()]
    summarizes_text = nlargest(7,sentence_score,key=sentence_score.get)
    final_text = [w.text for w in summarizes_text]
    summary = ' '.join(final_text)
    return summary
