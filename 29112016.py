def creartxt():
    archi=open('palabra.txt','w')
    archi.close()
    
def grabartxt(h,p):
    archi=open('palabra.txt','a')
    archi.write("La palabra de Harry se repide: \t")
    archi.write(str(h))
    archi.write("\nLa palabra de Potter se repide: \t")
    archi.write(str(p))
    archi.close() 

def leertxt():
    h=0
    p=0
    a=''
    archi=open('harry.txt','r')
    linea=archi.readline()
    while linea!="":
        print(linea)
        for i in range(len(linea)):
            if linea[i] ==" ":
                if a == 'Harry':
                    h=h+1
                elif a == 'Harry.':
                    h=h+1
                elif a == 'Potter':
                    p=p+1
                elif a == 'Potter.':
                    p=p+1
                a=''
            else:
                a=a+linea[i]
        linea=archi.readline()     
        archi.close()
    print(h)
    print(p)
    grabartxt(h,p)
    
        
creartxt()       
leertxt()
