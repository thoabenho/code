n=int(input("n= "))
k=int(input("k= "))
T=float(input("T= "))

m=round((n*(1+k*T)),1)

print("Voi so tien ban dau "+ str(n) + ", sau " + str(k) + " thang gui," + " lai suat " + str(T) + "/thang")
print("Thi so tien nhan duoc cuoi ky la:", m)
