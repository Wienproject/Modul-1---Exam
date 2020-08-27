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