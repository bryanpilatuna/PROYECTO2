def creartxt():
    archi=open('conteo.txt','w')
    archi.close()
    
def grabartxt(a):
    archi=open('conteo.txt','a')
    archi.write("El total de las palabras son:\t")
    archi.write(str(a))
    archi.close() 


def leertxt():
    archi=open('DOCUMENTO.txt','r')
    linea=archi.readline()
    while linea!="":
        print(linea)
        a=len(linea)
        linea=archi.readline()
        print ("Los caracteres son son: \n")
        print (a)                
        archi.close()
    grabartxt(a)
        
creartxt()       
leertxt()
