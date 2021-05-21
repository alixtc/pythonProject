text = 'aveesfg'


def isPhoneNumber(text):
    if len(text) != 12:
        return False

    for i in range(0,3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4,7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True


def find_phone_number(text):
    for idx in range(len(text)):
        chunk_text = text[idx:idx + 12]
        if isPhoneNumber(chunk_text):
            print('Phone number found:' + chunk_text)


print(isPhoneNumber(text))
print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))

find_phone_number('Is 415-555-4242 a phone number?')


# --------

import re
regexPhoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = regexPhoneNumber.search('My number is 415-555-4242.')
print('Phone number found:' + mo.group())