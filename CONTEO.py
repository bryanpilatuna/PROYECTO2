def creartxt():
    archi=open('conteo.txt','w')
    archi.close()
    
def grabartxt():
    archi=open('datos.txt','a')
    
    archi.close() 
creartxt()
grabartxt()

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
creartxt()
leertxt()
