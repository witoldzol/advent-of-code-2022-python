import re


def main():
    with open('input') as f:
        current_dir = ''
        directories= dict()
        current_size = 0
        dir_count = 0

        for line in f:
            # print(f'line is : {line}')
            l = line.split(' ')
            match = re.match('cd$', l[1])
            if(match):
                # print(f'found dir {l[2]}')
                if(l[2] == '..\n'):
                    # print('exiting directory')
                    continue
                current_dir = l[2].rstrip()
                if current_dir not in directories:
                    directories[current_dir] = True
                    print(f'adding dire {repr(current_dir)}')
                    dir_count += 1
                    print(f'dir count is = {dir_count}')
            if(re.match('^[0-9]+$', l[0])):
                # print(f'found file of size : {l[0]}')
                pass

        # if(current_dir):
        #     directories[current_dir] = True

        # for k in directories:
        #     print(f'{k} size == {directories[k]}')
        print(len(directories.keys()))
        # for d in sorted(directories.keys()):
        #     print(d)
        print(dir_count)
        print('done')


main()


# dict of directories => list of files and subdirectories
# {'/', [foo, bar, 100, 200]}
