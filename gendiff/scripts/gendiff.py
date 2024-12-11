import argparse

parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration files and shows a difference')

parser.add_argument('first_file')           # positional argument
parser.add_argument('second_file')           # positional argument
parser.add_argument('-f', '--format', help="Set format of output")
args = parser.parse_args()

def main():
	  print(f"Comparing {args.first_file} with {args.second_file}")

if __name__ == "__main__":
    main()
