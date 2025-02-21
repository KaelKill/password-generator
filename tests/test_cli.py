import unittest
import subprocess

class TestPasswordGeneratorCLI(unittest.TestCase):
    
    def run_cli(self, *args):
        result = subprocess.run(['python', 'cli.py'] + list(args), capture_output=True, text=True)
        return result.stdout.strip()
    
    def test_cli_default_length(self):
        output = self.run_cli()
        print('output: ' + output)
        self.assertEqual(len(output), 8)
    
    def test_cli_custom_length(self):
        output = self.run_cli('--length', '12')
        print(output)
        self.assertEqual(len(output), 12)
    
    def test_cli_uppercase(self):
        output = self.run_cli('--length', '12', '--uppercase')
        self.assertTrue(any(char.isupper() for char in output))
    
    def test_cli_lowercase(self):
        output = self.run_cli('--length', '12', '--lowercase')
        self.assertTrue(any(char.islower() for char in output))
    
    def test_cli_digits(self):
        output = self.run_cli('--length', '12', '--numbers')
        self.assertTrue(any(char.isdigit() for char in output))
    
    def test_cli_special(self):
        output = self.run_cli('--length', '12', '--special')
        self.assertTrue(any(char in '!@#$%^&*()' for char in output))
    
    def test_cli_no_options(self):
        output = self.run_cli('--length', '12', '--no-uppercase', '--no-lowercase', '--no-digits', '--no-special')
        self.assertEqual(output, '')

if __name__ == '__main__':
    unittest.main()
