"""This program encodes and decodes characters and strings of any length and capitalization"""

__author__ = "Will Lam lamwillp88@gmail.com"

LETTERS_IN_ALPHABET: int = 26
ASCII_INDEX: int = 97
ASCII_INDEX_UPPER: int = 65
UNIT_DISPLACE: int = 1


#function will take a letter and returned the coded version of that letter
def encode_char(character: str) -> str:
    ascii_code: int = ord(character)
    ascii_index: int = ASCII_INDEX

    #determines the value of ASCII_INDEX based on input
    if character.islower():
        ascii_index = 97
    else:
        ascii_index = 65
    normalized_code: int = ascii_code - ascii_index
    encoded_code: int = (normalized_code + UNIT_DISPLACE) % LETTERS_IN_ALPHABET + ascii_index
    encoded_character: str = chr(encoded_code)
    return encoded_character


#function will take a four letter word and return a coded word, by changing each character indexed
def encode_str(letters: str) -> str:
    i: int = 0
    encoded_letters: str = ""

    while i < len(letters):
        encoded_letter: str = encode_char(letters[i])
        encoded_letters += encoded_letter
        i = i + 1
    return encoded_letters


#function will take a coded letter and returned the decoded version of that letter
def decode_char(character: str) -> str:
    ascii_decode: int = ord(character)
    ascii_index: int = ASCII_INDEX

    #determines the value of ASCII_INDEX based on input
    if character.islower():
        ascii_index = 97
    else:
        ascii_index = 65

    normalized_code: int = ascii_decode - ascii_index
    decoded_code: int = (normalized_code - UNIT_DISPLACE) % LETTERS_IN_ALPHABET + ascii_index
    decoded_character: str = chr(decoded_code)
    return decoded_character


#function will take a coded four letter word and return a decoded word, by changing each character indexed
def decode_str(letters: str) -> str:
    i: int = 0
    decoded_letters: str = ""
    
    while i < len(letters):
        decoded_letter: str = decode_char(letters[i])
        decoded_letters += decoded_letter
        i = i + 1
    return decoded_letters