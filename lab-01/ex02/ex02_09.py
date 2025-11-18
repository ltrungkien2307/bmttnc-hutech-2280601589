def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 
so = int(input("Nhap mot so nguyen: "))
if kiem_tra_so_nguyen_to(so):
    print(f"{so} la so nguyen to")
else:
    print(f"{so} khong phai la so nguyen to")