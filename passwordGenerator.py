# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:31:31 2024

@author: knair
"""

import random
import string

def generate_password(length: int = 10):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password
    
password = generate_password()
print(f"Generate Password: ", password)

        