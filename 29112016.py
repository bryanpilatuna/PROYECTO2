def creartxt():
    archi=open('palabra.txt','w')
    archi.close()
    
def grabartxt():
    archi=open('palabra.txt','a')
    archi.write("El total de las palabras son:\t")
    archi.write(str())
    archi.close() 



def leertxt():
    archi=open('harry.txt','r')
    linea=archi.readline()
    while linea!="":
        print(linea)
        linea=archi.readline()     
        archi.close()
    grabartxt()
    
        
creartxt()       
leertxt()
