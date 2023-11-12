data = open('sample_input').read().strip()
lines = [x for x in data.split('\n') ]
for l in lines:
    print(l)
    for c in l.split('->'):
        c = c.strip()
        x,y = c.split(',')
        x,y = int(x), int(y)
