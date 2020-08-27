def rajut(text): #buat fungsi rajut dengan parameter text
    lengthtext= len(text) # buat variabel untuk menampilkan jumlah index di text
    result= '' #buat 1 variabel untuk menampung hasil
    before = 0 #buat variabel before dgn angka 0
    after = 1 #buat variabel after dgn angka 1
    exponent =1
    for i in range(lengthtext):
        i+=1
        if before<=len(text[-1]):
            result = text[before:after]
            before = after
            exponent= exponent + 1
            after = exponent + after
    return result

print(rajut('CCoCodCode'))