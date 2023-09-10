import re
import sys

from typing import List, Dict

class Directory():
    def __init__(self, name: str, parent = None):
        self.name = name
        self.parent: 'Directory'| None = parent
        self.dirs: List['Directory'] = []
        self.files: List[Dict[str, int]] = []
    

def main():
    create_tree('input')

def create_tree(file: str) -> Directory:
    with open(file) as f:
        root = Directory('/', None)
        current_dir = root
        for line in f:
            line = line.rstrip()
            # print(f'current line {line}')
            EXIT_DIR = re.match('^\$ cd \.\.$', line)
            GO_TO_ROOT = re.match('^\$ cd \/$', line)
            GO_TO_DIR = re.match('^\$ cd \w+$', line)
            LIST_DIR = re.match('^\$ ls$', line)
            DIR = re.match('^dir \w+', line)
            FILE = re.match('^\d+ \w+', line)
            if(EXIT_DIR):
                current_dir = current_dir.parent
            elif(GO_TO_DIR):
                #print('matched go to dir')
                dir_name = line.split()[2]
                #print(f'dir name is {repr(dir_name)}')
                temp = current_dir
                for d in current_dir.dirs:
                    if d.name == dir_name:
                        current_dir = d
                        break
                if temp == current_dir:
                    raise Exception("Failed to find child folder")
            elif(LIST_DIR):
                #print('matched ls ')
                pass
            elif(DIR):
                #print('matched a directory')
                dir_name = line.split()[1]
                d = Directory(dir_name, current_dir)
                current_dir.dirs.append(d)
            elif(FILE):
                #print('matched a file')
                size = int(line.split()[0])
                file_name = line.split()[1]
                current_dir.files.append({file_name: size})
            elif(GO_TO_ROOT):
                #print('matched go to root')
                continue
            else:
                raise Exception('Invalid input')

        return root

if __name__ == "__main__":
    main()
