#TOGAR OBAJA NAINGGOLAN
#NIM I0320103
#KELAS C
#TUgas 3 Soal 2

dict = {'Nama':'Togar Obaja Nainggolan','sosial media1':'instagram:@togarobaja_n'
    ,'sosial media2':'twitter:@ObajaTogar','sosial media3':'id line:togarobaja','makanan favorit1':"Bakso"
    ,'makanan favorit2':'Nasi goreng','makanan favorit3':"Martabak telor"}
dict2 = {'hobi1':'menonton film','hobi2':'bermain gitar','hobi3':'bermain futsal'
    ,'lagu kesukaan1':'Never lost (Elevation Worship)','lagu kesukaan2':'Evaluasi (Hindia)'
    ,'lagu kesukaan3':'Tukar Jiwa (Tulus)'}
dict2['hobi2'] = "bermain bulutangkis"
dict['sosial media3'] = "facebook:Togar Obaja"
del dict['makanan favorit3'],dict['makanan favorit2']
dict2['hobi4'] = "bermain game online"
dict.update(dict2)
print(dict)