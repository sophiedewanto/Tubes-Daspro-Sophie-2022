data_game = [['id', 'nama', 'kategori', 'tahun_rilis', 'harga', 'stok'], 
            ['GAME001', 'Journey', 'Adventure', 2020, 120000, 3], 
            ['GAME002', 'Hitman 3', 'Action', 2021, 370000, 5], 
            ['GAME003', 'Skyrim', 'RPG', 2011, 200000, 1], 
            ['GAME004', 'Forza Horizon 5', 'Racing', 2021, 550000, 9], 
            ['GAME005', 'Sekiro', 'Action', 2019, 250000, 0]]

def length(list):
    index = 0
    for i in list :
        index += 1 
    return index 

def search(index,data,column):
    x = 0
    for i in range (length(data)):
        if index != data[i][column]:
            x += 1
        elif index == data[i][column]:
            break
    return x

def ubah_stok(data):
    id = input("Masukan ID game: ")
    jumlah = int(input("Masukan jumlah: "))
    if 0 < search(id,data,0) < length(data):
        stok = data[search(id,data,0)][5] + jumlah
        if jumlah < 0:
            if (-jumlah) > data[search(id,data,0)][5]:
                print(f"Stok game {data[search(id,data,0)][1]} gagal dikurangi karena stok kurang. Stok sekarang: {data[search(id,data,0)][5]} (<{(-jumlah)})")
            else:
                print(f"Stok game {data[search(id,data,0)][1]} berhasil dikurangi. Stok sekarang: {stok}")
        else:
            print(f"Stok game {data[search(id,data,0)][1]} berhasil ditambahkan. Stok sekarang: {stok}")
    else:
        print("Tidak ada game dengan ID tersebut!")
    
    return data

ubah_stok(data_game)