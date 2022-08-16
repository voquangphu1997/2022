print("Nhap so tien USD: ")
usd = int(input())
print("Nhap ti gia USD/VND: ")
tg_usd_vnd = int(input())
vnd = tg_usd_vnd * usd
print(str(usd) + "USD = " + str(vnd) + "VND")