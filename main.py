import re


def main():
    with open('input') as f:
        current_dir = ''
        directories= dict()
        current_size = 0
        dir_count = 0

        for line in f:
            print(f'line is : {line}')
            l = line.split(' ')
            if(re.match('cd$', l[1])):
                dir_count += 1
                print(f'found dir {l[2]}')
                if(current_dir):
                    directories[current_dir] = current_size
                current_dir = l[2]
                current_size = 0

            if(re.match('^[0-9]+$', l[0])):
                print(f'found file of size : {l[0]}')
                current_size += int(l[0])

        if(current_dir):
            directories[current_dir] = current_size

        for k in directories:
            print(f'{k} size == {directories[k]}')
        print(len(directories.keys()))
        print(dir_count)
        print('done')


main()
