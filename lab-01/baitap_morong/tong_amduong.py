import re

def tinh_tong_so_trong_chuoi(chuoi):
    # Tìm tất cả các số (bao gồm cả số âm) trong chuỗi
    # Pattern: -?\d+ nghĩa là có thể có dấu - ở đầu, sau đó là 1 hoặc nhiều chữ số
    so_list = re.findall(r'-?\d+', chuoi)
    
    tong_duong = 0
    tong_am = 0
    
    for so in so_list:
        so_nguyen = int(so)
        if so_nguyen > 0:
            tong_duong += so_nguyen
        elif so_nguyen < 0:
            tong_am += so_nguyen
    
    return tong_duong, tong_am

chuoi = "-100#^sdfkj8902w3ir021@swf-20"
print(f"Chuỗi ban đầu: {chuoi}")

tong_duong, tong_am = tinh_tong_so_trong_chuoi(chuoi)
print(f"Giá trị dương: {tong_duong}")
print(f"Giá trị âm: {tong_am}")