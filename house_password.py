__author__ = 'Litvinov'
import re
def checkio(data):

    password_is_awesome = False
    more_than_ten_symbols = 0
    has_upper_case = 0
    has_lower_case = 0
    has_digit = 0

    if (data.__len__() >= 10) :
        more_than_ten_symbols = 1
    else :
        more_than_ten_symbols = 0
    lower_case_pattern = re.compile('[a-z]')
    upper_case_pattern = re.compile('[A-Z]')
    digit_pattern = re.compile('[0-9]')
    if re.search (upper_case_pattern, data) :
        has_upper_case = 1
    else :
        has_upper_case = 0
    if re.search ( lower_case_pattern, data) :
         has_lower_case = 1
    else :
         has_lower_case = 0
    if re.search ( digit_pattern, data) :
         has_digit = 1
    else :
         has_digit = 0
    if (more_than_ten_symbols & has_digit & has_lower_case & has_lower_case):
        password_is_awesome = True
    else :
        password_is_awesome = False
    return password_is_awesome
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
