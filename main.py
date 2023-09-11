import re

from typing import List, Dict

class Directory():
    def __init__(self, name: str, parent = None):
        self.name = name
        self.parent: 'Directory'| None = parent
        self.dirs: List['Directory'] = []
        self.files: List[Dict[str, int]] = []
        self.size: int = 0
    
    def depth_first_traversal(self, n: int = 0):
        tabs = '|' * n
        n += 1
        print(tabs + self.name)
        for d in self.dirs:
            d.depth_first_traversal(n)
    def sum_files(self):
        sum = 0
        for f in self.files:
            sum += list(f.values())[0]
        return sum

    def get_sum(self) -> int:
        sum = self.sum_files()
        for d in self.dirs:
            sum += d.get_sum()
        return sum




def main():
    root = create_tree('input')
    root.depth_first_traversal()
    print('sum is : ' + str(root.get_sum()))


def create_tree(file: str) -> Directory:
    with open(file) as f:
        counter = 0
        root = Directory('/', None)
        current_dir = root
        for line in f:
            line = line.rstrip()
            # print(f'current line {line}')
            EXIT_DIR = re.match(r'^\$ cd \.\.$', line)
            GO_TO_ROOT = re.match(r'^\$ cd \/$', line)
            GO_TO_DIR = re.match(r'^\$ cd \w+$', line)
            LIST_DIR = re.match(r'^\$ ls$', line)
            DIR = re.match(r'^dir \w+', line)
            FILE = re.match(r'^\d+ \w+', line)
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
                counter += 1
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

        print(f' conter : = {counter}')
        return root

if __name__ == "__main__":
    main()
