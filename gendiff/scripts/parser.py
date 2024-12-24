import argparse
from gendiff.scripts.two_dicts import two_dicts_json, two_dicts_yaml

def main():

    parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration files and shows a difference')

    parser.add_argument('first_file')           # positional argument
    parser.add_argument('second_file')           # positional argument
    parser.add_argument('-f', '--format', help="Set format of output")
    args = parser.parse_args()

    #json_file = two_dicts_json(args.first_file, args.second_file)
    #print(json_file)

    yaml_file = two_dicts_yaml(args.first_file, args.second_file)
    print(yaml_file)
    #two_dicts_yaml(args.first_file, args.second_file)
if __name__ == "__main__":
    main()
