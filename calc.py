from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("num1",type=float)
parser.add_argument("num2",type=float)
parser.add_argument("--operation","-o",required=True,type=str)

args = parser.parse_args()

eval(f"print({args.num1}{args.operation}{args.num2})")


