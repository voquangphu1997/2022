tien = int(input("Nhap so tien: "))
if tien < 75:
    tien_thanh_toan = tien
elif tien >=75 and tien <100:
    tien_thanh_toan = tien -15
elif tien >=100 and tien <150:
    tien_thanh_toan = tien -25
elif tien >=150 :
    tien_thanh_toan = tien -50
print("So tien phai thanh toan: " + str(tien_thanh_toan))