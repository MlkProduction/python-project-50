from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.parser import parsing

def main():
    args = parsing()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)

if __name__ == '__main__':
    main()