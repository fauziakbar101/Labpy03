print('Nama : Fauziakbar')
print('Nim  : 311810855')
print('PROGRAM MENAMPILKAN N BILANGAN ACAK LEBIH < 0.5')
print('')

import random

n = int(input("Masukan nilai N : "))
for i in range(n) :
    a=random.uniform(0.0,0.5)
    print ("Data ke : ", i, "=> ", a)
    
print("Selesai")
