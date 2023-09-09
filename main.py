import re


def main():
    with open('input') as f:
        current_dir = ''
        directories= dict()
        current_size = 0

        for line in f:
            print(f'line is : {line}')
            l = line.split(' ')
            # print(f'l 0 is {l[0]}')
            match = re.match('cd$', l[1])
            if(match != None):
                # print(f'entered directory : {l[2]}')
                # ARE WE MISSING The last itme like this?
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
        print('done')


main()
