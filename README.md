# Ujian-Modul-1-Michael-Prasetya

Soal 1
def timeconverter(seconds): #Buat function timeconverter dgn parameter second
    
    while True: #buat while looping selama benar
            try: #test variabel yang mempunyai syarat tertentu (in this case: Seconds, karena harus integer)
                seconds=int(input('Masukan detik : '))#buat variabel detik yg bisa diinput dan HARUS integer
            
                if seconds > 359999:  # buat kondisi, second tidak boleh lebih dari 359999
                    print('Invalid Input !')
                    continue
                if seconds <0: #Buat kondisi, second tidak boleh negativ
                    print('Invalid Input !')
                    continue
                h = seconds//(3600) #buat variabel jam, dimana 1 jam =3600 detik
                if h>99: #Buat syarat jam tidak boleh lebih dari 99
                    print('Invalid Input !')
                    continue
                m = (seconds-h*3600)//60 #buat variabel menit, dimana 1 jam=60menit=3600detik
                if m>59: #Buat kondisi menit tidak boleh lebih dari 59
                    print('Invalid Input !')
                    continue
                s = seconds-(h*60*60)-(m*60) #buat variabel detik
                print ('Konversi ', h,'jam :',m,'menit :',s,'detik')
                break
            except: #beri syarat jika keadaan integer tidak terpenuhi, maka "Invalid Input" akan keluar
                print ('Invalid Input !')
    return 
timeconverter({})




Soal 2
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
    
    
    
Soal 3
def urai(text): #Buat 1 function urai dgn argumen text
    x = 0 #Buat 1 variabel untuk menghitung jumlah i
    result ='' # Buat 1 variabel kosong untuk menampilkan hasil
    for i in text: #Buat for looping i dalam text
        x +=1 
        print(text[0:x],end='') #tampilkan index 0 sampai yang kita inginkan dari text dengan(end=''untuk membuat agar hasil menyamping) 
    return result

print(urai('Purwadhika'))
print(urai('Python'))
print(urai("Code"))
