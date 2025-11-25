import itertools

def liet_ke_hoan_vi():
    danh_sach = [1, 2, 3]
    hoan_vi = itertools.permutations(danh_sach)
    
    print("Các hoán vị của danh sách [1, 2, 3]:")
    for hv in hoan_vi:
        print(hv)
liet_ke_hoan_vi()

