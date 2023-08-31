import argparse

parser = argparse.ArgumentParser(prog='Dummy', description='Dummy description', epilog='Dummy at bottom')

parser.add_argument('filename', help='Enter the file name')
parser.add_argument('-c', '--count', help='Enter the number of count.')
parser.add_argument('-v', '--verbose', help='Enter the verbose level.')

args = parser.parse_args()

print(args.filename, args.count, args.verbose)