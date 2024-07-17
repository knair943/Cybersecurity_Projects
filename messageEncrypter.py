# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:23:36 2024

@author: knair
"""
#Program which takes a message and returns an encrypted message by shifting down each character by 3 letters
import string

def caesar_encrypt(message, key):
    
    shift = key % 26
    cipher =  str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    
    encrypted_message = message.lower().translate(cipher)
    
    return encrypted_message

def caesar_decrypt(encrypted_message, key):
    
    shift = 26 - (key % 26)
    cipher =  str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    
    message = encrypted_message.translate(cipher)
    return message

message = input("Enter a message: ")
key = 3
 
encrypted_message = caesar_encrypt(message, key)
print("Encrypted Message:", encrypted_message)

decrypted_message = caesar_decrypt(encrypted_message, key)
print("Decrypted Message:", decrypted_message)

