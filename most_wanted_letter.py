__author__ = 'Litvinov'
import re
def checkio(text):

    text.lower()
    most_wanted_letter = ''
    temporary_most_wanted = ''
    most_wanted_count = 1
    while(len(text)):
        temporary_most_wanted = text[0]
        if text[0].isalpha() and text.count(temporary_most_wanted) >= most_wanted_count and temporary_most_wanted >= text[0]:
              most_wanted_count = text.count(temporary_most_wanted)
              most_wanted_letter = text[0]
        #need to  remove all intrances of this character
        text = text.strip(text[0])
    return most_wanted_letter

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #assert checkio("Hello World!") == "l", "Hello test"
    #assert checkio("How do you do?") == "o", "O is most wanted"
    #assert checkio("One") == "e", "All letter only once."
    assert checkio("fn;lsfndasl;f naslkdnlkasdnfslahwemwjkrjkl;zcmk;lzcdkcslksdkseewme,") == "k"