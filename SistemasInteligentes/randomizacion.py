import random

abc = ['a','b','c','ch','d','e','f','g','h','i','j','k','l','ll','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

def readtxt  ( path ):
    with open( path, 'r') as f:
        lines = f.readlines()
    return lines

def randomizade ():
    path = '/home/gabriel/Escritorio/PagGuemes.txt'
    lines = readtxt( path )
    oracioneserroneas =  open ('/home/gabriel/errores.txt','w')
    for i in range (150):
        newline = lines[ i ]
        combinenline = lines[ random.randint( 0, 150 ) ]
        corte = random.randint(0, len(newline)-1)
        add = random.randint(0,len(combinenline)-1)
        rand = random.randint(0, 2)
        if (rand == 0):
            newline = newline[0:corte] + abc[random.randint(0, len(abc)-1)]+ combinenline[add:]
        elif (rand == 2):
            newline = newline[0:corte]
            for i in range(random.randint(0,len(newline)-1)):
                newline += abc[random.randint(0, len(abc)-1)]
        else:
            newline = newline[0:corte] + combinenline[add:]
        oracioneserroneas.write(newline)
    oracioneserroneas.close()

randomizade()
        
