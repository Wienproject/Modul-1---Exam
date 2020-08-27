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