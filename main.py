import re

# $ cd 
# $ ls
# dir <>
# size filename
#
#
# $ cd /
# $ ls
# dir bntdgzs
# 179593 cjw.jgc
# 110209 grbwdwsm.znn
# dir hsswswtq
# dir jdfwmhg
# dir jlcbpsr
# 70323 qdtbvqjj
# 48606 qdtbvqjj.zdg
# dir tvcr
# dir vhjbjr
# dir vvsg
# 270523 wpsjfqtn.ljt
# $ cd bntdgzs
#
#
from typing import List, Dict

class Directory():
    def __init__(self, name: str, parent: 'Directory'):
        self.name = name
        self.parent: 'Directory' = parent
        self.dirs: List['Directory'] = []
        self.files: List[Dict[int, str]] = []
    

def main():
    with open('input') as f:
        current_dir = ''
        dir_count = 0

        for line in f:
            line = line.rstrip()
            print(f'current line {line}')
            EXIT_DIR = re.match('^\$ cd \.\.$', line)
            GO_TO_ROOT = re.match('^\$ cd \/$', line)
            GO_TO_DIR = re.match('^\$ cd \w+$', line)
            LIST_DIR = re.match('^\$ ls$', line)
            DIR = re.match('^dir \w+', line)
            FILE = re.match('^\d+ \w+', line)

            if(EXIT_DIR):
                print('matched exit dir')
            elif(GO_TO_ROOT):
                print('matched go to root')
            elif(GO_TO_DIR):
                print('matched go to dir')
            elif(LIST_DIR):
                print('matched ls ')
            elif(DIR):
                print('matched a directory')
            elif(FILE):
                print('matched a file')
            else:
                raise Exception('Invalid input')

                

            #
            # # print(f'line is : {line}')
            # l = line.split(' ')
            # match = re.match('cd$', l[1])
            # if(match):
            #     # print(f'found dir {l[2]}')
            #     if(l[2] == '..\n'):
            #         # print('exiting directory')
            #         continue
            #     current_dir = l[2].rstrip()
            #     if current_dir not in directories:
            #         directories[current_dir] = True
            #         print(f'adding dire {repr(current_dir)}')
            #         dir_count += 1
            #         print(f'dir count is = {dir_count}')
            # if(re.match('^[0-9]+$', l[0])):
            #     # print(f'found file of size : {l[0]}')
            #     pass
            #
        # if(current_dir):
        #     directories[current_dir] = True

        # for k in directories:
        #     print(f'{k} size == {directories[k]}')
        # print(len(directories.keys()))
        # for d in sorted(directories.keys()):
        #     print(d)
        # print(dir_count)
        # print('done')


main()


# dict of directories => list of files and subdirectories
# {'/', [foo, bar, 100, 200]}
