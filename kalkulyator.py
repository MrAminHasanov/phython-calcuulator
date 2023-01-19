import math
def sin(b):return round(math.sin(math.radians(b)),2)
def cos(b):return round(math.cos(math.radians(b)),2)
def tan(b):return round(math.tan(math.radians(b)),2)
def cotng(b):return round(math.cotng(math.radians(b)),2)
def fac(b):
    c=1
    for i in range(1,int(b)+1):c*=i
    return c
def vic(a):
    def tr(d,b):
        if  a[d]=='(':return vic(a[d+1:b])
        elif a[d]=="!":return fac(vic(a[d+2:b]))
        elif a[d]=="s":return sin(vic(a[d+4:b])) 
        elif a[d]=="c":return cos(vic(a[d+4:b]))
        elif a[d]=="t":return tan(vic(a[d+3:b]))
        elif a[d]=="k":return cotng(vic(a[d+4:b]))
        else:return float(a[d:b+1])
    d=[]
    m=0
    nn=0
    n=[0]
    q=0
    p=["+","-",'*','/']
    k=len(p)
    for i in range(len(a)):
        aa=0
        if q==0:
            for j in range(k):
                if a[i]==p[j]:
                    aa=1
        else:
            if a[i]=="(":m+=1
            elif a[i]==")":nn+=1
            if m==nn:
                m=0
                nn=0
                q=0
                if i!=(len(a)-1) and i!=0:n.append(i)
        if a[i]=="(" and m==0:
            q=1
            m+=1
        if aa==1:
            d.append(a[i])
            if a[i-1]!=")":n.append(i-1)
    n.append(len(a)-1)
    l=tr(n[0],n[1])
    for i in range(len(d)):
        if d[i]=='+':l=l+tr((n[i+1]+2),n[i+2])
        elif d[i]=='-':l=l-tr((n[i+1]+2),n[i+2])
        elif d[i]=='*':l=l*tr((n[i+1]+2),n[i+2])
        elif d[i]=='/':l=l/tr((n[i+1]+2),n[i+2])     
    return float(l)
a=''
print("доступные операци {+,-,*,/,sin(),cos(),tg(),ctg(),!,()}\nИнструкция умножения проводить в скобках (пример:2+(2*5))так же факториял тоже в скобках (пример:!(5))\nТригонометрические функции sin(a);cos(a);tg(a);ktg(a)\nдля работа с паматью или что бы останавить програму нажмите Enter\n")
b='g'
while True: 
    b=a
    a+=input(a)
    if a==b:
        k=input("введите in для получения инструкции:")
        while k!="con":
            if k=="in":
                print("введите MS для сохранения результато\nMR для считования сохраненых результатов\nMC для очишения памяти\nM+ для ручного добовления информации в сохраненые файлы\nнажмите Enter для прикрошения работы калькулятора\nr для того что бы возобновить калькулятор\ncon для продолжения работы с калькулятором")
            if k=="MR":
                q=open("info.txt","r")
                print(q.read())
                q.close()
            elif k=="MC":
                q=open("info.txt","w")
                q.write("")
                q.close()
            elif k=="MS":
                q=open("info.txt","a")
                q.write(a)
                q.write("\n")
                q.close()
            elif k=="M+":
                q=open("info.txt","a")
                q.write(input())
                q.close()
            elif k=="r":
                a=""
                break
            elif k=="":
                q=open("info.txt","w")
                q.write("")
                q.close()
                exit()
            k=input("введите действие:")
    else:a=str(vic(a))
