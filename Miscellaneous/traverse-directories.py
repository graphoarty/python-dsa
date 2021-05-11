import os

def TraverseDirectory(directory, space, hashes):
    for item in os.scandir(directory):
        if not item.is_file():
            if not (item.name.__contains__('.git') or item.name.__contains__('__pycache__')):
                print(hashes + ' ' + item.name + '<br />')
                TraverseDirectory(os.path.join(directory, item.name), space + '&nbsp;&nbsp;&nbsp;&nbsp;', hashes + '#')
        else:
            print(space + item.name + '<br />')

TraverseDirectory('.', '', '##') 