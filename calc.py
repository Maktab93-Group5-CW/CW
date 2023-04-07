from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("num1",nargs=2, type=float)
# parser.add_argument("num2",type=float)
parser.add_argument("--operation","-o",required=True,type=str, choices=['+','-','*','/'],metavar='operation')

args = parser.parse_args()

eval(f"print({args.num1[0]}{args.operation}{args.num1[1]})")


