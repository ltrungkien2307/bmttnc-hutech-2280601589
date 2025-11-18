so_gio_lam = float(input("Nhap so gio lam viec trong tuan: "))
luong_1_gio = float(input("Nhap luong 1 gio: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_1_gio + gio_vuot_chuan * luong_1_gio * 1.5
print(f"so tien thuc linh {thuc_linh}" )