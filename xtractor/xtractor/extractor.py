'''
    This module contains functions which get the text content of an xml file, strips it of its xml tags and returns what is left.

    the get_text function can also parse text from ordinary text files (format txt) and html files.
'''
import re, fire

def get_text(enc='utf-8', filepath=None):
    """returns text from a file"""
    if filepath == None:
        file = input("Provide path to the file to be extracted: \n")
    else:
        file = filepath
    f = open(file,'r',encoding = enc)
    return f.read()

def strip_tags(text):
    '''Goes through text and removes all xml tags from it'''
    pattern = re.compile(r"<.*?>")
    return pattern.sub('',text)


def extract(path_to_xml, destination=""):
    t = get_text(filepath = path_to_xml)
    stripped = strip_tags(t)
    print(stripped)
    if destination != "": #if a destination for extracted text file is provided
        f = open(destination+"\\recovered.txt", "a")
        f.write(stripped)
        f.close()
    return stripped
