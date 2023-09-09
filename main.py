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
    def __init__(self, name: str, parent = None):
        self.name = name
        self.parent: 'Directory'| None = parent
        self.dirs: List['Directory'] = []
        self.files: List[Dict[str, int]] = []
    

def main():
    with open('input') as f:
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
                #print('matched exit dir')
                pass
            elif(GO_TO_DIR):
                #print('matched go to dir')
                dir_name = line.split()[2]
                #print(f'dir name is {repr(dir_name)}')
                for d in current_dir.dirs:
                    current_dir = None
                    #print(f'd name is {repr(d.name)}')
                    if d.name == dir_name:
                        current_dir = d
                        #print(f'matched name, setting current dir to ...{current_dir}')
                        break
                    if current_dir == None:
                        raise Exception('Couldnt find a matching directory for')
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

                
        print(root.name)
        for d in root.dirs:
            print(d.name)
        for f in root.files:
            print(f)


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
