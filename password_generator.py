import random

def generate_password(length=8, use_uppercase=False, use_lowercase=True, use_digits=False, use_special=False):
    if length <= 0:
        return ''
    
    char_table = ''
    if use_uppercase:
        char_table += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if use_lowercase:
        char_table += 'abcdefghijklmnopqrstuvwxyz'
    if use_digits:
        char_table += '0123456789'
    if use_special:
        char_table += '!@#$%^&*()'
    
    if len(char_table) == 0:
        return ''
        
    for i in range(length):
        password = ''.join(random.choice(char_table) for i in range(length))
        return password


if __name__ == "__main__":
    generate_password()