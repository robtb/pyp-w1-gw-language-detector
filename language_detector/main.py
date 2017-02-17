# -*- coding: utf-8 -*-

"""This is the entry point of the program."""


def detect_language(text, languages):
    """Returns the detected language of given text."""
    # implement your solution here
    text_list = text.split()
    tally = {}
    for i in range(len(languages)):
        count = 0
        for word in text_list:
            if word in languages[i]['common_words']:
                count += 1
        tally[languages[i]['name']] = count
        
    return max(tally, key=tally.get)
    

 
