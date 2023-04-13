import argparse
parse = argparse.ArgumentParser()
parse.add_argument('FILE_NAME', type=str)
parse.add_argument('-n', action='store_true')
args = parse.parse_args()

with open(args.FILE_NAME, 'r') as f:
    if args.n:
        print('Number of lines in the file:', len(f.readlines()))
    else:
        print(f.read())
print(args.n)

# Salam G5
