# Name: Abyatar Fanuel Lantera
# Class: JC Data Science Online 012 - C
# Capstone Project Module 1 (Topik: Rental Mobil)

# List Mobil Rental
listMobil = [
    {
        'Jenis Mobil' : 'SUV',
        'Merk' : 'Mitsubishi',
        'Tipe' : 'Pajero Sport',
        'Tahun' : 2019,
        'Stock' : 1,
        '12 Jam' : 350000,
        '24 Jam' : 700000
    },
    
    {
        'Jenis Mobil' : 'Van',
        'Merk' : 'Daihatsu',
        'Tipe' : 'Gran Max',
        'Tahun' : 2018,
        'Stock' : 5,
        '12 Jam' : 250000,
        '24 Jam' : 500000
    },
    
    {
        'Jenis Mobil' : 'Sedan',
        'Merk' : 'Honda',
        'Tipe' : 'Accord',
        'Tahun' : 2019,
        'Stock' : 2,
        '12 Jam' : 300000,
        '24 Jam' : 600000
    },
    
    {
        'Jenis Mobil' : 'LCGC',
        'Merk' : 'Toyota',
        'Tipe' : 'Agya',
        'Tahun' : 2020,
        'Stock' : 3,
        '12 Jam' : 100000,
        '24 Jam' : 200000
    },
    
    {
        'Jenis Mobil' : 'MPV',
        'Merk' : 'Suzuki',
        'Tipe' : 'Ertiga',
        'Tahun' : 2019,
        'Stock' : 4,
        '12 Jam' : 200000,
        '24 Jam' : 400000
    }          
]

##################################################################################

#Membuat fungsi untuk menampilkan data mobil rental (Menu 1.1)
def data_mobil():
    
    # Menampilkan judul tabel daftar mobil rental
    print('\t\t\t\t          Daftar Mobil Rental')
    print('+' + '-' * 103 + '+')
    print('| Kode\t| Jenis Mobil\t| Merk\t\t| Tipe\t\t| Tahun\t| Stock\t| Tarif 12 Jam\t| Tarif 24 Jam\t|')
    print('+' + '-' * 103 + '+')
    
    # Looping untuk menampilkan tabel data mobil rental dengan bebrapa kondisi agar tabel rapih
    for i in range(len(listMobil)) :
        if len(listMobil[i]['Merk']) > 5 and len(listMobil[i]['Tipe']) > 5 :
            # ketika merk dan tipe mobil lebih dari 5 karakter
            print(f'| {i}\t| {listMobil[i]["Jenis Mobil"]}\t\t| {listMobil[i]["Merk"]}\t| {listMobil[i]["Tipe"]}\t| {listMobil[i]["Tahun"]}\t| {listMobil[i]["Stock"]}\t| {listMobil[i]["12 Jam"]}\t| {listMobil[i]["24 Jam"]}\t|')
        elif len(listMobil[i]['Merk']) <= 5 and len(listMobil[i]['Tipe']) <= 5 :
            # ketika merk dan tipe mobil kurang dari sama dengan 5 karakter
            print(f'| {i}\t| {listMobil[i]["Jenis Mobil"]}\t\t| {listMobil[i]["Merk"]}\t\t| {listMobil[i]["Tipe"]}\t\t| {listMobil[i]["Tahun"]}\t| {listMobil[i]["Stock"]}\t| {listMobil[i]["12 Jam"]}\t| {listMobil[i]["24 Jam"]}\t|')
        elif len(listMobil[i]['Merk']) > 5 and len(listMobil[i]['Tipe']) <= 5 :
            # ketika merk mobil lebih dari 5 karakter dan tipe mobil kurang dari sama dengan 5 karakter
            print(f'| {i}\t| {listMobil[i]["Jenis Mobil"]}\t\t| {listMobil[i]["Merk"]}\t| {listMobil[i]["Tipe"]}\t\t| {listMobil[i]["Tahun"]}\t| {listMobil[i]["Stock"]}\t| {listMobil[i]["12 Jam"]}\t| {listMobil[i]["24 Jam"]}\t|')
        elif len(listMobil[i]['Merk']) <= 5 and len(listMobil[i]['Tipe']) > 5 :
            # ketika merk mobil kurang dari sama dengan 5 karakter dan tipe mobil lebih dari 5 karakter
            print(f'| {i}\t| {listMobil[i]["Jenis Mobil"]}\t\t| {listMobil[i]["Merk"]}\t\t| {listMobil[i]["Tipe"]}\t| {listMobil[i]["Tahun"]}\t| {listMobil[i]["Stock"]}\t| {listMobil[i]["12 Jam"]}\t| {listMobil[i]["24 Jam"]}\t|')
    
    print('+' + '-' * 103 + '+')
    
# Memfilter data mobil rental berdasarkan Merk (Menu 1.2)
def filter_mobil():
    # Menampilkan data mobil rental sebelum memfilter data mobil berdasarkan merk
    data_mobil()
    
    # Validasi inputan merk mobil. Jika inputan bukan merk mobil yang tersedia maka akan terus mengulang inputan / looping
   
    merk_mobil = input('Masukkan merk mobil yang ingin ditampilkan : ')
            
    # Menampilkan judul tabel daftar mobil rental
    print('\t\t\t\t          Daftar Mobil Rental')
    print('+' + '-' * 103 + '+')
    print('| Kode\t| Jenis Mobil\t| Merk\t\t| Tipe\t\t| Tahun\t| Stock\t| Tarif 12 Jam\t| Tarif 24 Jam\t|')
    print('+' + '-' * 103 + '+')
    
    # Looping untuk menampilkan tabel data mobil rental dengan bebrapa kondisi agar tabel rapih
    for i in range(len(listMobil)) :
        if merk_mobil.lower() == listMobil[i]['Merk'].lower():
            if len(listMobil[i]['Merk']) > 5 and len(listMobil[i]['Tipe']) > 5 :
                # ketika merk dan tipe mobil lebih dari 5 karakter
                print(f'| {i}\t| {listMobil[i]["Jenis Mobil"]}\t\t| {listMobil[i]["Merk"]}\t| {listMobil[i]["Tipe"]}\t| {listMobil[i]["Tahun"]}\t| {listMobil[i]["Stock"]}\t| {listMobil[i]["12 Jam"]}\t| {listMobil[i]["24 Jam"]}\t|')
            elif len(listMobil[i]['Merk']) <= 5 and len(listMobil[i]['Tipe']) <= 5 :
                # ketika merk dan tipe mobil kurang dari sama dengan 5 karakter
                print(f'| {i}\t| {listMobil[i]["Jenis Mobil"]}\t\t| {listMobil[i]["Merk"]}\t\t| {listMobil[i]["Tipe"]}\t\t| {listMobil[i]["Tahun"]}\t| {listMobil[i]["Stock"]}\t| {listMobil[i]["12 Jam"]}\t| {listMobil[i]["24 Jam"]}\t|')
            elif len(listMobil[i]['Merk']) > 5 and len(listMobil[i]['Tipe']) <= 5 :
                # ketika merk mobil lebih dari 5 karakter dan tipe mobil kurang dari sama dengan 5 karakter
                print(f'| {i}\t| {listMobil[i]["Jenis Mobil"]}\t\t| {listMobil[i]["Merk"]}\t| {listMobil[i]["Tipe"]}\t\t| {listMobil[i]["Tahun"]}\t| {listMobil[i]["Stock"]}\t| {listMobil[i]["12 Jam"]}\t| {listMobil[i]["24 Jam"]}\t|')
            elif len(listMobil[i]['Merk']) <= 5 and len(listMobil[i]['Tipe']) > 5 :
                # ketika merk mobil kurang dari sama dengan 5 karakter dan tipe mobil lebih dari 5 karakter
                print(f'| {i}\t| {listMobil[i]["Jenis Mobil"]}\t\t| {listMobil[i]["Merk"]}\t\t| {listMobil[i]["Tipe"]}\t| {listMobil[i]["Tahun"]}\t| {listMobil[i]["Stock"]}\t| {listMobil[i]["12 Jam"]}\t| {listMobil[i]["24 Jam"]}\t|')
        else:
            continue
    
    print('+' + '-' * 103 + '+')
    
##################################################################################

#Membuat Fungsi Menambahkan Data Mobil Rental (Menu 2.1)
def tambah_mobil():
    
    #Menampilkan data mobil rental sebelum menambahkan data baru
    data_mobil()

    # Validasi Inputan jenis mobil. Jika inputan bukan jenis mobil yang tersedia maka akan terus mengulang inputan / looping
    while True:
        jenis_mobil = input('Masukkan jenis mobil [SUV, MPV, Sedan, Van, LCGC]: ')
        if jenis_mobil.lower() in ['suv', 'mpv', 'sedan', 'van', 'lcgc']:
            break
        else:
            print('Jenis mobil tidak tersedia')
            
    merk = input('Masukkan merk mobil : ')


    while True:
        try:
            tipe = input('Masukkan tipe mobil : ')
            tahun = int(input('Masukkan tahun mobil : '))
            
            #Cek duplikat data mobil rental, 
            for i in listMobil:
                if i['Tahun'] == tahun and i['Tipe'].lower() == tipe.lower():
                    print('Data mobil sudah ada, silahkan masukkan data mobil yang baru')
                    # Jika data mobil sudah ada maka akan mengulang inputan / looping
                    return
            else :
                # Jika data mobil belum ada maka akan melanjutkan baris selanjutnya di fungsi tambah_mobil()
                break
        except ValueError:
            # Validasi inputan tahun, stock dan tarif harus berupa integer (Jika bukan integer maka akan terus mengulang inputan / looping)
            print('Inputan tahun harus berupa angka')

    while True:
        try:
            stock = int(input('Masukkan stock mobil : '))
            break
        except ValueError:
            print('Inputan harus berupa angka')

    while True:
        try:
            tarif_12jam = int(input('Masukkan tarif 12 jam : '))
            break
        except ValueError:
            print('Inputan harus berupa angka')
            
    while True:
        try:
            tarif_24jam = int(input('Masukkan tarif 24 jam : '))
            break
        except ValueError:
            print('Inputan harus berupa angka')

    # Menambahkan data mobil yang sudah di input ke listMobil
    listMobil.append({
        'Jenis Mobil': jenis_mobil,
        'Merk': merk,
        'Tipe': tipe,
        'Tahun': tahun,
        'Stock': stock,
        '12 Jam': tarif_12jam,
        '24 Jam': tarif_24jam
    })

    #Menampilkan data mobil rental setelah menambahkan data baru
    data_mobil()
    
    # Validasi apakah user ingin menyimpan data yang sudah di input atau tidak (Jika tidak maka akan menghapus data yang sudah di input)
    while True:
        cek_tambah_mobil = input('Apakah anda ingin menyimpan data tersebut? [ya/tidak] : ')
        if cek_tambah_mobil.lower() == 'tidak':
            # Jika user tidak ingin menyimpan data maka akan menghapus data yang sudah di input            
            listMobil.pop()
            data_mobil()
            print('Data mobil tidak disimpan')
            break
        elif cek_tambah_mobil.lower() == 'ya':
            print(f'Data mobil: {merk} {tipe} tahun {tahun} berhasil ditambahkan')
            break
        else:
            print('input tidak tersedia')
            continue

##################################################################################

#Menghapus Data Mobil Rental (Menu 3.1)
def hapus_mobil():
    
    #Menampilkan data mobil rental sebelum menghapus data
    data_mobil()

    # Validasi inputan kode mobil harus berupa angka (Jika bukan angka maka akan terus mengulang inputan / looping)
    while True:
        try:
            kode_mobil = int(input('Masukkan kode mobil yang ingin dihapus : '))
            if kode_mobil < 0 or kode_mobil >= len(listMobil):
                # Jika kode mobil yang di input kurang dari 0 atau lebih dari panjang itterable di listMobil maka akan terus mengulang inputan / looping
                print('Kode mobil tidak valid')
                continue
            
            print(f'Anda akan menghapus data mobil {listMobil[kode_mobil]["Merk"]} {listMobil[kode_mobil]["Tipe"]} tahun {listMobil[kode_mobil]["Tahun"]}')
            cek_hapus_mobil = input('Apakah anda yakin ingin menghapus data mobil tersebut? [ya/tidak] : ')
            if cek_hapus_mobil.lower() == 'tidak':
                # Jika user tidak ingin menghapus data maka akan keluar dari looping / break
                print('Data mobil tidak dihapus')
                break
            elif cek_hapus_mobil.lower() == 'ya':
                del listMobil[kode_mobil]
                #Menampilkan data mobil rental setelah menghapus data
                data_mobil()
                print('Data mobil berhasil dihapus')
                break
            else:
                print('input tidak tersedia')
                continue
        except ValueError:
            # Jika kode mobil yang di input bukan berupa integer maka akan muncul pesan inputan harus berupa angka
            print('Inputan harus berupa angka')

##################################################################################

#Mengupdate Stock Mobil Rental (Menu 4.1)
def stock_mobil():
    #Menampilkan data mobil rental sebelum mengupdate stock mobil
    data_mobil()
    
    while True:
        try:
            kode_mobil = int(input('Masukkan kode mobil yang ingin diupdate stocknya : '))
            if kode_mobil < 0 or kode_mobil >= len(listMobil):
                # Jika kode mobil yang di input kurang dari 0 atau lebih dari panjang itterable di listMobil maka akan terus mengulang inputan / looping
                print('Kode mobil tidak valid')
                continue
            else:
                break
        except ValueError:
            # Jika kode mobil yang di input bukan berupa integer maka akan muncul pesan inputan harus berupa angka
            print('Inputan harus berupa angka')
            
    while True:
        try:
            stock = int(input('Masukkan stock mobil baru : '))
            if stock < 0:
                print('Stock mobil tidak boleh kurang dari 0')
                continue
            else:
                break
        except ValueError:
            print('Inputan harus berupa angka')
            
    while True:
        cek_stock_mobil = input('Apakah anda yakin ingin mengupdate stock mobil tersebut? [ya/tidak] : ')
        if cek_stock_mobil.lower() == 'ya':
            #Menambahkan data stock mobil yang sudah di input ke listMobil
            listMobil[kode_mobil]['Stock'] = stock
            #Menampilkan data mobil rental setelah mengupdate stock mobil
            data_mobil()
            print(f'Stock mobil {listMobil[kode_mobil]["Merk"]} {listMobil[kode_mobil]["Tipe"]} tahun {listMobil[kode_mobil]["Tahun"]} berhasil diupdate menjadi {stock}')
            break
        elif cek_stock_mobil.lower() == 'tidak':
            data_mobil()
            # Jika user tidak ingin mengupdate stock mobil maka akan keluar dari looping / break
            print('Stock mobil tidak diupdate')
            break      

##################################################################################

#Membuat Keranjang Penyewaan Mobil (Menu 5), dibuat global agar dapat diakses di fungsi lain dan juga value nya dapat di reset setelah melakukan pembayaran
daftar_penyewaan = []
total_harga = 0
    
#Membuat Fungsi Menyewa Mobil (Menu 5.1)
def sewa_mobil():
    
    #mengakses variabel global agar dapat diakses di fungsi lain
    global daftar_penyewaan
    global total_harga

    #While True dibuat agar user dapat menambahkan mobil yang disewa lebih dari 1 mobil
    while True: 
        
        #Menampilkan data mobil rental sebelum menyewa mobil
        data_mobil()
        
        # Validasi inputan kode mobil harus berupa angka (Jika bukan angka maka akan terus mengulang inputan / looping)
        while True:
            try:
                index_mobil = int(input("Masukkan kode mobil yang ingin disewa : "))
                # Validasi inputan kode mobil tidak boleh kurang dari 0 dan tidak boleh lebih dari panjang itterable di listMobil
                if index_mobil < 0 or index_mobil >= len(listMobil):
                    print('Kode mobil tidak valid')
                else:
                    break
            except ValueError:
                # Jika kode mobil yang di input bukan berupa integer maka akan muncul pesan inputan harus berupa angka
                print('Inputan harus berupa angka')
        
        # Validasi inputan lama sewa harus 12 jam atau 24 jam (Jika bukan 12 jam atau 24 jam maka akan terus mengulang inputan / looping)     
        while True:
            lama_sewa = input("Masukkan lama sewa [12 Jam / 24 Jam] : ")
            if lama_sewa in ['12 Jam', '24 Jam']:
                break
            else:
                print('Lama sewa tidak tersedia')
        
        #Stock mobil akan berkurang sesuai dengan jumlah mobil yang disewa
        while True:
            try:
                quantity = int(input('Masukkan jumlah mobil yang disewa : '))
                if quantity > listMobil[index_mobil]['Stock']:
                    print('Stock mobil tidak mencukupi')
                    return
                elif quantity <= 0:
                    print('Jumlah mobil yang disewa tidak bisa kurang dari 1')
                    return
                else:
                    listMobil[index_mobil]['Stock'] -= quantity
                    break
            except ValueError:
                # Jika jumlah mobil yang di input bukan berupa integer maka akan muncul pesan inputan harus berupa angka
                print('Inputan harus berupa angka')
        
        # Menambahkan data mobil yang disewa ke daftar_penyewaan           
        daftar_penyewaan.append({
            'Jenis Mobil': listMobil[index_mobil]['Jenis Mobil'],
            'Merk': listMobil[index_mobil]['Merk'],
            'Tipe': listMobil[index_mobil]['Tipe'],
            'Tahun': listMobil[index_mobil]['Tahun'],
            'Lama Sewa': lama_sewa,
            'Qty': quantity,
            'Tarif': listMobil[index_mobil][lama_sewa],
            'Total': listMobil[index_mobil][lama_sewa] * quantity,
        })

        # Menampilkan data mobil yang disewa dengan tabel yang rapih (Keranjang penyewaan)
        print('\t\t\t\t\t      List Mobil yang Disewa')
        print('+' + '-' * 111 + '+')
        print('| Jenis Mobil\t| Merk\t\t| Tipe\t\t| Tahun\t| Lama Sewa\t| Qty\t| Tarif\t\t| Total\t\t|')
        print('+' + '-' * 111 + '+')
        
        # Looping untuk menampilkan tabel data mobil rental dengan bebrapa kondisi agar tabel rapih
        for i in daftar_penyewaan:
            if len(i['Merk']) > 5 and len(i['Tipe']) > 5 :
                print(f'| {i["Jenis Mobil"]}\t\t| {i["Merk"]}\t| {i["Tipe"]}\t| {i["Tahun"]}\t| {i["Lama Sewa"]}\t| {i["Qty"]}\t| {i["Tarif"]}\t| {i["Total"]}\t|')
            elif len(i['Merk']) <= 5 and len(i['Tipe']) <= 5 :
                print(f'| {i["Jenis Mobil"]}\t\t| {i["Merk"]}\t\t| {i["Tipe"]}\t\t| {i["Tahun"]}\t| {i["Lama Sewa"]}\t| {i["Qty"]}\t| {i["Tarif"]}\t| {i["Total"]}\t|')
            elif len(i['Merk']) > 5 and len(i['Tipe']) <= 5 :
                print(f'| {i["Jenis Mobil"]}\t\t| {i["Merk"]}\t| {i["Tipe"]}\t\t| {i["Tahun"]}\t| {i["Lama Sewa"]}\t| {i["Qty"]}\t| {i["Tarif"]}\t| {i["Total"]}\t|')
            elif len(i['Merk']) <= 5 and len(i['Tipe']) > 5 :
                print(f'| {i["Jenis Mobil"]}\t\t| {i["Merk"]}\t\t| {i["Tipe"]}\t| {i["Tahun"]}\t| {i["Lama Sewa"]}\t| {i["Qty"]}\t| {i["Tarif"]}\t| {i["Total"]}\t|')
        
        print('+' + '-' * 111 + '+')

        #Check apakah user ingin menambah mobil yang disewa atau tidak, jika tidak maka akan keluar dari looping / break
        while True:
            tambah_lagi = input('Apakah anda ingin menambah mobil yang disewa? [ya/tidak] : ')
            if tambah_lagi.lower() == 'tidak':
                print('Silahkan lanjut ke menu pembayaran sewa jika sudah selesai atau kembali ke menu utama jika ingin membatalkan penyewaan')
                return
            elif tambah_lagi.lower() == 'ya':
                break
            else:
                print('input tidak tersedia')
        
            
#Membuat Fungsi Cek Keranjang Penyewaan (Menu 5.2)
def cek_keranjang_penyewaan():
    # Menampilkan data mobil yang disewa dengan tabel yang rapih (kreanjang penyewaan)
    print('\t\t\t\t\t      List Mobil yang Disewa')
    print('+' + '-' * 111 + '+')
    print('| Jenis Mobil\t| Merk\t\t| Tipe\t\t| Tahun\t| Lama Sewa\t| Qty\t| Tarif\t\t| Total\t\t|')
    print('+' + '-' * 111 + '+')
        
    # Looping untuk menampilkan tabel data mobil rental dengan bebrapa kondisi agar tabel rapih
    for i in daftar_penyewaan:
        if len(i['Merk']) > 5 and len(i['Tipe']) > 5 :
            print(f'| {i["Jenis Mobil"]}\t\t| {i["Merk"]}\t| {i["Tipe"]}\t| {i["Tahun"]}\t| {i["Lama Sewa"]}\t| {i["Qty"]}\t| {i["Tarif"]}\t| {i["Total"]}\t|')
        elif len(i['Merk']) <= 5 and len(i['Tipe']) <= 5 :
            print(f'| {i["Jenis Mobil"]}\t\t| {i["Merk"]}\t\t| {i["Tipe"]}\t\t| {i["Tahun"]}\t| {i["Lama Sewa"]}\t| {i["Qty"]}\t| {i["Tarif"]}\t| {i["Total"]}\t|')
        elif len(i['Merk']) > 5 and len(i['Tipe']) <= 5 :
            print(f'| {i["Jenis Mobil"]}\t\t| {i["Merk"]}\t| {i["Tipe"]}\t\t| {i["Tahun"]}\t| {i["Lama Sewa"]}\t| {i["Qty"]}\t| {i["Tarif"]}\t| {i["Total"]}\t|')
        elif len(i['Merk']) <= 5 and len(i['Tipe']) > 5 :
            print(f'| {i["Jenis Mobil"]}\t\t| {i["Merk"]}\t\t| {i["Tipe"]}\t| {i["Tahun"]}\t| {i["Lama Sewa"]}\t| {i["Qty"]}\t| {i["Tarif"]}\t| {i["Total"]}\t|')
        
    print('+' + '-' * 111 + '+')
    
    
#Membuat Fungsi Pembayaran Sewa (Menu 5.3)
def pembayaran_sewa():
    global daftar_penyewaan
    global total_harga
    
    if len(daftar_penyewaan) == 0:
        print('Anda belum menyewa mobil')
        return
    else:
        for i in daftar_penyewaan:
            total_harga += i['Total']
        while True:
            try:
                print(f'Total Yang Harus Dibayar = {total_harga}')
                jml_uang = int(input('Masukkan jumlah uang : '))
                if(jml_uang > total_harga) :
                    kembali = jml_uang - total_harga
                    print(f'Terima kasih \n\nUang kembali anda : {kembali}')
                    break
                elif(jml_uang == total_harga) :
                    print('Terima kasih')
                    break
                elif jml_uang < total_harga:
                    kekurangan = total_harga - jml_uang
                    print(f'Uang anda kurang sebesar {kekurangan}')
            except ValueError:
                # Jika jumlah uang yang di input bukan berupa integer maka akan muncul pesan inputan harus berupa angka
                print('Inputan harus berupa angka')
        
    # Reset value daftar_penyewaan dan total_harga agar user dapat menyewa mobil lagi
    daftar_penyewaan = []
    total_harga = 0
    
##################################################################################

#Sub Menu

#SUB Menu 1
def sub_menu_data_mobil():
    while True:
        menu1 = input ('''
+=========================================+
|               List Menu 1               |
+=========================================+
| 1. Data Mobil Keseluruhan               |
| 2. Filter Data Mobil Berdasarkan Merk   |   
| 3. Kembali ke Menu Utama                |
+=========================================+
Masukkan pilihan menu : ''')
        
        if menu1 == '1':
            data_mobil()
        elif menu1 == '2':
            filter_mobil()
        elif menu1 == '3':
            break
        else:
            print('Pilihan menu tidak tersedia')

#SUB Menu 2
def sub_menu_tambah_mobil():
    while True:
        menu2 = input ('''
+====================================+
|             List Menu 2            |
+====================================+
| 1. Tambah Data Mobil               |
| 2. Kembali ke menu utama           |
+====================================+
Masukkan pilihan menu : ''')
        
        if menu2 == '1':
            tambah_mobil()
        elif menu2 == '2':
            break
        else:
            print('Pilihan menu tidak tersedia')
        
#SUB Menu 3
def sub_menu_hapus_mobil():
    while True:
        menu3 = input ('''
+====================================+
|             List Menu 3            |
+====================================+
| 1. Hapus Data Mobil                |
| 2. Kembali ke menu utama           |
+====================================+
Masukkan pilihan menu : ''')
        
        if menu3 == '1':
            hapus_mobil()
        elif menu3 == '2':
            break
        else:
            print('Pilihan menu tidak tersedia')

#SUB Menu 4
def sub_menu_stock_mobil():
    while True:
        menu4 = input ('''
+====================================+
|             List Menu 4            |
+====================================+
| 1. Update Stock Mobil              |
| 2. Kembali ke menu utama           |
+====================================+
Masukkan pilihan menu : ''')
        
        if menu4 == '1':
            stock_mobil()
        elif menu4 == '2':
            break
        else:
            print('Pilihan menu tidak tersedia')

#SUB Menu 5
def sub_menu_sewa_mobil():
    while True:
        menu5 = input ('''
+============================================+
|                 List Menu 5                |
+============================================+
| 1. Tambah Penyewaan Mobil                  |
| 2. Cek Keranjang Penyewaan Mobil           |
| 3. Pembayaran & Finalisasi Sewa            |   
| 4. Pembatalan Sewa & kembali ke menu utama |
+============================================+
Masukkan pilihan menu : ''')
        
        if menu5 == '1':
            sewa_mobil()
        elif menu5 == '2':
            cek_keranjang_penyewaan()
        elif menu5 == '3':
            pembayaran_sewa()
            #Setelah melakukan pembayaran maka akan kembali ke menu utama
        elif menu5 == '4':
            print('Penyewaan mobil selesai')
            break
        else:
            print('Pilihan menu tidak tersedia')
        
##################################################################################

# Menu Utama Program Rental Mobil
def menu_utama():
    while True:
        pilihan_menu = input('''
+====================================+
|   Selamat Datang di Rental Mobil   |
+====================================+    
| List Menu :                        |
| 1. Menampilkan Daftar Mobil Rental |
| 2. Menambahkan Data Mobil Rental   |
| 3. Menghapus Data Mobil Rental     |
| 4. Update Stock Mobil Rental       |  
| 5. Menyewa Mobil                   |
| 6. Keluar                          |
+====================================+      
Masukkan pilihan menu : ''')        

        if pilihan_menu == '1':
            sub_menu_data_mobil()
        elif pilihan_menu == '2':
            sub_menu_tambah_mobil()
        elif pilihan_menu == '3':
            sub_menu_hapus_mobil()
        elif pilihan_menu == '4':
            sub_menu_stock_mobil()
        elif pilihan_menu == '5':
            sub_menu_sewa_mobil()
        elif pilihan_menu == '6':
            print('Terima kasih telah menggunakan program rental mobil kami')
            break
        else:
            print('Pilihan menu tidak tersedia')


#Memanggil fungsi menu_utama()
menu_utama()