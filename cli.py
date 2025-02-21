import argparse
from password_generator import generate_password

def cli():
  parser = argparse.ArgumentParser(description='Generate a random password')  
  parser.add_argument('--length', type=int, default=8, action='store')
  parser.add_argument('--uppercase', action='store_true', dest='use_uppercase')
  parser.add_argument('--lowercase', action='store_true', dest='use_lowercase', default=True)
  parser.add_argument('--numbers', action='store_true', dest='use_digits')
  parser.add_argument('--special', action='store_true', dest='use_special')

  args = parser.parse_args()
  password = generate_password(length=args.length, 
                               use_uppercase=args.use_uppercase, 
                               use_lowercase=args.use_lowercase,
                               use_digits=args.use_digits,
                               use_special=args.use_special)
  print(password)

if __name__ == "__main__":
    cli()