aux = []
while True:
    try:
        x, y = list(input().split())
        aux.append([int(x),int(y)])
    except:
        break  
def probtbpo(valor):
    solucion = []
    counti = 1
    countj = 1
    for i in valor:
        x = i[0]
        y = i[1]
        countj = 1
        if (x < y):
            for j in range(x, y):
                counti = 1
                while (j != 1):
                    if (j % 2 == 0):
                        j = j/2
                    else:
                        j = (3*j)+1
                    counti += 1
                if (counti > countj):
                    countj = counti
            solucion.append([x, y, countj])
        else:
            solucion.append([x , y, 0])
    return(solucion)

print(probtbpo(aux))

"""
counti = 1
countj = 1
x = 1
y = 10
for i in range (x, y+1):
    counti = 1
    while (i != 1):
        counti += 1
        if (i%2 == 0):
            i = i/2
        else:
            i = (i*3)+1
    if (counti > countj):
        countj = counti
    
print(x,y,countj)

"""
