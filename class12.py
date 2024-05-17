list=[1,2,3,4,5]
for element in list:
    print(element)
   #or print(list[2])
   #suma: print(list[2]+list[4])


list=[1,2,3,4,5]
list.append(6)
for element in list:
    print(element)


list=[1,2,3,4,5,6,7,8,9]
list.append(list[4]+list[5])
list.append(list[2]+list[6])
for element in list:
    print(element)


import random
n=random.randint(0,100)
n2=random.randint(0,100)
list=[1,2,3,4,5,6,7,8,9]
list.append(list[4]+list[5])
list.append(list[2]+list[6])
for element in list:
    print(element)

import random  
bing=[22,23,24,25,26]
comodin=random.randint(10,99)
bing.append(comodin)
if comodin in bing:
    print("Nuevo comodin :)")
    comodin=random.randint(10,99)
for num in bing:
    print(num)