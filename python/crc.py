#!/usr/bin/python3
# Codficacion en Python de un CRC de 3 bits (x^2 + x + 1) de entrada
# con division polinomial simulando registros de corrimientos. 

import array

def mycrc(data):
    raw_data = []
    for byte in data:
        for b in range(0,8):
            raw_data.append( 0x01&(byte >> b) )
    c = [0]*3
    c_xor = [0]*3
    for input in raw_data:
        c_xor[0] = (c[2]^input)
        c_xor[1] = ((c[0]^c[2])^input)
        c_xor[2] = ((c[1]^c[2])^input)
        
        c[0] = c_xor[0] # Registro de corrimiento
        c[1] = c_xor[1] # Registro de corrimiento
        c[2] = c_xor[2] # Registro de corrimiento
    crcvalue = ((0x01&c[2]) << 2) | ((0x01&c[1]) << 1) | (0x01&c[0])
    return crcvalue

if __name__ == "__main__":
    
    datos = [1, 1, 1, 1] # 1111b = 15 decimal
    print("El CRC x^2 + x + 1 (111b) de" , datos, " es ", mycrc(datos))
