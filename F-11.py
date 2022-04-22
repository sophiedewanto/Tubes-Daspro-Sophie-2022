data_game = [['id', 'nama', 'kategori', 'tahun_rilis', 'harga', 'stok'], 
            ['GAME001', 'Journey', 'Adventure', '2020', '120000', '3'], 
            ['GAME002', 'Hitman 3', 'Action', '2021', '370000', '5'], 
            ['GAME003', 'Skyrim', 'RPG', '2011', '200000', '1'], 
            ['GAME004', 'Forza Horizon 5', 'Racing', '2021', '550000', '9'], 
            ['GAME005', 'Sekiro', 'Action', '2019', '250000', '0']]

def length(list):
    index = 0
    for i in list :
        index += 1 
    return index 

def search_game_at_store(data):
    id = input("Masukkan ID Game: ")
    nama = input("Masukkan Nama Game: ")
    harga = input("Masukkan Harga Game: ")
    kategori = input("Masukkan Kategori Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")
    newlist = []

    for i in range (1,length(data)):
        if (id == data[i][0] or id==""):
            if (nama == data[i][1] or nama==""):
                if (kategori == data[i][2] or kategori==""):
                    if (tahun_rilis == data [i][3] or tahun_rilis==""):
                        if (harga == data[i][4] or harga==""):
                            newlist += [[data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5]]]
    print("")
    if length(newlist) == 0:
        print("Tidak ada game pada toko yang memenuhi kriteria")
    else:
        print("Daftar game pada toko yang memenuhi kriteria:")
        for i in range(length(newlist)):
            for j in range(5):
                print(newlist[i][j],end="|")
            for j in range(5,6):
                print(newlist[i][j])

search_game_at_store(data_game)
