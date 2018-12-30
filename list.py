list1=[1212,333, 55]
print(list1[0])
print(list1[1])
print(list1[2])

list1.remove(333)
list1.append(3334)
print(list1)

#loop
for a in list1:
    print(a)


angka =0
while(angka!=1):

    a=input("masukkan angka : ")
    try:
        angka = int(a)    
    except ValueError:
        print("bukan angka")
        
    

print("\n######### program selesai")
