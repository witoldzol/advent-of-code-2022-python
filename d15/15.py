import re
def parse(line:str):
    pattern = r'.*x=(.*),.*y=(.*):.*x=(.*),.*y=(.*)$'
    m = re.search(pattern,line)
    if m:
        sx,sy,bx,by = m.groups()
        sx,sy,bx,by = int(sx),int(sy),int(bx),int(by)
        print(sx,sy,bx,by)
    else:
        print('no match')

def main(filename):
    f = open(filename, 'r')
    data = f.read().strip()
    lines = data.split('\n')
    for l in lines:
        parse(l)

if __name__ == '__main__':
    main('input')
    # main('sample_input')
