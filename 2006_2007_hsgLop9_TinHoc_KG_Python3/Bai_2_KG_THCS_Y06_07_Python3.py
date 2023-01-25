daySo = ""
k = int(input("Nhập k = "))
dem = 0
demHang = 0

while len(daySo)<= k + 1:
    daySo += str(dem)
    dem += 1
chuSoThuK = daySo[k-1]
xuat = "Chữ số thứ {} của dãy vô hạn các số nguyên không âm {}... là: {}"
print(xuat.format(k, "012345678910", chuSoThuK))

'''#Cách làm trên có ưu điểm là dễ hiểu, tuy nhiên chạy hơi chậm. Cách làm dưới đây giúp chạy nhanh hơn
dem = 0
demK = 0
breakOk = False
while dem <= k:
    chuoi = str(dem)
    for x in range(len(chuoi)):
        demK += 1
        if demK == k:
            print("Chữ số thứ", k, "của dãy vô hạn các số nguyên không âm 012345678910... là:",chuoi[x])
            breakOk = True
            break
    if breakOk :
        break
    dem += 1
'''
