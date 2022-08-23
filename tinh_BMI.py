can_nang = float(input("Nhap can nang: "))
chieu_cao = float(input("Nhap chieu cao: "))
BMI = can_nang / (chieu_cao ** 2)
print("BMI = " + str(BMI))
if BMI < 16:
    print("Gay cap do III")
elif BMI >= 16 and BMI < 17:
    print("Gay cap do II")
elif BMI >= 17 and BMI < 18.5:
    print("Gay cap do I")
elif BMI >= 18.5 and BMI < 25:
    print("Binh thuong")
elif BMI >= 25 and BMI < 30:
    print("Thua can")
elif BMI >= 30 and BMI < 35:
    print("Beo phi cap do I")
elif BMI >= 35 and BMI < 40:
    print("Beo phi cap do II")