"""This program..."""

__author__ = "Will Lam lamwillp88@gmail.com"

LETTERS_IN_ALPHABET: int = 26
ASCII_INDEX: int = 97
UNIT_DISPLACE: int = 1


#function will take a letter and returned the coded version of that letter
def encode_char(character: str) -> str:
    low_character: str = character.lower()
    ascii_code: int = ord(low_character)
    normalized_code: int = ascii_code - ASCII_INDEX
    encoded_code: int = (normalized_code + UNIT_DISPLACE) % LETTERS_IN_ALPHABET + ASCII_INDEX
    encoded_character: str = chr(encoded_code)
    return encoded_character

#function will take a four letter word and return a coded word, by changing each character indexed
def encode_str(word: str) -> str:
    
    c1: str = encode_char(word[0])
    c2: str = encode_char(word[1])
    c3: str = encode_char(word[2])
    c4: str = encode_char(word[3])

    coded_word: str = c1 + c2 + c3 +c4 
    return coded_word

#function will take a coded letter and returned the decoded version of that letter
def decode_char(character: str) -> str:
    low_character: str = character.lower()
    ascii_decode: int = ord(low_character)
    normalized_code: int = ascii_decode - ASCII_INDEX
    decoded_code: int = (normalized_code - UNIT_DISPLACE) % LETTERS_IN_ALPHABET + ASCII_INDEX
    decoded_character: str = chr(decoded_code)
    return decoded_character

#function will take a coded four letter word and return a decoded word, by changing each character indexed
def decode_str(word: str) -> str:
    
    c1: str = decode_char(word[0])
    c2: str = decode_char(word[1])
    c3: str = decode_char(word[2])
    c4: str = decode_char(word[3])

    decoded_word: str = c1 + c2 + c3 +c4 
    return decoded_word







# Notes:
# ord(str) -> int
# chr(int) -> str#