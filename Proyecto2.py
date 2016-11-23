def creartxt():
    archi=open('datos.txt','w')
    archi.close()

def grabartxt():
    archi=open('datos.txt','a')
    archi.write('BRYAN PILATUÑA\n')
    archi.write('BRYAN ESPAÑA\n') 
    archi.write('PROGRAMACION AVANZADA\n')
    archi.close() 
creartxt()
grabartxt()

def leertxt():
    archi=open('datos.txt','r')
    linea=archi.readline()
    while linea!="":
        print(linea)
        linea=archi.readline()
        archi.close()
