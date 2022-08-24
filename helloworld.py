import random 
letters = [' ', '!', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']

out = ''
count = 0
while out != 'hello world!':
    out = ''
    for i in range(0, len(letters)):
        out += letters[random.randint(0,11)]
    count += 1
    
print(f'{out} made on iteration number {count}!')