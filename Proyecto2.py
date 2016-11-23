def creartxt(): 
	archi=open('datos.txt','w') 
	archi.close()
def grabartxt(): 
	archi=open('datos.txt','a') 
	archi.write('HOLA\n') 
	archi.write('PILATUÑA\n') 
	archi.write('ESPAÑA\n') 
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

leertxt()
