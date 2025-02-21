import random
import string

def special_characters(): 
    return '!@#$%^&*()'


def generate_password(length=8, use_uppercase=False, use_lowercase=True, use_digits=False, use_special=False):
    if length <= 0:
        return ''
    
    password = []


    char_table = ''
    if use_uppercase:
        char_table += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        char_table += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        char_table += string.digits
        password.append(random.choice(string.digits))
    if use_special:
        char_table += special_characters()
        password.append(random.choice(special_characters()))
    
    if len(char_table) == 0:
        return ''
        
    password += [random.choice(char_table) for _ in range(length - len(password))]
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    print(generate_password())