import numpy as np
pt=input("enter plain txt :")
key=input("enter key :")
pt=pt.lower()
key=key.lower()
key=np.array([ord(b)-97 for b in key])
pt=np.array([ord(a)-97 for a in pt])
if len(key)==4:
    size=2
    keym=key.reshape(2,2)
if len(key)==9:
    size=3
    keym=key.reshape(3,3)
print(pt)
ptm=np.array_split(pt,len(pt)/size)
print("encryption is :")
b=""
for a in ptm:
    a = a.reshape(size,1)
    encr = np.dot(keym,a)%26
    for a in np.nditer(encr):
        b+=chr(a+97)
        print(chr(a+97),end="")

adj = np.linalg.inv(keym)
det = round(np.linalg.det(keym))

adj = (adj * det)%26
np.set_printoptions(suppress=True)
det= det%26

x = 1
while((det*x)%26 != 1): 
    x += 1 
final = (x * adj)%26
print("inverse: ",final)
print("decrypted text is: ")
b=np.array([ord(a)-97 for a in b])
encm = np.array_split(b, len(b)/size)
for a in encm:
    a = a.reshape(size,1)
    decr = np.round(np.dot(final, a))
    decr = decr.astype(int)
    decr = decr%26
    for a in np.nditer(decr):
        print(chr(a+97), end = "")