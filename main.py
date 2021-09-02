a = (3.1415926535)
b = (3.14)
c = (22/7)

rad = (8)
pi = b

print( rad,"| radius")
print( pi,"| pi")
print("--------------------------------------------------------------")


circle = rad*rad*pi
roundedcir = round(circle,4)
print(roundedcir, "circle")

semicircle = (roundedcir * 1/2)
roundedsemi = round(semicircle,4)
print(roundedsemi, "semicircle")

quartant = (roundedcir * 1/4)
roundedqua = round(quartant,4)
print(roundedqua, "quartant")

print("end")