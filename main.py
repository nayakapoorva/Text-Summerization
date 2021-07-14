#tkinter libraries for UI design
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import *
from tkinter.scrolledtext import *

import time
import webbrowser

from nltk_summerizer import nltk_summarizer
from spacy_summerizer import summarizer_text
from gensim.summarization import summarize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# web scrapping
from bs4 import BeautifulSoup
from urllib.request import urlopen

def callback(url):
    webbrowser.open_new(url)

def sumy_summary(docx):
    parser = PlaintextParser.from_string(docx,Tokenizer('english'))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document,3)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result

timr = time.strftime("%y%m%d-%H%M%S")

window = Tk()
window.title("Text Summarizer")
window.geometry('700x600')

# style
style = ttk.Style(window)
style.configure('lefttab.TNotebook')

# tabs
tab_control = ttk.Notebook(window,style='lefttab.TNotebook')

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

tab_control.add(tab1,text = f'{"Home":^20s}')
tab_control.add(tab2,text = f'{"File":^20s}')
tab_control.add(tab3,text = f'{"URL":^20s}')
tab_control.add(tab4,text = f'{"Comparer":^20s}')

# labels
lbl1 = Label(tab1,text='Summarizer',padx=5,pady=5)
lbl1.grid(column=0,row=0)
lbl1 = Label(tab2,text='File Processing',padx=5,pady=5)
lbl1.grid(column=0,row=0)
lbl1 = Label(tab3,text='URL',padx=5,pady=5)
lbl1.grid(column=0,row=0)
lbl1 = Label(tab4,text='Comparer',padx=5,pady=5)
lbl1.grid(column=0,row=0)

tab_control.pack(expand=1,fill='both')

# -:Home tab:-
l1 = Label(tab1,text='Enter text to Summarize',padx=5,pady=5)
l1.grid(column=0,row=1)

entry = ScrolledText(tab1,height=10)
entry.grid(row=2,column=0,columnspan=3,padx=5,pady=5)

# functions
def clear_text():
    entry.delete('1.0',END)
    tab1_display

def get_summary():
    tab1_display.delete('1.0', END)
    raw_text = entry.get('1.0', tk.END)
    final_text = summarizer_text(raw_text)
    result = '\nSummary of the content :\n\n{}'.format(final_text)
    tab1_display.insert(tk.END, result)

def clear_result():
    tab1_display.delete('1.0',END)

def save_summary():
    raw_text = entry.get('1.0',tk.END)
    final_text = summarizer_text(raw_text)
    filename = "summary"+timr+'.txt'
    with open(filename,'w') as f:
        f.write(final_text)
    result = '\nName of file : file{}\nSummary:{}'.format(filename,final_text)
    tab1_display.insert(tk.END, result)

# buttons
btn1 = Button(tab1,text='Reset',command=clear_text,width=12)
btn1.grid(row=4,column=0,padx=10,pady=10)

btn2 = Button(tab1,text='Summarize',command=get_summary,width=12)
btn2.grid(row=4,column=1,padx=10,pady=10)

btn3 = Button(tab1,text='Clear Result',command=clear_result,width=12)
btn3.grid(row=5,column=0,padx=10,pady=10)

btn4 = Button(tab1,text='Save Summary',command=save_summary,width=12)
btn4.grid(row=5,column=1,padx=10,pady=10)

btn6 = Button(tab1,text="Close",command=lambda:exit(),width=12)
btn6.grid(row=9,column=2,padx=10,pady=10)

# display:-
tab1_display = ScrolledText(tab1,height=10)
tab1_display.grid(row=7,column=0,columnspan=3,padx=5,pady =5)

#file
lbl1 = Label(tab2,text='Open File to Summarize',padx=10,pady=10)
lbl1.grid(column=0,row=1)

file_display = ScrolledText(tab2,height=10)
file_display.grid(row=2,column=0,columnspan=3,padx=5,pady=5)

#function
def open_file():
    files = filedialog.askopenfilename(filetypes=[("Text Files","*.txt"),("All Files","*")])
    read_text = open(files).read()
    file_display.insert(tk.END,read_text)
    lbl_file=Label(tab2,text=files,padx=10,pady=10)
    lbl_file.grid(row=3,column=0)

def clear_text_file():
    tab2_display.delete('1.0',END)
    file_display.delete('1.0',END)

def get_summary_file():
    tab2_display.delete('1.0', END)
    raw_text = file_display.get('1.0', tk.END)
    final_text = summarizer_text(raw_text)
    result = '\nSummary of the File :\n\n{}'.format(final_text)
    tab2_display.insert(tk.END, result)

def clear_result_file():
    tab2_display.delete('1.0',END)

b0 = Button(tab2,text="Open File",width=12,command=open_file)
b0.grid(row=4,column=0,padx=5,pady=5)

b1 = Button(tab2,text='Reset',command=clear_text_file,width=12)
b1.grid(row=5,column=0,padx=10,pady=10)

b2 = Button(tab2,text='Summarize',command=get_summary_file,width=12)
b2.grid(row=4,column=1,padx=10,pady=10)

b3 = Button(tab2,text='Clear Result',command=clear_result_file,width=12)
b3.grid(row=5,column=1,padx=10,pady=10)

b4 = Button(tab2,text='Close',command=lambda:exit(),width=12)
b4.grid(row=10,column=2,padx=10,pady=10)

tab2_display = ScrolledText(tab2,height=10)
tab2_display.grid(row=7,column=0,columnspan=3,padx=5,pady=5)

#URL :-
lu1 = Label(tab3,text="Enter URL to Summarize")
lu1.grid(row=1,column=0,padx=10,pady=10)

raw_entry = StringVar()
url_entry = Entry(tab3,textvariable=raw_entry,width=50)
url_entry.grid(row=1,column=1)

url_display = ScrolledText(tab3,height=10)
url_display.grid(row=7,column=0,columnspan=3,padx=5,pady=5)

def clear_text_url():
    url_display.delete('1.0',END)
    tab3_display.delete('1.0',END)

def get_summary_url():
    tab3_display.delete('1.0', END)
    raw_text = url_display.get('1.0', tk.END)
    final_text = summarizer_text(raw_text)
    result = '\nSummary of thr URL:\n\n{}'.format(final_text)
    tab3_display.insert(tk.END, result)


def clear_result_url():
    tab3_display.delete('1.0',END)

def get_url_text():
    raw_text = str(url_entry.get())
    page = urlopen(raw_text)
    soup = BeautifulSoup(page,'html.parser')
    fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
    url_display.insert(tk.END,fetched_text)

bu1 = Button(tab3,text='Reset',command=clear_text_url,width=12)
bu1.grid(row=8,column=0,padx=10,pady=10)

bu2 = Button(tab3,text='Summarize',command=get_summary_url,width=12)
bu2.grid(row=9,column=0,padx=10,pady=10)

bu3 = Button(tab3,text='Clear Result',command=clear_result_url,width=12)
bu3.grid(row=9,column=1,padx=10,pady=10)

bu4 = Button(tab3,text = 'Get Text',command=get_url_text,width=12)
bu4.grid(row=8,column=1,padx=10,pady=10)

bu5 = Button(tab3,text="Close",command=lambda:exit(),width=12)
bu5.grid(row=12,column=2,padx=10,pady=10)

tab3_display = ScrolledText(tab3,height=10)
tab3_display.grid(row=10,column=0,columnspan=3,padx=5,pady=5)

#comparer
l41 = Label(tab4,text='Enter text to Summarize',padx=10,pady=10)
l41.grid(column=0,row=1)

entry_com = ScrolledText(tab4,height=10)
entry_com.grid(row=2,column=0,columnspan=3,padx=5,pady=5)

#functions:-

def clear_text_com():
    tab4_display.delete('1.0',END)
    entry_com.delete('1.0',END)

def get_summary_spacy():
    tab4_display.delete('1.0',END)
    raw_text = entry_com.get('1.0', tk.END)
    final_text = summarizer_text(raw_text)
    result = '\nSummary of the given content (Spacy):\n\n{}'.format(final_text)
    tab4_display.insert(tk.END, result)

def clear_result_com():
    tab4_display.delete('1.0',END)

def get_summary_nltk():
    tab4_display.delete('1.0',END)
    raw_text = entry_com.get('1.0', tk.END)
    final_text = nltk_summarizer(raw_text)
    result = '\nSummary of the given content (NLTK):\n\n{}'.format(final_text)
    tab4_display.insert(tk.END, result)

def get_summary_gensim():
    tab4_display.delete('1.0',END)
    raw_text = entry_com.get('1.0', tk.END)
    final_text = summarize(raw_text)
    result = '\nSummary of the given content (Gensim):\n\n{}'.format(final_text)
    tab4_display.insert(tk.END, result)

def get_summary_sumy():
    tab4_display.delete('1.0',END)
    raw_text = entry_com.get('1.0', tk.END)
    final_text = sumy_summary(raw_text)
    result = '\nSummary of the given content (Sumy):\n\n{}'.format(final_text)
    tab4_display.insert(tk.END, result)

#buttons
btnc1 = Button(tab4,text='Reset',command=clear_text_com,width=12)
btnc1.grid(row=4,column=0,padx=10,pady=10)

btnc2 = Button(tab4,text='Spacy',command=get_summary_spacy,width=12)
btnc2.grid(row=4,column=2,padx=10,pady=10)

btnc3 = Button(tab4,text='Clear Result',command=clear_result_com,width=12)
btnc3.grid(row=4,column=1,padx=10,pady=10)

btnc4 = Button(tab4,text='NLTK',command=get_summary_nltk,width=12)
btnc4.grid(row=5,column=0,padx=10,pady=10)

btnc5 = Button(tab4,text='Gensim',command=get_summary_gensim,width=12)
btnc5.grid(row=5,column=1,padx=10,pady=10)

btnc5 = Button(tab4,text='Sumy',command=get_summary_sumy,width=12)
btnc5.grid(row=5,column=2,padx=10,pady=10)

btnc7 = Button(tab4,text="Close",command=lambda:exit(),width=12)
btnc7.grid(row=9,column=2,padx=10,pady=10)

variable = StringVar()

tab4_display = ScrolledText(tab4,height=10)
tab4_display.grid(row=7,column=0,columnspan=3,padx=5,pady=5)

window.mainloop()



