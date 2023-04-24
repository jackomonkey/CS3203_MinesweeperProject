import sys
import math

class hashFunction:

    def left_rotate(x, amount):
        x &= 0xFFFFFFFF
        return ((x<<amount) | (x>>(32-amount))) & 0xFFFFFFFF

    @staticmethod
    def hash(username):

    
        s = [7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22, 5,  
         9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  4, 11, 
         16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23, 6, 10, 15, 
         21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]
    
        K = [0 for i in range(64)]
        for j in range(64):
            K[j] = math.floor(pow(2,32) * abs(math.sin(j + 1)))

        a0 = 0x67452301
        b0 = 0xefcdab89
        c0 = 0x98badcfe
        d0 = 0x10325476

        #Padding
        username = bytearray(username, encoding="utf8")
        originalLength = len(username) * 8 & 0xffffffffffffffff
        username.append(0x80)
        while(len(username) % 64 != 56):
            username.append(0)

        username += originalLength.to_bytes(8, byteorder='little')

        for chunk in range(0,len(username),64):
            A = a0
            B = b0
            C = c0
            D = d0

            #M = [username[0:4], username[4:8], username[8:12], 
            #    username[12:16], username[16:20], username[20:24], 
            #    username[24:28], username[28:32], username[32:36], 
            #    username[36:40], username[40:44], username[44:48], 
            #    username[48:52], username[52:56], username[56:60], 
            #    username[60:64]]
            
            M = username[chunk:chunk+64]

            for i in range (64):
                F = 0
                g = 0
                if(0 <= i <= 15):
                    F = (B & C) | ((~B) & D)
                    g = i
                elif(16 <= i <= 31):
                    F = (D & B) | ((~D) & C)
                    g = (5 * i + 1) % 16
                elif(32 <= i <= 47):
                    F = B ^ C ^ D
                    g = ((3 * i) + 5) % 16
                elif(48 <= i <= 63):
                    F = C ^ (B | (~D))
                    g = (7 * i) % 16

                F = F + A + K[i]  + M[g * 4]
                A = D
                D = C
                C = B
                F &= 0xFFFFFFFF
                B = B + (((F<<s[i]) | (F>>(32-s[i]))) & 0xFFFFFFFF)

            a0 = a0 + A
            b0 = b0 + B
            c0 = c0 + C
            d0 = d0 + D

        digest = sum(x<<(32*i) for i, x in enumerate([A, B, C, D]))
        raw = digest.to_bytes(17, byteorder="little")

        return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))

password = "yo"
print("Password: " + password + "\n" + "Hashed: " + hashFunction.hash(password))