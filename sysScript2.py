from sys import argv
if len(argv) == 3:
    print(f"Wellcome {argv[1]} {argv[2]}!")
elif len(argv) == 4 and argv[3].isdigit():
    print(f"Wellcome {argv[1]} {argv[2]} with age {argv[3]}!")
else:
    raise IndexError('Wrong inputs!')

