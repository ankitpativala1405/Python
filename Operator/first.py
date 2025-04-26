a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

sum_value = a + b + c
print("Total :", sum_value)

dis = float(input("Enter Discount: "))
d = sum_value * dis / 100
e = sum_value - d
print("Total Discounted Amount :", e)

e += e * 0.18
print("Total with GST :", e)