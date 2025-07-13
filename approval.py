import random
import os
import sys
word=''
lst1=['k','m','n','g','o','s','q','p','h']
lst2=['1','2','3','4','5','6','7','8','9']
decoded=''
word=''
if not os.path.exists('secretkey.txt'):
    for _ in range(8):
        i=random.randint(1,9)
        word=word+str(i)
    with open('secretkey.txt','w') as f:
        f.write('14368749'+word+'57617867')
    with open('security_manager.txt','w') as t1:
        t1.write('Tool security manager : arsh/henry')
else:
    print('')
print(word)
with open('secretkey.txt','r') as f:
    encode1=f.read()
for momin in encode1[8:16]:
    temp3=lst2.index(momin)
    temp4=lst1[temp3]
    decoded=decoded+temp4
if not os.path.exists('approved.txt'):
    print(f'your code is : {encode1}\nask henry for key')
    inp=input('enter key : ')
    if inp[8:16]==decoded:
        with open('approved.txt','w') as f:
            f.write(inp)
        print('thanks for buying our tool, enjoy')
    else:    
        print('wrong key. pay henry for approve wp :- +91 9235741670')
        sys.exit()
else:
    with open('approved.txt','r') as f:
        approved=f.read()
    if approved[8:16]==decoded:
        print('success, Thanks for buying our tool\nHenry\'s tool')
    else:
        print('something got wrong, ask henry')
with open('security_manager.txt','r') as t45:
    t46=t45.read()
if t46!='Tool security manager : arsh/henry':
    print("don't change the credits of security manager\nwrite 'Tool security manager : arsh/henry' in security_manager.txt & remove the '' ")
    sys.exit()
print('hello world')
