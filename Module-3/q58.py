import random
f1=open('text2.txt','a')
f1.write('hello,good moring students!')
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('text2.txt'))