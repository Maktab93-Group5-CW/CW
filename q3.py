import argparse
parser = argparse.ArgumentParser(description='knsfkacm[a]', epilog='ye chizi')
parser.add_argument('name', type=str)
parser.add_argument('last_name', type=str)
parser.add_argument('-a', '--age', type=int)
args = parser.parse_args()
print(f'Wellcome {args.name} {args.last_name} with age {args.age}' if args.age else f'Wellcome {args.name} {args.last_name}')
