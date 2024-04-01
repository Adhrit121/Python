import cryptocode
import time
import random
here=input("enc/dec: ")
if here=="enc":
    xyza=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
    flubbero=""
    while len(flubbero)<10:
        xyzb=random.choice(xyza)
        flubbero=flubbero+xyzb
    chubb=input("Your Sentence:")
    str_encoded = cryptocode.encrypt(chubb,flubbero)
    print("Key:",flubbero)
    print("encoded:",str_encoded)
else:
    flubbero=input("Key:")
    str_=input("Sentence:")
    str_decoded = cryptocode.decrypt(str_, flubbero)
    print(str_decoded)
