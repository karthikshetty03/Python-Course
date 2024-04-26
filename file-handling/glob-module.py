import glob

if __name__ == '__main__':
    for file in glob.glob('*.py'):
        print(file)

    for file in glob.glob('????ing.py'):
        print("Found1", file)

    for file in glob.glob('[a-z]*ing.py'):  # first letter [a-z] means any character from a to z
        print("Found2", file)

    for file in glob.glob('[!ms]*'):  # first letter [a-z] means any character from a to z
        print("Found3", file, end=' ')
    else:
        print()

    # recursive search
    for file in glob.glob('**/*.py', recursive=True, root_dir='/Users/kashett2/Downloads', include_hidden=True):
        print("Found4", file, end=' ')
    else:
        print()
