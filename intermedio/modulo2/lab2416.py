#Laboratorio 2.4.1.6
#Elaborado por: Emmanuel López García
#Fecha: 29 de julio del 2022

digitos =[
    '1111110', #0
    '0110000', #1
    '1101101', #2
    '1111001', #3
    '0110011', #4
    '1011011', #5
    '1011111', #6
    '1110000', #7
    '1111111', #8
    '1111011', #9
]

def imprimir_mumero(num):
    global digitos
    digs = str(num)
    lineas = ['' for lin in range(5)]
    for d in digs:
        segs = [[' ',' ',' '] for lin in range(5)]
        ptrn = digitos[ord(d) - ord('0')]
        if ptrn[0] == '1':
            segs[0][0] = segs[0][1]= segs[0][2] = '#'
        if ptrn[1] == '1':
            segs[0][2] = segs[1][2]= segs[2][2] = '#'
        if ptrn[2] == '1':
            segs[2][2] = segs[3][2]= segs[4][2] = '#'
        if ptrn[3] == '1':
            segs[4][0] = segs[4][1]= segs[4][2] = '#'
        if ptrn[4] == '1':
            segs[2][0] = segs[3][0]= segs[4][0] = '#'
        if ptrn[5] == '1':
            segs[0][0] = segs[1][0]= segs[2][0] = '#'
        if ptrn[6] == '1':
            segs[2][0] = segs[2][1]= segs[2][2] = '#'
        for lin in range(5):
            lineas[lin] += ''.join(segs[lin]) + ' '
    for lin in lineas:
        print(lin)

imprimir_mumero(int(input("Ingresa los dígitos: ")))
