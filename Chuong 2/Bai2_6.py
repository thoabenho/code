Hoten=input("Ho ten: ")
Songaycong=int(input("So ngay cong: "))
Dongiangaycong=int(input("Don gia ngay cong: "))
Hesophucap=float(input("He so phu cap: "))
Tamung=int(input("Tam ung: "))

Luong=round((Dongiangaycong*Songaycong*Hesophucap),1)
ThucLinh=round((Luong-Tamung),1)

print("Nhan vien", Hoten + ", Co tien Luong=" + str(Luong) + ", Tam ung="+str(Tamung) + ", va Thuc linh="+ str(ThucLinh))
