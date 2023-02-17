#!/usr/bin/python3

import os
import re
import socket
from collections import Counter
from pathlib import Path

CWD = Path(os.getcwd())
OUTPUT_DIR = Path('/home/output/')

def read_file(file):
    with open(file, "r") as f:
        return f.read()

def count_words(file):
    content = read_file(file)
    text = content.lower().replace("\n", " ").replace(chr(8212), " ")
    text = re.sub("[^\w ']", "", text)
    text = text.split()
    words = Counter(text)
    return dict(words)

def docker_ip():
    return socket.gethostbyname(socket.gethostname())

def main():
    """
    a. List name of all the text file at location: /home/data
    b. Read the two text files and count total number of words in each text files
    c. Add all the number of words to find the grand total (total number of words in both files)
    d. List the top 3 words with maximum number of counts in IF.txt.  Include the word counts for the top 3 words.
    e. Find the IP address of your machine
    f. Write all the output to a text file at location: /home/output/result.txt (inside your container).
    g. Upon running your container, it should do all the above stated steps and print the information on console from result.txt file and exit.
    """
    txt_files = list(Path(CWD, "data").glob('*.txt'))
    [print(f) for f in txt_files]

    IF_words = count_words(txt_files[0])
    Limerick_words = count_words(txt_files[1])
    ip = docker_ip()

    print(IF_words, Limerick_words, ip)
if __name__ == "__main__":
    main()