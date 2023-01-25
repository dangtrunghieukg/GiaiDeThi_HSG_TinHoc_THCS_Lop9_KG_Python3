# Ta dễ thấy con sên phải bò N bước và lên k bước thì phải bò xuống k bước.
# Do đó độ cao cực đại bằng N chia phần nguyên 2 (N//2)
N = input("Nhập N = ")
N = int(N) #chuyển N sang kiểu số integer
print("Tổng số bước sên bò là:", N)
doCaoMax = N//2 #Chia lấy phần nguyên
print("Độ cao cực đại:",  doCaoMax)
print("Tọa độ các đỉnh:", end='')
Xn = 0
Yn = 0
# 1<= i < N+1
for i in range(1, N+1):
    if i <= doCaoMax:
        Xn += 1
        Yn += 1
        print("("+str(Xn)+","+str(Yn)+");", end='')
    else:
        Xn += 1
        Yn -= 1
        if Yn<0:
            Yn = 0
        if i != N:
            print("("+str(Xn)+","+str(Yn)+");", end='')
        else:
            print("("+str(Xn)+","+str(Yn)+")")
