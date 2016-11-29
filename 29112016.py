def creartxt():
    archi=open('palabra.txt','w')
    archi.close()
    
def grabartxt():
    archi=open('palabra.txt','a')
    archi.write("El total de las palabras son:\t")
    archi.write(str())
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
    grabartxt()
    
        
creartxt()       
leertxt()
