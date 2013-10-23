__author__ = 'Litvinov'
#Your optional code here
#You can import some modules or create additional functions


def checkio(line):
    #Your code goes here
    #This is the main function.
    #It's must return the result for auto-testing, so don't remove it!
    one_bsp = 1
    temp = ""
    for x in line:
        if ((x == "-") & (int(one_bsp) == 0)):
            continue;
        else :
            if (x == "-") :
                one_bsp = 0
            else :
                one_bsp = 1
            temp +=x
    line = temp
    return line

#Some hints
#you can use split and join methods from string.
#If you used replace() -- don't forget about three or four dashes
#Maybe regexp

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    assert checkio('I-like--python---a----lot') == "I-like-python",'Example'
