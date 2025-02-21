import unittest
from password_generator import generate_password, special_characters

class TestPasswordGenerator(unittest.TestCase):
    
    def test_password_length(self):
        length = 12
        password = generate_password(length=length)
        self.assertEqual(len(password), length)
    
    def test_password_contains_uppercase(self):
        password = generate_password(length=12, use_uppercase=True)
        self.assertTrue(any(char.isupper() for char in password))
    
    def test_password_contains_lowercase(self):
        password = generate_password(length=12, use_lowercase=True)
        self.assertTrue(any(char.islower() for char in password))
    
    def test_password_contains_digits(self):
        password = generate_password(length=12, use_digits=True)
        self.assertTrue(any(char.isdigit() for char in password))
    
    def test_password_contains_special_characters(self):
        password = generate_password(length=12, use_special=True)
        self.assertTrue(any(char in special_characters() for char in password))
    
    def test_password_no_options(self):
        password = generate_password(length=12, use_uppercase=False, use_lowercase=False, use_digits=False, use_special=False)
        self.assertEqual(password, '')

    def test_zero_length_password(self):
        password = generate_password(length=0, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True)
        self.assertEqual(password, '')
    
    def test_negative_length_password(self):
        password = generate_password(length=-1, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True)
        self.assertEqual(password, '')
    
    def test_no_character_types_selected(self):
        password = generate_password(length=12, use_uppercase=False, use_lowercase=False, use_digits=False, use_special=False)
        self.assertEqual(password, '')

    def test_password_contains_all_requested_options(self):
        for _ in range(100):
            password = generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True)
            print(password)
            self.assertTrue(any(char.isupper() for char in password))
            self.assertTrue(any(char.islower() for char in password))
            self.assertTrue(any(char.isdigit() for char in password))
            self.assertTrue(any(char in special_characters() for char in password))

if __name__ == '__main__':
    unittest.main()
