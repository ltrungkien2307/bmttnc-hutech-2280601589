def chia_het_cho_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan, 2)
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
chuoi_so_nhi_phan = input("nhap chuoi(cach nhau dau ',') ")
list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho5 = [so for so in list if chia_het_cho_5(so)]
if len(so_chia_het_cho5) > 0:
    ketqua = ','.join(so_chia_het_cho5)
    print("cac so nhi phan chia het cho 5 la ", ketqua)
else:
     print("khong co so nao")