#Created:Apr2022  TimeTaken:Approx1month
#Option to encrypt files was added on May2023 (uses same Adhrit style encryption) (originally it could just encrypt a sentence)
#AdhritTheGreat
import random
import base64
import time
import cryptocode
print(" ")
xoll=input("Encryptor / Decryptor : ")
time.sleep(1)
print(" ")
if ("e" in xoll.lower()) and ("n" in xoll.lower()) and ("d" not in xoll.lower()):
    a="aj"
    b="bj"
    c="cj"
    d="dj"
    e="ej"
    f="fj"
    g="gj"
    h="hj"
    i="ij"
    j="jj"
    k="kj"
    l="lj"
    m="mj"
    n="nj"
    o="oj"
    p="pj"
    q="qj"
    r="rj"
    s="sj"
    t="tj"
    u="uj"
    v="vj"
    w="wj"
    x="xj"
    y="yj"
    z="zj"
    zero=""
    one=""
    two=""
    three=""
    four=""
    five=""
    six=""
    seven=""
    eight=""
    nine=""
    pl="!"
    pp="@"
    pq="#"
    pr="&"
    pu="("
    pj=")"
    pf="/"
    pa="$"
    ps="+"
    pd="-"
    po="="
    pi="?"

    print("Advanced encryption activating....")

    time.sleep(5)
    print(" ")

    this=input("Encrypt a File/Sentence: ").lower()
    print(" ")
    if "fi" in this:
        #Everything in this if block was added on May2023
        time.sleep(5)
        path=input("Path of file: ")
        if not "//" in path:
            if "/" in path:
                path = path.replace('/', '//')
            if "\\" in path:
                path = path.replace("\\", '//')
        while True:
            if "." in path:
                type=path.split(".")[1]
                nam=path.split(".")[0]
                break
            else:
                print("Not a file")
        try:
            with open(path.strip(), 'rb') as file:
                file_data = file.read()
                worlookj=file_data
        except Exception as e:
            print("ERROR:",e)
        time.sleep(2)
        xacrt=["adbd","ajct","akno","popd","wjci","ncgf","jbfi","hfgi","nvhi","rivw","qobn","cogm","ondi","onll","psok","mjjk","odpl","neie","jsdi","baci","nfcs","kskio","jkbi","lomp","hvji","0893","1245","8903","9028","1120","8620","0029","7891","9753","5019","6930","7890","0389"]
        xlopik=random.choice(xacrt)
        def split(worlookj):
            return [char for char in worlookj]
        xppol=split(worlookj)
        numbrs=[">","@","*","~","#","-","|","!",")","$"]

        yiok=len(xppol)
        listop=""
        lok=[]
        lopkji=["1","2","3","4","5","6","7","8","9","€","£","₹"]
        xkio=0
        run_code=0
        bumml=["!",")","(","*","&","^","%","$","#","@"]
        lopko=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        let=[4,5,6]
        letfront=random.choice(let)
        letback=random.choice(let)
        letfron=letfront
        letbac=letback
        numfront=""
        numback=""
        while letfron!=0:
            klopil=random.choice(lopko)
            numfront=numfront+klopil
            letfron=letfron-1
        while letbac!=0:
            klopil=random.choice(lopko)
            numback=numback+klopil
            letbac=letbac-1




        tklop=1
        while tklop>0:
            if a=="aj":
                ka=a
                while True:
                    a=random.choice(lopko)
                    if (a!="a") and (a not in lok):
                        lok.append(a)
                        break
                    elif (a=="a") or (a in lok):
                        a=ka


            elif b=="bj":
                kb=b
                while True:
                    b=random.choice(lopko)
                    if (b!="b") and (b not in lok):
                        lok.append(b)
                        break
                    elif (b=="b") or (b in lok):
                        b=kb

            elif c=="cj":
                kc=c
                while True:
                    c=random.choice(lopko)
                    if (c!="c") and (c not in lok):
                        lok.append(c)
                        break
                    elif (c=="c") or (c in lok):
                        c=kc

            elif d=="dj":
                kd=d
                while True:
                    d=random.choice(lopko)
                    if (d!="d") and (d not in lok):
                        lok.append(d)
                        break
                    elif (d=="d") or (d in lok):
                        d=kd

            elif e=="ej":
                ke=e
                while True:
                    e=random.choice(lopko)
                    if (e!="e") and (e not in lok):
                        lok.append(e)
                        break
                    elif (e=="e") or (e in lok):
                        e=ke


            elif f=="fj":
                kf=f
                while True:
                    f=random.choice(lopko)
                    if (f!="f") and (f not in lok):
                        lok.append(f)
                        break
                    elif (f=="f") or (f in lok):
                        f=kf



            elif g=="gj":
                kg=g
                while True:
                    g=random.choice(lopko)
                    if (g!="g") and (g not in lok):
                        lok.append(g)
                        break
                    elif (g=="g") or (g in lok):
                        g=kg


            elif h=="hj":
                kh=h
                while True:
                    h=random.choice(lopko)
                    if (h!="h") and (h not in lok):
                        lok.append(h)
                        break
                    elif (h=="h") or (h in lok):
                        h=kh


            elif i=="ij":
                ki=i
                while True:
                    i=random.choice(lopko)
                    if (i!="i") and (i not in lok):
                        lok.append(i)
                        break
                    elif (i=="i") or (i in lok):
                        i=ki


            elif j=="jj":
                kj=j
                while True:
                    j=random.choice(lopko)
                    if (j!="j") and (j not in lok):
                        lok.append(j)
                        break
                    elif (j=="j") or (j in lok):
                        j=kj



            elif k=="kj":
                kk=k
                while True:
                    k=random.choice(lopko)
                    if (k!="k") and (k not in lok):
                        lok.append(k)
                        break
                    elif (k=="k") or (k in lok):
                        k=kk


            elif l=="lj":
                kl=l
                while True:
                    l=random.choice(lopko)
                    if (l!="l") and (l not in lok):
                        lok.append(l)
                        break
                    elif (l=="l") or (l in lok):
                        l=kl


            elif m=="mj":
                km=m
                while True:
                    m=random.choice(lopko)
                    if (m!="m") and (m not in lok):
                        lok.append(m)
                        break
                    elif (m=="m") or (m in lok):
                        m=km


            elif n=="nj":
                kn=n
                while True:
                    n=random.choice(lopko)
                    if (n!="n") and (n not in lok):
                        lok.append(n)
                        break
                    elif (n=="n") or (n in lok):
                        n=kn



            elif o=="oj":
                ko=o
                while True:
                    o=random.choice(lopko)
                    if (o!="o") and (o not in lok):
                        lok.append(o)
                        break
                    elif (o=="o") or (o in lok):
                        o=ko


            elif p=="pj":
                kp=p
                while True:
                    p=random.choice(lopko)
                    if (p!="p") and (p not in lok):
                        lok.append(p)
                        break
                    elif (p=="p") or (p in lok):
                        p=kp


            elif q=="qj":
                kq=q
                while True:
                    q=random.choice(lopko)
                    if (q!="q") and (q not in lok):
                        lok.append(q)
                        break
                    elif (q=="q") or (q in lok):
                        q=kq


            elif r=="rj":
                kr=r
                while True:
                    r=random.choice(lopko)
                    if (r!="r") and (r not in lok):
                        lok.append(r)
                        break
                    elif (r=="r") or (r in lok):
                        r=kr


            elif s=="sj":
                ks=s
                while True:
                    s=random.choice(lopko)
                    if (s!="s") and (s not in lok):
                        lok.append(s)
                        break
                    elif (s=="s") or (s in lok):
                        s=ks


            elif t=="tj":
                kt=t
                while True:
                    t=random.choice(lopko)
                    if (t!="t") and (t not in lok):
                        lok.append(t)
                        break
                    elif (t=="t") or (t in lok):
                        t=kt


            elif u=="uj":
                ku=u
                while True:
                    u=random.choice(lopko)
                    if (u!="u") and (u not in lok):
                        lok.append(u)
                        break
                    elif (u=="u") or (u in lok):
                        u=ku


            elif v=="vj":
                kv=v
                while True:
                    v=random.choice(lopko)
                    if (v!="v") and (v not in lok):
                        lok.append(v)
                        break
                    elif (v=="v") or (v in lok):
                        v=kv


            elif w=="wj":
                kw=w
                while True:
                    w=random.choice(lopko)
                    if (w!="w") and (w not in lok):
                        lok.append(w)
                        break
                    elif (w=="w") or (w in lok):
                        w=kw


            elif x=="xj":
                kx=x
                while True:
                    x=random.choice(lopko)
                    if (x!="x") and (x not in lok):
                        lok.append(x)
                        break
                    elif (x=="x") or (x in lok):
                        x=kx


            elif y=="yj":
                ky=y
                while True:
                    y=random.choice(lopko)
                    if (y!="y") and (y not in lok):
                        lok.append(y)
                        break
                    elif (y=="y") or (y in lok):
                        y=ky


            elif z=="zj":
                kz=z
                while True:
                    z=random.choice(lopko)
                    if (z!="z") and (z not in lok):
                        lok.append(z)
                        break
                    elif (z=="z") or (z in lok):
                        z=kz
            elif zero=="":
                zer=zero
                while True:
                    zero=random.choice(numbrs)
                    if (zero not in lok):
                        lok.append(zero)
                        break
                    elif (zero in lok):
                        zero=zer

            elif one=="":
                on=one
                while True:
                    one=random.choice(numbrs)
                    if (one not in lok):
                        lok.append(one)
                        break
                    elif (one in lok):
                        one=on

            elif two=="":
                tw=two
                while True:
                    two=random.choice(numbrs)
                    if (two not in lok):
                        lok.append(two)
                        break
                    elif (two in lok):
                        two=tw
            elif three=="":
                thre=three
                while True:
                    three=random.choice(numbrs)
                    if (three not in lok):
                        lok.append(three)
                        break
                    elif (three in lok):
                        three=thre
            elif four=="":
                fou=four
                while True:
                    four=random.choice(numbrs)
                    if (four not in lok):
                        lok.append(four)
                        break
                    elif (four in lok):
                        four=fou
            elif five=="":
                fiv=five
                while True:
                    five=random.choice(numbrs)
                    if (five not in lok):
                        lok.append(five)
                        break
                    elif (five in lok):
                        five=fiv
            elif six=="":
                si=six
                while True:
                    six=random.choice(numbrs)
                    if (six not in lok):
                        lok.append(six)
                        break
                    elif (six in lok):
                        six=si
            elif seven=="":
                seve=seven
                while True:
                    seven=random.choice(numbrs)
                    if (seven not in lok):
                        lok.append(seven)
                        break
                    elif (seven in lok):
                        seven=seve

            elif eight=="":
                eigh=eight
                while True:
                    eight=random.choice(numbrs)
                    if (eight not in lok):
                        lok.append(eight)
                        break
                    elif (eight in lok):
                        eight=eigh
            elif nine=="":
                nin=nine
                while True:
                    nine=random.choice(numbrs)
                    if (nine not in lok):
                        lok.append(nine)
                        break
                    elif (nine in lok):
                        nine=nin
            elif pp=="@":
                ppa=pp
                while True:
                    pp=random.choice(lopkji)
                    if (pp not in lok):
                        lok.append(pp)
                        break
                    elif (pp in lok):
                        pp=ppa
            elif pl=="!":
                pla=pl
                while True:
                    pl=random.choice(lopkji)
                    if (pl not in lok):
                        lok.append(pl)
                        break
                    elif (pl in lok):
                        pl=pla
            elif pq=="#":
                pqa=pq
                while True:
                    pq=random.choice(lopkji)
                    if (pq not in lok):
                        lok.append(pq)
                        break
                    elif (pq in lok):
                        pq=pqa
            elif pr=="&":
                pra=pr
                while True:
                    pr=random.choice(lopkji)
                    if (pr not in lok):
                        lok.append(pr)
                        break
                    elif (pr in lok):
                        pr=pra
            elif pu=="(":
                pua=pu
                while True:
                    pu=random.choice(lopkji)
                    if (pu not in lok):
                        lok.append(pu)
                        break
                    elif (pu in lok):
                        pu=pua
            elif pj==")":
                pja=pj
                while True:
                    pj=random.choice(lopkji)
                    if (pj not in lok):
                        lok.append(pj)
                        break
                    elif (pj in lok):
                        pj=pja
            elif pa=="$":
                paa=pa
                while True:
                    pa=random.choice(lopkji)
                    if (pa not in lok):
                        lok.append(pa)
                        break
                    elif (pa in lok):
                        pa=paa
            elif ps=="+":
                psa=ps
                while True:
                    ps=random.choice(lopkji)
                    if (ps not in lok):
                        lok.append(ps)
                        break
                    elif (ps in lok):
                        ps=psa
            elif pd=="-":
                pda=pd
                while True:
                    pd=random.choice(lopkji)
                    if (pd not in lok):
                        lok.append(pd)
                        break
                    elif (pd in lok):
                        pd=pda
            elif po=="=":
                poa=po
                while True:
                    po=random.choice(lopkji)
                    if (po not in lok):
                        lok.append(po)
                        break
                    elif (po in lok):
                        po=poa
            elif pi=="?":
                pia=pi
                while True:
                    pi=random.choice(lopkji)
                    if (pi not in lok):
                        lok.append(pi)
                        break
                    elif (pi in lok):
                        pi=pia
            elif pf=="/":
                pfa=pf
                while True:
                    pf=random.choice(lopkji)
                    if (pf not in lok):
                        lok.append(pf)
                        break
                    elif (pf in lok):
                        pf=pfa
            elif (a!="aj") and (b!="bj") and (c!="cj") and (d!="dj") and (e!="ej") and (f!="fj") and (g!="gj") and (h!="hj") and (i!="ij") and (j!="jj") and (k!="kj") and (l!="lj") and (m!="mj") and (n!="nj") and (o!="oj") and (p!="pj") and (q!="qj") and (r!="rj") and (s!="sj") and (t!="tj") and (u!="uj") and (v!="vj") and (w!="wj") and (x!="xj") and (y!="yj") and (z!="zj"):
                time.sleep(1)
                print(" ")
                print("Collecting letters....")
                time.sleep(3)
                print(" ")
                print("Adding salt....")
                print(" ")
                time.sleep(3)
                print("Starting encryption....")
                print(" ")
                time.sleep(3)
                tklop=tklop-1
        num=0
        for char in xppol:
            num=num+1
        now=0
        for char in xppol:
            now=now+1
            if now>1:
                char=str(char)
                xo=now/num*100
                print(xo,"%")
                if char.lower()=="a":
                    listop=listop+a
                elif char.lower()=="b":
                    listop=listop+b
                elif char.lower()=="c":
                    listop=listop+c
                elif char.lower()=="d":
                    listop=listop+d
                elif char.lower()=="e":
                    listop=listop+e
                elif char.lower()=="f":
                    listop=listop+f
                elif char.lower()=="g":
                    listop=listop+g
                elif char.lower()=="h":
                    listop=listop+h
                elif char.lower()=="i":
                    listop=listop+i
                elif char.lower()=="j":
                    listop=listop+j
                elif char.lower()=="k":
                    listop=listop+k
                elif char.lower()=="l":
                    listop=listop+l
                elif char.lower()=="m":
                    listop=listop+m
                elif char.lower()==" ":
                    listop=listop+"/"
                elif char.lower()=="n":
                    listop=listop+n
                elif char.lower()=="o":
                    listop=listop+o
                elif char.lower()=="p":
                    listop=listop+p
                elif char.lower()=="q":
                    listop=listop+q
                elif char.lower()=="r":
                    listop=listop+r
                elif char.lower()=="s":
                    listop=listop+s
                elif char.lower()=="t":
                    listop=listop+t
                elif char.lower()=="u":
                    listop=listop+u
                elif char.lower()=="v":
                    listop=listop+v
                elif char.lower()=="w":
                    listop=listop+w
                elif char.lower()=="x":
                    listop=listop+x
                elif char.lower()=="y":
                    listop=listop+y
                elif char.lower()=="z":
                    listop=listop+z
                elif char.lower()=="0":
                    listop=listop+zero
                elif char.lower()=="1":
                    listop=listop+one
                elif char.lower()=="2":
                    listop=listop+two
                elif char.lower()=="3":
                    listop=listop+three
                elif char.lower()=="4":
                    listop=listop+four
                elif char.lower()=="5":
                    listop=listop+five
                elif char.lower()=="6":
                    listop=listop+six
                elif char.lower()=="7":
                    listop=listop+seven
                elif char.lower()=="8":
                    listop=listop+eight
                elif char.lower()=="9":
                    listop=listop+nine
                elif char.lower()=="!":
                    listop=listop+pl
                elif char.lower()=="@":
                    listop=listop+pp
                elif char.lower()=="#":
                    listop=listop+pq
                elif char.lower()=="&":
                    listop=listop+pr
                elif char.lower()=="(":
                    listop=listop+pu
                elif char.lower()==")":
                    listop=listop+pj
                elif char.lower()=="$":
                    listop=listop+pa
                elif char.lower()=="+":
                    listop=listop+ps
                elif char.lower()=="-":
                    listop=listop+pd
                elif char.lower()=="=":
                    listop=listop+po
                elif char.lower()=="?":
                    listop=listop+pi
                else:
                    listop=listop+char.lower()
                print(listop)
        xyza=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
        flubbero=""
        print(listop)
        listop=numfront+listop+numback

        while len(flubbero)<10:
            xyzb=random.choice(xyza)
            flubbero=flubbero+xyzb
        chubb=listop
        str_encoded = cryptocode.encrypt(chubb,flubbero)
        listop=str_encoded
        xopli=20598376985367568756956548765489675976539868450445687456985769846909698595886958596869869696909698595886958596869869696
        print(" ")
        print(" ")
        while xopli>0:
            xopli=xopli-5999999999999000939479890435886745986750679858679487696568969096985958869585968698696969096985958869585968698696969
            print(xopli, end="\r")
            xopli=xopli+100009869578968
            print(xopli, end="\r")
        print(" ")
        xkolpil=35
        while xkolpil>0:
            print(" ")
            xkolpil=xkolpil-1
        time.sleep(0.5)
        print("Writing encrypted file....")
        with open(path.strip(), 'wb') as encrypted_file:
            encrypted_file.write(listop)
        time.sleep(2)
        print("Done :)")
        time.sleep(3)
        print(" ")
        print("Preparing decryption code....")
        print(" ")
        time.sleep(3)
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")

        time.sleep(0.5)
        print(xopolo)
        letfront=str(letfront)
        letback=str(letback)
        decrypc=a+n+b+o+c+p+d+q+e+r+f+s+g+t+h+u+i+v+j+w+k+x+l+y+m+z+zero+nine+seven+two+eight+one+three+six+four+five+pl+pp+pq+pr+pu+pj+pa+ps+pd+po+pi+pf+flubbero+letfront+letback

        time.sleep(1)
        print(" ")
        time.sleep(1)
        decryk=" Decryption code:   "+decrypc
        time.sleep(0.5)
        print(decryk)
        if run_code>0:
            time.sleep(0.5)
            print(" ")
            print(" ")
            print(" ")
            print("Run code error:",run_code)
            time.sleep(0.5)
            print("An error has been encountered and our your sentence might be incorrectly encrypted, please delete your sentence and retry.")
            time.sleep(0.5)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)



        else:
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            time.sleep(1)
            print("If you want to decrypt this, go to the decryptor, enter the encrypted sentence and then enter the decryption code")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")


    else:
        #Everything in this else block is all original code (not modified at all)
        time.sleep(3)
        worlookj=input("Enter the text you want to encrypt: ")
        time.sleep(2)
        xacrt=["adbd","ajct","akno","popd","wjci","ncgf","jbfi","hfgi","nvhi","rivw","qobn","cogm","ondi","onll","psok","mjjk","odpl","neie","jsdi","baci","nfcs","kskio","jkbi","lomp","hvji","0893","1245","8903","9028","1120","8620","0029","7891","9753","5019","6930","7890","0389"]
        xlopik=random.choice(xacrt)
        def split(worlookj):
            return [char for char in worlookj]
        xppol=split(worlookj)
        numbrs=[">","@","*","~","#","-","|","!",")","$"]

        yiok=len(xppol)
        listop=""
        lok=[]
        lopkji=["1","2","3","4","5","6","7","8","9","€","£","₹"]
        xkio=0
        run_code=0
        bumml=["!",")","(","*","&","^","%","$","#","@"]
        lopko=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        let=[4,5,6]
        letfront=random.choice(let)
        letback=random.choice(let)
        letfron=letfront
        letbac=letback
        numfront=""
        numback=""
        while letfron!=0:
            klopil=random.choice(lopko)
            numfront=numfront+klopil
            letfron=letfron-1
        while letbac!=0:
            klopil=random.choice(lopko)
            numback=numback+klopil
            letbac=letbac-1




        tklop=1
        while tklop>0:
            if a=="aj":
                ka=a
                while True:
                    a=random.choice(lopko)
                    if (a!="a") and (a not in lok):
                        lok.append(a)
                        break
                    elif (a=="a") or (a in lok):
                        a=ka


            elif b=="bj":
                kb=b
                while True:
                    b=random.choice(lopko)
                    if (b!="b") and (b not in lok):
                        lok.append(b)
                        break
                    elif (b=="b") or (b in lok):
                        b=kb

            elif c=="cj":
                kc=c
                while True:
                    c=random.choice(lopko)
                    if (c!="c") and (c not in lok):
                        lok.append(c)
                        break
                    elif (c=="c") or (c in lok):
                        c=kc

            elif d=="dj":
                kd=d
                while True:
                    d=random.choice(lopko)
                    if (d!="d") and (d not in lok):
                        lok.append(d)
                        break
                    elif (d=="d") or (d in lok):
                        d=kd

            elif e=="ej":
                ke=e
                while True:
                    e=random.choice(lopko)
                    if (e!="e") and (e not in lok):
                        lok.append(e)
                        break
                    elif (e=="e") or (e in lok):
                        e=ke


            elif f=="fj":
                kf=f
                while True:
                    f=random.choice(lopko)
                    if (f!="f") and (f not in lok):
                        lok.append(f)
                        break
                    elif (f=="f") or (f in lok):
                        f=kf



            elif g=="gj":
                kg=g
                while True:
                    g=random.choice(lopko)
                    if (g!="g") and (g not in lok):
                        lok.append(g)
                        break
                    elif (g=="g") or (g in lok):
                        g=kg


            elif h=="hj":
                kh=h
                while True:
                    h=random.choice(lopko)
                    if (h!="h") and (h not in lok):
                        lok.append(h)
                        break
                    elif (h=="h") or (h in lok):
                        h=kh


            elif i=="ij":
                ki=i
                while True:
                    i=random.choice(lopko)
                    if (i!="i") and (i not in lok):
                        lok.append(i)
                        break
                    elif (i=="i") or (i in lok):
                        i=ki


            elif j=="jj":
                kj=j
                while True:
                    j=random.choice(lopko)
                    if (j!="j") and (j not in lok):
                        lok.append(j)
                        break
                    elif (j=="j") or (j in lok):
                        j=kj



            elif k=="kj":
                kk=k
                while True:
                    k=random.choice(lopko)
                    if (k!="k") and (k not in lok):
                        lok.append(k)
                        break
                    elif (k=="k") or (k in lok):
                        k=kk


            elif l=="lj":
                kl=l
                while True:
                    l=random.choice(lopko)
                    if (l!="l") and (l not in lok):
                        lok.append(l)
                        break
                    elif (l=="l") or (l in lok):
                        l=kl


            elif m=="mj":
                km=m
                while True:
                    m=random.choice(lopko)
                    if (m!="m") and (m not in lok):
                        lok.append(m)
                        break
                    elif (m=="m") or (m in lok):
                        m=km


            elif n=="nj":
                kn=n
                while True:
                    n=random.choice(lopko)
                    if (n!="n") and (n not in lok):
                        lok.append(n)
                        break
                    elif (n=="n") or (n in lok):
                        n=kn



            elif o=="oj":
                ko=o
                while True:
                    o=random.choice(lopko)
                    if (o!="o") and (o not in lok):
                        lok.append(o)
                        break
                    elif (o=="o") or (o in lok):
                        o=ko


            elif p=="pj":
                kp=p
                while True:
                    p=random.choice(lopko)
                    if (p!="p") and (p not in lok):
                        lok.append(p)
                        break
                    elif (p=="p") or (p in lok):
                        p=kp


            elif q=="qj":
                kq=q
                while True:
                    q=random.choice(lopko)
                    if (q!="q") and (q not in lok):
                        lok.append(q)
                        break
                    elif (q=="q") or (q in lok):
                        q=kq


            elif r=="rj":
                kr=r
                while True:
                    r=random.choice(lopko)
                    if (r!="r") and (r not in lok):
                        lok.append(r)
                        break
                    elif (r=="r") or (r in lok):
                        r=kr


            elif s=="sj":
                ks=s
                while True:
                    s=random.choice(lopko)
                    if (s!="s") and (s not in lok):
                        lok.append(s)
                        break
                    elif (s=="s") or (s in lok):
                        s=ks


            elif t=="tj":
                kt=t
                while True:
                    t=random.choice(lopko)
                    if (t!="t") and (t not in lok):
                        lok.append(t)
                        break
                    elif (t=="t") or (t in lok):
                        t=kt


            elif u=="uj":
                ku=u
                while True:
                    u=random.choice(lopko)
                    if (u!="u") and (u not in lok):
                        lok.append(u)
                        break
                    elif (u=="u") or (u in lok):
                        u=ku


            elif v=="vj":
                kv=v
                while True:
                    v=random.choice(lopko)
                    if (v!="v") and (v not in lok):
                        lok.append(v)
                        break
                    elif (v=="v") or (v in lok):
                        v=kv


            elif w=="wj":
                kw=w
                while True:
                    w=random.choice(lopko)
                    if (w!="w") and (w not in lok):
                        lok.append(w)
                        break
                    elif (w=="w") or (w in lok):
                        w=kw


            elif x=="xj":
                kx=x
                while True:
                    x=random.choice(lopko)
                    if (x!="x") and (x not in lok):
                        lok.append(x)
                        break
                    elif (x=="x") or (x in lok):
                        x=kx


            elif y=="yj":
                ky=y
                while True:
                    y=random.choice(lopko)
                    if (y!="y") and (y not in lok):
                        lok.append(y)
                        break
                    elif (y=="y") or (y in lok):
                        y=ky


            elif z=="zj":
                kz=z
                while True:
                    z=random.choice(lopko)
                    if (z!="z") and (z not in lok):
                        lok.append(z)
                        break
                    elif (z=="z") or (z in lok):
                        z=kz
            elif zero=="":
                zer=zero
                while True:
                    zero=random.choice(numbrs)
                    if (zero not in lok):
                        lok.append(zero)
                        break
                    elif (zero in lok):
                        zero=zer

            elif one=="":
                on=one
                while True:
                    one=random.choice(numbrs)
                    if (one not in lok):
                        lok.append(one)
                        break
                    elif (one in lok):
                        one=on

            elif two=="":
                tw=two
                while True:
                    two=random.choice(numbrs)
                    if (two not in lok):
                        lok.append(two)
                        break
                    elif (two in lok):
                        two=tw
            elif three=="":
                thre=three
                while True:
                    three=random.choice(numbrs)
                    if (three not in lok):
                        lok.append(three)
                        break
                    elif (three in lok):
                        three=thre
            elif four=="":
                fou=four
                while True:
                    four=random.choice(numbrs)
                    if (four not in lok):
                        lok.append(four)
                        break
                    elif (four in lok):
                        four=fou
            elif five=="":
                fiv=five
                while True:
                    five=random.choice(numbrs)
                    if (five not in lok):
                        lok.append(five)
                        break
                    elif (five in lok):
                        five=fiv
            elif six=="":
                si=six
                while True:
                    six=random.choice(numbrs)
                    if (six not in lok):
                        lok.append(six)
                        break
                    elif (six in lok):
                        six=si
            elif seven=="":
                seve=seven
                while True:
                    seven=random.choice(numbrs)
                    if (seven not in lok):
                        lok.append(seven)
                        break
                    elif (seven in lok):
                        seven=seve

            elif eight=="":
                eigh=eight
                while True:
                    eight=random.choice(numbrs)
                    if (eight not in lok):
                        lok.append(eight)
                        break
                    elif (eight in lok):
                        eight=eigh
            elif nine=="":
                nin=nine
                while True:
                    nine=random.choice(numbrs)
                    if (nine not in lok):
                        lok.append(nine)
                        break
                    elif (nine in lok):
                        nine=nin
            elif pp=="@":
                ppa=pp
                while True:
                    pp=random.choice(lopkji)
                    if (pp not in lok):
                        lok.append(pp)
                        break
                    elif (pp in lok):
                        pp=ppa
            elif pl=="!":
                pla=pl
                while True:
                    pl=random.choice(lopkji)
                    if (pl not in lok):
                        lok.append(pl)
                        break
                    elif (pl in lok):
                        pl=pla
            elif pq=="#":
                pqa=pq
                while True:
                    pq=random.choice(lopkji)
                    if (pq not in lok):
                        lok.append(pq)
                        break
                    elif (pq in lok):
                        pq=pqa
            elif pr=="&":
                pra=pr
                while True:
                    pr=random.choice(lopkji)
                    if (pr not in lok):
                        lok.append(pr)
                        break
                    elif (pr in lok):
                        pr=pra
            elif pu=="(":
                pua=pu
                while True:
                    pu=random.choice(lopkji)
                    if (pu not in lok):
                        lok.append(pu)
                        break
                    elif (pu in lok):
                        pu=pua
            elif pj==")":
                pja=pj
                while True:
                    pj=random.choice(lopkji)
                    if (pj not in lok):
                        lok.append(pj)
                        break
                    elif (pj in lok):
                        pj=pja
            elif pa=="$":
                paa=pa
                while True:
                    pa=random.choice(lopkji)
                    if (pa not in lok):
                        lok.append(pa)
                        break
                    elif (pa in lok):
                        pa=paa
            elif ps=="+":
                psa=ps
                while True:
                    ps=random.choice(lopkji)
                    if (ps not in lok):
                        lok.append(ps)
                        break
                    elif (ps in lok):
                        ps=psa
            elif pd=="-":
                pda=pd
                while True:
                    pd=random.choice(lopkji)
                    if (pd not in lok):
                        lok.append(pd)
                        break
                    elif (pd in lok):
                        pd=pda
            elif po=="=":
                poa=po
                while True:
                    po=random.choice(lopkji)
                    if (po not in lok):
                        lok.append(po)
                        break
                    elif (po in lok):
                        po=poa
            elif pi=="?":
                pia=pi
                while True:
                    pi=random.choice(lopkji)
                    if (pi not in lok):
                        lok.append(pi)
                        break
                    elif (pi in lok):
                        pi=pia
            elif pf=="/":
                pfa=pf
                while True:
                    pf=random.choice(lopkji)
                    if (pf not in lok):
                        lok.append(pf)
                        break
                    elif (pf in lok):
                        pf=pfa
            elif (a!="aj") and (b!="bj") and (c!="cj") and (d!="dj") and (e!="ej") and (f!="fj") and (g!="gj") and (h!="hj") and (i!="ij") and (j!="jj") and (k!="kj") and (l!="lj") and (m!="mj") and (n!="nj") and (o!="oj") and (p!="pj") and (q!="qj") and (r!="rj") and (s!="sj") and (t!="tj") and (u!="uj") and (v!="vj") and (w!="wj") and (x!="xj") and (y!="yj") and (z!="zj"):
                time.sleep(1)
                print(" ")
                print("Collecting letters....")
                time.sleep(3)
                print(" ")
                print("Adding salt....")
                print(" ")
                time.sleep(3)
                print("Starting encryption....")
                print(" ")
                time.sleep(3)
                tklop=tklop-1

        for char in xppol:
                char=str(char)
                if char.lower()=="a":
                    listop=listop+a
                elif char.lower()=="b":
                    listop=listop+b
                elif char.lower()=="c":
                    listop=listop+c
                elif char.lower()=="d":
                    listop=listop+d
                elif char.lower()=="e":
                    listop=listop+e
                elif char.lower()=="f":
                    listop=listop+f
                elif char.lower()=="g":
                    listop=listop+g
                elif char.lower()=="h":
                    listop=listop+h
                elif char.lower()=="i":
                    listop=listop+i
                elif char.lower()=="j":
                    listop=listop+j
                elif char.lower()=="k":
                    listop=listop+k
                elif char.lower()=="l":
                    listop=listop+l
                elif char.lower()=="m":
                    listop=listop+m
                elif char.lower()==" ":
                    listop=listop+"/"
                elif char.lower()=="n":
                    listop=listop+n
                elif char.lower()=="o":
                    listop=listop+o
                elif char.lower()=="p":
                    listop=listop+p
                elif char.lower()=="q":
                    listop=listop+q
                elif char.lower()=="r":
                    listop=listop+r
                elif char.lower()=="s":
                    listop=listop+s
                elif char.lower()=="t":
                    listop=listop+t
                elif char.lower()=="u":
                    listop=listop+u
                elif char.lower()=="v":
                    listop=listop+v
                elif char.lower()=="w":
                    listop=listop+w
                elif char.lower()=="x":
                    listop=listop+x
                elif char.lower()=="y":
                    listop=listop+y
                elif char.lower()=="z":
                    listop=listop+z
                elif char.lower()=="0":
                    listop=listop+zero
                elif char.lower()=="1":
                    listop=listop+one
                elif char.lower()=="2":
                    listop=listop+two
                elif char.lower()=="3":
                    listop=listop+three
                elif char.lower()=="4":
                    listop=listop+four
                elif char.lower()=="5":
                    listop=listop+five
                elif char.lower()=="6":
                    listop=listop+six
                elif char.lower()=="7":
                    listop=listop+seven
                elif char.lower()=="8":
                    listop=listop+eight
                elif char.lower()=="9":
                    listop=listop+nine
                elif char.lower()=="!":
                    listop=listop+pl
                elif char.lower()=="@":
                    listop=listop+pp
                elif char.lower()=="#":
                    listop=listop+pq
                elif char.lower()=="&":
                    listop=listop+pr
                elif char.lower()=="(":
                    listop=listop+pu
                elif char.lower()==")":
                    listop=listop+pj
                elif char.lower()=="$":
                    listop=listop+pa
                elif char.lower()=="+":
                    listop=listop+ps
                elif char.lower()=="-":
                    listop=listop+pd
                elif char.lower()=="=":
                    listop=listop+po
                elif char.lower()=="?":
                    listop=listop+pi
        xyza=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
        flubbero=""

        listop=numfront+listop+numback

        while len(flubbero)<10:
            xyzb=random.choice(xyza)
            flubbero=flubbero+xyzb
        chubb=listop
        str_encoded = cryptocode.encrypt(chubb,flubbero)
        listop=str_encoded
        xopli=20598376985367568756956548765489675976539868450445687456985769846909698595886958596869869696909698595886958596869869696
        print(" ")
        print(" ")
        while xopli>0:
            xopli=xopli-5999999999999000939479890435886745986750679858679487696568969096985958869585968698696969096985958869585968698696969
            print(xopli, end="\r")
            xopli=xopli+100009869578968
            print(xopli, end="\r")
        print(" ")
        xkolpil=35
        while xkolpil>0:
            print(" ")
            xkolpil=xkolpil-1
        time.sleep(0.5)
        print("Preparing encrypted sentence....")
        time.sleep(3)
        print(" ")
        print("Preparing decryption code....")
        print(" ")
        time.sleep(3)
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        xopolo=' Encrypted sentence: '+listop
        time.sleep(0.5)
        print(xopolo)
        letfront=str(letfront)
        letback=str(letback)
        decrypc=a+n+b+o+c+p+d+q+e+r+f+s+g+t+h+u+i+v+j+w+k+x+l+y+m+z+zero+nine+seven+two+eight+one+three+six+four+five+pl+pp+pq+pr+pu+pj+pa+ps+pd+po+pi+pf+flubbero+letfront+letback

        time.sleep(1)
        print(" ")
        time.sleep(1)
        decryk=" Decryption code:   "+decrypc
        time.sleep(0.5)
        print(decryk)
        if run_code>0:
            time.sleep(0.5)
            print(" ")
            print(" ")
            print(" ")
            print("Run code error:",run_code)
            time.sleep(0.5)
            print("An error has been encountered and our your sentence might be incorrectly encrypted, please delete your sentence and retry.")
            time.sleep(0.5)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)
            time.sleep(9)



        else:
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            time.sleep(1)
            print("If you want to decrypt this, go to the decryptor, enter the encrypted sentence and then enter the decryption code")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")

        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)

elif ("d" in xoll.lower()) and ("e" in xoll.lower()) and ("n" not in xoll.lower()):
    time.sleep(1)
    print("Advanced decryption activated")
    def split(sent):
        return [char for char in sent]
    while True:
        time.sleep(1)
        print(" ")
        depil=input("Enter your decryption code: ")
        depil=depil.strip()
        if (len(depil)>59) and (len(depil)<61):
            time.sleep(0.5)
            print(" ")
            print("Checking......")
            time.sleep(2)
            break
        else:
            time.sleep(0.5)
            print(" ")
            print("Retry :(")
            time.sleep(0.5)



    fop=depil
    a=fop[0]
    n=fop[1]
    b=fop[2]
    o=fop[3]
    c=fop[4]
    p=fop[5]
    d=fop[6]
    q=fop[7]
    e=fop[8]
    r=fop[9]
    f=fop[10]
    s=fop[11]
    g=fop[12]
    t=fop[13]
    h=fop[14]
    u=fop[15]
    i=fop[16]
    v=fop[17]
    j=fop[18]
    w=fop[19]
    k=fop[20]
    x=fop[21]
    l=fop[22]
    y=fop[23]
    m=fop[24]
    z=fop[25]
    zero=fop[26]
    nine=fop[27]
    seven=fop[28]
    two=fop[29]
    eight=fop[30]
    one=fop[31]
    three=fop[32]
    six=fop[33]
    four=fop[34]
    five=fop[35]
    pl=fop[36]
    pp=fop[37]
    pq=fop[38]
    pr=fop[39]
    pu=fop[40]
    pj=fop[41]
    pa=fop[42]
    ps=fop[43]
    pd=fop[44]
    po=fop[45]
    pi=fop[46]
    pf=fop[47]


    ar=fop[48]
    br=fop[49]
    cr=fop[50]
    dr=fop[51]
    er=fop[52]
    fr=fop[53]
    gr=fop[54]
    hr=fop[55]
    ir=fop[56]
    jr=fop[57]


    salta=fop[58]
    saltb=fop[59]


    time.sleep(0.5)
    print(" ")
    print("Unpacking decryption code....")
    time.sleep(0.5)
    time.sleep(3)
    flubbero=ar+br+cr+dr+er+fr+gr+hr+ir+jr
    print(" ")
    sent=input("Enter the encrypted sentence: ")
    time.sleep(0.5)
    depil=sent.strip()
    time.sleep(0.5)
    time.sleep(1)


    str_=depil.strip()
    print(" ")
    print("Collecting decryption package....")
    time.sleep(3)
    print(" ")
    print("Decryption starting....")
    print(" ")
    _decoded = cryptocode.decrypt(str_, flubbero)
    sent=_decoded
    xppol=split(sent)
    listop=""
    for char in xppol:
        char=str(char)
        if char==a:
            listop=listop+"a"
        elif char==b:
            listop=listop+"b"
        elif char==c:
            listop=listop+"c"
        elif char==d:
            listop=listop+"d"
        elif char==e:
            listop=listop+"e"
        elif char==f:
            listop=listop+"f"
        elif char==g:
            listop=listop+"g"
        elif char==h:
            listop=listop+"h"
        elif char==i:
            listop=listop+"i"
        elif char=="/":
            listop=listop+" "
        elif char==j:
            listop=listop+"j"
        elif char==k:
            listop=listop+"k"
        elif char==l:
            listop=listop+"l"
        elif char==m:
            listop=listop+"m"
        elif char==n:
            listop=listop+"n"
        elif char==o:
            listop=listop+"o"
        elif char==p:
            listop=listop+"p"
        elif char==q:
            listop=listop+"q"
        elif char==r:
            listop=listop+"r"
        elif char==s:
            listop=listop+"s"
        elif char==t:
            listop=listop+"t"
        elif char==u:
            listop=listop+"u"
        elif char==v:
            listop=listop+"v"
        elif char==w:
            listop=listop+"w"
        elif char==x:
            listop=listop+"x"
        elif char==y:
            listop=listop+"y"
        elif char==z:
            listop=listop+"z"
        elif char==zero:
            listop=listop+"0"
        elif char==one:
            listop=listop+"1"
        elif char==two:
            listop=listop+"2"
        elif char==three:
            listop=listop+"3"
        elif char==four:
            listop=listop+"4"
        elif char==five:
            listop=listop+"5"
        elif char==six:
            listop=listop+"6"
        elif char==seven:
            listop=listop+"7"
        elif char==eight:
            listop=listop+"8"
        elif char==nine:
            listop=listop+"9"
        elif char==pl:
            listop=listop+"!"
        elif char==pp:
            listop=listop+"@"
        elif char==pq:
            listop=listop+"#"
        elif char==pr:
            listop=listop+"&"
        elif char==pu:
            listop=listop+"("
        elif char==pj:
            listop=listop+")"
        elif char==pa:
            listop=listop+"$"
        elif char==ps:
            listop=listop+"+"
        elif char==pd:
            listop=listop+"-"
        elif char==po:
            listop=listop+"="
        elif char==pi:
            listop=listop+"?"
        elif char==pf:
            listop=listop+"/"
        else:
            listop=listop+char

    size = len(listop)
    xxaq=saltb
    xxaq=int(xxaq)
    salta=int(salta)
    listop=listop[salta:]
    listop=listop[:- xxaq]

    xopli=20598376985367568756956548765489675976539868450445687456985769846909698595886958596869869696909698595886958596869869696
    while xopli>0:
        xopli=xopli-5999999999999000939479890435886745986750679858679487696568969096985958869585968698696969096985958869585968698696969
        print(xopli, end="\r")
        xopli=xopli+100009869578968
        print(xopli, end="\r")
    xkolpil=20
    time.sleep(2)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    time.sleep(0.5)
    print("Removing salt....")
    time.sleep(2)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("Preparing decrypted sentence....")
    time.sleep(7)
    while xkolpil>0:
        print(" ")
        xkolpil=xkolpil-1
    time.sleep(2)

    xolopo='Decrypted sentence:   '+listop
    print(xolopo)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    time.sleep(9)
    time.sleep(9)
    time.sleep(9)
    time.sleep(9)
    time.sleep(9)
    time.sleep(9)
    time.sleep(9)
    time.sleep(9)
else:
    print("Nothing called",xoll)
    time.sleep(9)
    time.sleep(9)
    time.sleep(9)
    time.sleep(9)
