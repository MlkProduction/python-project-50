import argparse

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='Compares two configuration files and shows a difference',
                    epilog='show this help message and exit')

parser.add_argument('first_file')           # positional argument
parser.add_argument('second_file')           # positional argument

args = parser.parse_args()

def main():
	  print(f"Comparing {args.first_file} with {args.second_file}")

if __name__ == "__main__":
    main()
