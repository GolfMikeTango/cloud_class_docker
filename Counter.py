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

def write_results(results):
    with open(Path(OUTPUT_DIR, 'results.txt'), "w") as f:
        return f.write(results)

def count_words(file):
    """
    Reads file from path, removes non words with regex, counts words and sorts by most common, and returns

    :param file: Path to a file 
    :type file: str
    :returns dict: Dictionary of counted and sorted words by most common
    """
    content = read_file(file)
    text = content.lower().replace("\n", " ").replace(chr(8212), " ")
    text = re.sub("[^\w ']", "", text)
    text = text.split()
    words = Counter(text).most_common()
    return dict(words)


def docker_ip():
    """
    :returns str: string of the docker IP. There should only be one as no other networking is done in the container
    """
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

    IF_words = count_words(txt_files[0])
    Limerick_words = count_words(txt_files[1])
    total_words = sum(IF_words.values()) + sum(Limerick_words.values())
    if_top_3 = list(IF_words.items())[:3]
    top3 = ""
    for i in if_top_3:
        top3 += f"Word is: {i[0]}\tCount is: {i[1]}\n"
    ip = docker_ip()

    output = f"Text File Paths in {CWD}: {[f.name for f in txt_files]}\n\
Grand total word is: {total_words}\n\
Top 3 words in IF.txt:\n{top3}\n\
Container IP: {ip}"

    print("Writing output...")
    write_results(output)

if __name__ == "__main__":
    main()
