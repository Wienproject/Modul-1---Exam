listawal=[[1,2,3],[4,5,6],[7,8,9]]

# for i in listawal:
#     print(i)
# print()

def counterclockwise(listawal): # Buat function dgn nama counterclockwise dengan parameter listawal
    rotatelist=[] #Membuat list kosong untuk diisi i yang sudah dirotasi dari kondisi-kondisi di bawah
    panjanglist= len(listawal)
    for i in range(panjanglist): # buat looping dgn panjang list(len dari list awal)
        rotatelist.append([]) #tambahkan bracket kosong ke rotatelist
    for i in range(panjanglist): # buat looping dgn panjang list(len dari list awal)
        for j in range(panjanglist): #buat looping untuk setiap element di panjanglist
            rotatelist[i].append(listawal[j].pop(-1)) #tambahkan element j dr listawal dan remove 1 item paling kanan
    return rotatelist #return list yang sudah dirotasi ke list kosong rotatelist

for i in counterclockwise(listawal): #Buat looping agar dapat tampilan ke bawah
    print (i)