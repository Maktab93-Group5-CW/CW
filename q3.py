import argparse
parse = argparse.ArgumentParser()
parse.add_argument('name', type=str)
parse.add_argument('last_name', type=str)
parse.add_argument('-a','--age', type=int)
args = parse.parse_args()
print(f'Wellcome {args.name} {args.last_name} with age {args.age}' if args.age else f'Wellcome {args.name} {args.last_name}')