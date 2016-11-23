def creartxt():
    archi=open('datos.txt','w')
    archi.close()

def grabartxt():
    archi=open('datos.txt','a')
    archi.write('\tESCUELA POLITECNICA NACIONAL\n')
    archi.write('\tESCUELA DE FORMACION DE TECNOLOGOS\n')
    archi.write('\tPROGRAMACION AVANZADA\n')
    archi.write('\tINGENIERO JUAN ZALDUMBIDE\n')
    archi.write('INTEGRANTES\n')
    archi.write('BRYAN PILATUÑA\n')
    archi.write('BRYAN ESPAÑA\n')
    archi.write('\tEPN-216\n')
    
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
