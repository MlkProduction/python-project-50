import argparse

def parsing():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='first config file')
    parser.add_argument('second_file', help='second config file')
    parser.add_argument(
        '-f', '--format',
                    help='set format of output',
                    choices=['stylish', 'plain', 'json'],
                    default='stylish')
    return parser.parse_args()

