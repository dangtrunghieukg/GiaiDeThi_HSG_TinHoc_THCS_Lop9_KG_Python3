N = int(input("Nhập số tự nhiên N = "))
listTribo = [0, 1, 1, 2]
Trk = 0
k = 4
while Trk < N:
    Trk = listTribo[k-1]+listTribo[k-2]+listTribo[k-3]
    if Trk > N:
        break
    listTribo.append(Trk)
    k += 1
strKetQua = ""
tong = 0
M = N
for i in range(len(listTribo)-1, 1, -1):
    if M-listTribo[i] >= 0:
        strKetQua = strKetQua + str(listTribo[i]) + "+"
        tong += listTribo[i]
        M = M - listTribo[i]
    if tong == N:
        break
strKetQua = strKetQua[0:len(strKetQua)-1]
print(N,"=", strKetQua, sep='')