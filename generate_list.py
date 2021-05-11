import os

def TraverseDirectory(directory, space):
    for item in os.scandir(directory):
        if not item.is_file():
            if not (item.name.__contains__('.git') or item.name.__contains__('__pycache__')):
                print(space + item.name)
                TraverseDirectory(os.path.join(directory, item.name), space + '    ')
        else:
            print(space + item.name)

TraverseDirectory('.', '')
        
