str = input("escribe el texto que te gustaria ver alrevez: ")

f = str

division_roddy = f[::-1]
print(division_roddy)

while True:
        
    t = input("\nescribe tu nombre si quieres ver como es alrevez: ")
    c = len(t)
    b = []

    for i in range(0, c):
        negativo = -i - 1
        for i in t:
            a = list(t)
            print(a[negativo], end=" ")
            break

'''
del input sale:
 y klk, mi nombre es roddy rafael tejeda rosario, que paso?

RESULTADO:
?osap euq ,oirasor adejet leafar yddor se erbmon im ,klk y
'''
