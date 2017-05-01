

def jsint(a):
    k = a % (2*2147483648)
    if k >= 2147483648:
        return k - 2*2147483648

    return k


def sr(a, b):
    if a < 0:
        return jsint(((2 << (31 - b))+(a >> b)))
    else:
        return jsint(a >> b)


def m_he(a, b):
    c = 0
    d = a.Sf
    if len(d) < 80:
        for i in range(0, 80-len(d)):
            d.append(0)
    for e in range(c, c+64, 4):
        d[e // 4] = jsint(b[e] << 24 | b[e + 1] << 16 | b[e + 2] << 8 | b[e + 3])
    for e in range(16, 80, 1):
        f = jsint(d[e - 3] ^ d[e - 8] ^ d[e - 14] ^ d[e - 16])
        d[e] = (jsint(f << 1) | sr(f, 31)) & jsint(4294967295)
    c = a.i[0]
    g = a.i[1]
    h = a.i[2]
    i = a.i[3]
    j = a.i[4]

    k = 0
    for e in range(0, 80, 1):
        if e < 40:
            if e < 20:
                f = jsint(i ^ g & (h ^ i))
                k = jsint(1518500249)
            else:
                f = jsint(g ^ h ^ i)
                k = jsint(1859775393)
        else:
            if e < 60:
                f = jsint(g & h | i & (g | h))
                k = jsint(2400959708)
            else:
                f = jsint(g ^ h ^ i)
                k = jsint(3395469782)
        f = jsint((jsint(c << 5) | sr(c, 27)) + f + j + k + d[e] & jsint(4294967295))
        j = jsint(i)
        i = jsint(h)
        h = jsint((jsint(g << 30) | sr(g, 2)) & jsint(4294967295))
        g = jsint(c)
        c = jsint(f)
    a.i[0] = jsint(a.i[0] + c & jsint(4294967295))
    a.i[1] = jsint(a.i[1] + g & jsint(4294967295))
    a.i[2] = jsint(a.i[2] + h & jsint(4294967295))
    a.i[3] = jsint(a.i[3] + i & jsint(4294967295))
    a.i[4] = jsint(a.i[4] + j & jsint(4294967295))


m_Sc = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118, 202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192, 183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117, 9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207, 208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115, 96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8, 186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223, 140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22]
m_Rc = [82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163, 158, 129, 243, 215, 251, 124, 227, 57, 130, 155, 47, 255, 135, 52, 142, 67, 68, 196, 222, 233, 203, 84, 123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11, 66, 250, 195, 78, 8, 46, 161, 102, 40, 217, 36, 178, 118, 91, 162, 73, 109, 139, 209, 37, 114, 248, 246, 100, 134, 104, 152, 22, 212, 164, 92, 204, 93, 101, 182, 146, 108, 112, 72, 80, 253, 237, 185, 218, 94, 21, 70, 87, 167, 141, 157, 132, 144, 216, 171, 0, 140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6, 208, 44, 30, 143, 202, 63, 15, 2, 193, 175, 189, 3, 1, 19, 138, 107, 58, 145, 17, 65, 79, 103, 220, 234, 151, 242, 207, 206, 240, 180, 230, 115, 150, 172, 116, 34, 231, 173, 53, 133, 226, 249, 55, 232, 28, 117, 223, 110, 71, 241, 26, 113, 29, 41, 197, 137, 111, 183, 98, 14, 170, 24, 190, 27, 252, 86, 62, 75, 198, 210, 121, 32, 154, 219, 192, 254, 120, 205, 90, 244, 31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16, 89, 39, 128, 236, 95, 96, 81, 127, 169, 25, 181, 74, 13, 45, 229, 122, 159, 147, 201, 156, 239, 160, 224, 59, 77, 174, 42, 245, 176, 200, 235, 187, 60, 131, 83, 153, 97, 23, 43, 4, 126, 186, 119, 214, 38, 225, 105, 20, 99, 85, 33, 12, 125]
m_Ic = [[0, 0, 0, 0],
        [1, 0, 0, 0],
        [2, 0, 0, 0],
        [4, 0, 0, 0],
        [8, 0, 0, 0],
        [16, 0, 0, 0],
        [32, 0, 0, 0],
        [64, 0, 0, 0],
        [128, 0, 0, 0],
        [27, 0, 0, 0],
        [54, 0, 0, 0]]
m_Qc = [0, 9, 18, 27, 36, 45, 54, 63, 72, 65, 90, 83, 108, 101, 126, 119, 144, 153, 130, 139, 180, 189, 166, 175, 216, 209, 202, 195, 252, 245, 238, 231, 59, 50, 41, 32, 31, 22, 13, 4, 115, 122, 97, 104, 87, 94, 69, 76, 171, 162, 185, 176, 143, 134, 157, 148, 227, 234, 241, 248, 199, 206, 213, 220, 118, 127, 100, 109, 82, 91, 64, 73, 62, 55, 44, 37, 26, 19, 8, 1, 230, 239, 244, 253, 194, 203, 208, 217, 174, 167, 188, 181, 138, 131, 152, 145, 77, 68, 95, 86, 105, 96, 123, 114, 5, 12, 23, 30, 33, 40, 51, 58, 221, 212, 207, 198, 249, 240, 235, 226, 149, 156, 135, 142, 177, 184, 163, 170, 236, 229, 254, 247, 200, 193, 218, 211, 164, 173, 182, 191, 128, 137, 146, 155, 124, 117, 110, 103, 88, 81, 74, 67, 52, 61, 38, 47, 16, 25, 2, 11, 215, 222, 197, 204, 243, 250, 225, 232, 159, 150, 141, 132, 187, 178, 169, 160, 71, 78, 85, 92, 99, 106, 113, 120, 15, 6, 29, 20, 43, 34, 57, 48, 154, 147, 136, 129, 190, 183, 172, 165, 210, 219, 192, 201, 246, 255, 228, 237, 10, 3, 24, 17, 46, 39, 60, 53, 66, 75, 80, 89, 102, 111, 116, 125, 161, 168, 179, 186, 133, 140, 151, 158, 233, 224, 251, 242, 205, 196, 223, 214, 49, 56, 35, 42, 21, 28, 7, 14, 121, 112, 107, 98, 93, 84, 79, 70]
m_Oc = [0, 11, 22, 29, 44, 39, 58, 49, 88, 83, 78, 69, 116, 127, 98, 105, 176, 187, 166, 173, 156, 151, 138, 129, 232, 227, 254, 245, 196, 207, 210, 217, 123, 112, 109, 102, 87, 92, 65, 74, 35, 40, 53, 62, 15, 4, 25, 18, 203, 192, 221, 214, 231, 236, 241, 250, 147, 152, 133, 142, 191, 180, 169, 162, 246, 253, 224, 235, 218, 209, 204, 199, 174, 165, 184, 179, 130, 137, 148, 159, 70, 77, 80, 91, 106, 97, 124, 119, 30, 21, 8, 3, 50, 57, 36, 47, 141, 134, 155, 144, 161, 170, 183, 188, 213, 222, 195, 200, 249, 242, 239, 228, 61, 54, 43, 32, 17, 26, 7, 12, 101, 110, 115, 120, 73, 66, 95, 84, 247, 252, 225, 234, 219, 208, 205, 198, 175, 164, 185, 178, 131, 136, 149, 158, 71, 76, 81, 90, 107, 96, 125, 118, 31, 20, 9, 2, 51, 56, 37, 46, 140, 135, 154, 145, 160, 171, 182, 189, 212, 223, 194, 201, 248, 243, 238, 229, 60, 55, 42, 33, 16, 27, 6, 13, 100, 111, 114, 121, 72, 67, 94, 85, 1, 10, 23, 28, 45, 38, 59, 48, 89, 82, 79, 68, 117, 126, 99, 104, 177, 186, 167, 172, 157, 150, 139, 128, 233, 226, 255, 244, 197, 206, 211, 216, 122, 113, 108, 103, 86, 93, 64, 75, 34, 41, 52, 63, 14, 5, 24, 19, 202, 193, 220, 215, 230, 237, 240, 251, 146, 153, 132, 143, 190, 181, 168, 163]
m_Pc = [0, 13, 26, 23, 52, 57, 46, 35, 104, 101, 114, 127, 92, 81, 70, 75, 208, 221, 202, 199, 228, 233, 254, 243, 184, 181, 162, 175, 140, 129, 150, 155, 187, 182, 161, 172, 143, 130, 149, 152, 211, 222, 201, 196, 231, 234, 253, 240, 107, 102, 113, 124, 95, 82, 69, 72, 3, 14, 25, 20, 55, 58, 45, 32, 109, 96, 119, 122, 89, 84, 67, 78, 5, 8, 31, 18, 49, 60, 43, 38, 189, 176, 167, 170, 137, 132, 147, 158, 213, 216, 207, 194, 225, 236, 251, 246, 214, 219, 204, 193, 226, 239, 248, 245, 190, 179, 164, 169, 138, 135, 144, 157, 6, 11, 28, 17, 50, 63, 40, 37, 110, 99, 116, 121, 90, 87, 64, 77, 218, 215, 192, 205, 238, 227, 244, 249, 178, 191, 168, 165, 134, 139, 156, 145, 10, 7, 16, 29, 62, 51, 36, 41, 98, 111, 120, 117, 86, 91, 76, 65, 97, 108, 123, 118, 85, 88, 79, 66, 9, 4, 19, 30, 61, 48, 39, 42, 177, 188, 171, 166, 133, 136, 159, 146, 217, 212, 195, 206, 237, 224, 247, 250, 183, 186, 173, 160, 131, 142, 153, 148, 223, 210, 197, 200, 235, 230, 241, 252, 103, 106, 125, 112, 83, 94, 73, 68, 15, 2, 21, 24, 59, 54, 33, 44, 12, 1, 22, 27, 56, 53, 34, 47, 100, 105, 126, 115, 80, 93, 74, 71, 220, 209, 198, 203, 232, 229, 242, 255, 180, 185, 174, 163, 128, 141, 154, 151]
m_Nc = [0, 14, 28, 18, 56, 54, 36, 42, 112, 126, 108, 98, 72, 70, 84, 90, 224, 238, 252, 242, 216, 214, 196, 202, 144, 158, 140, 130, 168, 166, 180, 186, 219, 213, 199, 201, 227, 237, 255, 241, 171, 165, 183, 185, 147, 157, 143, 129, 59, 53, 39, 41, 3, 13, 31, 17, 75, 69, 87, 89, 115, 125, 111, 97, 173, 163, 177, 191, 149, 155, 137, 135, 221, 211, 193, 207, 229, 235, 249, 247, 77, 67, 81, 95, 117, 123, 105, 103, 61, 51, 33, 47, 5, 11, 25, 23, 118, 120, 106, 100, 78, 64, 82, 92, 6, 8, 26, 20, 62, 48, 34, 44, 150, 152, 138, 132, 174, 160, 178, 188, 230, 232, 250, 244, 222, 208, 194, 204, 65, 79, 93, 83, 121, 119, 101, 107, 49, 63, 45, 35, 9, 7, 21, 27, 161, 175, 189, 179, 153, 151, 133, 139, 209, 223, 205, 195, 233, 231, 245, 251, 154, 148, 134, 136, 162, 172, 190, 176, 234, 228, 246, 248, 210, 220, 206, 192, 122, 116, 102, 104, 66, 76, 94, 80, 10, 4, 22, 24, 50, 60, 46, 32, 236, 226, 240, 254, 212, 218, 200, 198, 156, 146, 128, 142, 164, 170, 184, 182, 12, 2, 16, 30, 52, 58, 40, 38, 124, 114, 96, 110, 68, 74, 88, 86, 55, 57, 43, 37, 15, 1, 19, 29, 71, 73, 91, 85, 127, 113, 99, 109, 215, 217, 203, 197, 239, 225, 243, 253, 167, 169, 187, 181, 159, 145, 131, 141]


def m_Hc(a):
    a[0] = m_Sc[a[0]]
    a[1] = m_Sc[a[1]]
    a[2] = m_Sc[a[2]]
    a[3] = m_Sc[a[3]]


def m_Kc(a, b):
    for c in range(4):
        for d in range(4):
            a.j[c][d] = a.j[c][d] ^ a.C[4 * b + d][c]


def m_Lc(a):
    for b in range(1, 4):
        for c in range(4):
            a.wc[b][(c+b) % 4] = a.j[b][c]
    for b in range(1, 4):
        for c in range(4):
            a.j[b][c] = a.wc[b][c]


def m_Mc(a):
    for c in range(4):
        for d in range(4):
            a.j[c][d] = m_Rc[a.j[c][d]]


class m_Jc:
    Vb = [91, 99, 219, 17, 59, 122, 243, 224, 177, 67, 85, 86, 200, 249, 83, 12]
    I = 4
    Ub = 10
    j = [[], [], [], []]
    wc = [[], [], [], []]
    C = [''] * 44

    def __init__(self):
        # self.C = ['' for i in range(4*(self.Ub+1))]
        for a in range(self.I):
            self.C[a] = [self.Vb[a*4], self.Vb[a*4+1], self.Vb[a*4+2], self.Vb[a * 4+3]]
        b = [''] * 4
        for a in range(self.I, (4*(self.Ub+1)), 1):
            b[0] = self.C[a-1][0]
            b[1] = self.C[a-1][1]
            b[2] = self.C[a-1][2]
            b[3] = self.C[a-1][3]
            if(a % self.I) == 0:
                c = b
                d = c[0]
                c[0] = c[1]
                c[1] = c[2]
                c[2] = c[3]
                c[3] = d
                m_Hc(b)
                b[0] = int(b[0]) ^ int(m_Ic[a // self.I][0])
                b[1] = int(b[1]) ^ int(m_Ic[a // self.I][1])
                b[2] = int(b[2]) ^ int(m_Ic[a // self.I][2])
                b[3] = int(b[3]) ^ int(m_Ic[a // self.I][3])

            else:
                if (6 < self.I) and (4 == a % self.I):
                    m_Hc(b)
            self.C[a] = ['', '', '', '']
            self.C[a][0] = int(self.C[a - self.I][0]) ^ int(b[0])
            self.C[a][1] = int(self.C[a - self.I][1]) ^ int(b[1])
            self.C[a][2] = int(self.C[a - self.I][2]) ^ int(b[2])
            self.C[a][3] = int(self.C[a - self.I][3]) ^ int(b[3])

    def vd(self, bytes, new_bytes, num):
        for f in range(4):
            for g in range(4):
                self.j[f].append("")
                self.wc[f].append("")
                self.j[f][g] = bytes[4*g+f+num]
        m_Kc(self, self.Ub)
        for a in range(1, self.Ub, 1):
            m_Lc(self)
            m_Mc(self)
            m_Kc(self, self.Ub-a)
            c = self.j
            f = self.wc[0]
            for g in range(0, 4):
                f[0] = c[0][g]
                f[1] = c[1][g]
                f[2] = c[2][g]
                f[3] = c[3][g]
                c[0][g] = m_Nc[f[0]] ^ m_Oc[f[1]] ^ m_Pc[f[2]] ^ m_Qc[f[3]]
                c[1][g] = m_Qc[f[0]] ^ m_Nc[f[1]] ^ m_Oc[f[2]] ^ m_Pc[f[3]]
                c[2][g] = m_Pc[f[0]] ^ m_Qc[f[1]] ^ m_Nc[f[2]] ^ m_Oc[f[3]]
                c[3][g] = m_Oc[f[0]] ^ m_Pc[f[1]] ^ m_Qc[f[2]] ^ m_Nc[f[3]]

        m_Lc(self)
        m_Mc(self)
        m_Kc(self, 0)
        new_bytes += [''] * 16

        d = 16 if len(new_bytes) > 16 else 0

        for a in range(4):
            for c in range(4):
                new_bytes[4*c+a+d] = self.j[a][c]
        return new_bytes


zz_cg = m_Jc()
xor_bytes = [113, 231, 4, 5, 53, 58, 119, 139, 250, 111, 188, 48, 50, 27, 149, 146]


def get_replacement(bytes):
    new_bytes = []
    for num in range(0, len(bytes), 16):
        new_bytes = zz_cg.vd(bytes, new_bytes, num)
        xor = xor_bytes if num == 0 else bytes

        for i in range(16):
            new_bytes[num + i] = new_bytes[num + i] ^ xor[i]
    return new_bytes


def bytes_to_number(bytes, index):
    # Add up the bytes, bitwise shifting from small to large
    # E.g. '20, 01, 00, 00' -> 32 + (1 << 8) -> 288
    total = bytes[index]
    total += bytes[index+1] << 8
    total += bytes[index+2] << 16
    total += bytes[index+3] << 24
    return total


def decrypt(image):
    # return if the encryption marker isn't present at the start of the file
    if image[:4] != b"\x0A\x0A\x0A\x0A":
        return image

    # Convert the image to a list of ints (0 -> 255) (for insertion, maths etc)
    byte_list = list(image)

    # Use the last 4 bytes to get the index of the bytes to be replaced
    index = bytes_to_number(byte_list, len(byte_list) - 4)

    # Trim out the encryption marker and info bytes
    byte_list = byte_list[4:-4]

    # How many bytes to replace
    replace_num = bytes_to_number(byte_list, index)

    # Delete the 4 bytes at the start
    del byte_list[index:index+4]

    # The bytes to replace
    to_replace = byte_list[index:index+replace_num]

    # Get the replacement bytes
    replacement = get_replacement(to_replace)
    # Replace the bytes!
    byte_list[index:index+replace_num] = replacement

    # Convert back into bytes
    return bytes(byte_list)
