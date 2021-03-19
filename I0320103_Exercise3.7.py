#TOGAR OBAJA NAINGGOLAN
#NIM I0320103
#KELAS C
#Exercise 3.7

##Contoh cara menghapus pada Dictionary Python

dict = {'Name':'Zara','Age':7,'Class':'First'}
dict['School'] = 'DPS School'
del dict['Name']    # hapus entri dengan key 'Name'
dict.clear()        # hapus semua entri di dict
del dict            # hapus dictionary yang sudah ada

print("dict['Age']: ",dict['Age'])
print("dict['School']: ",dict['School'])
