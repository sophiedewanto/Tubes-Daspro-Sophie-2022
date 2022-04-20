def keluar():
    while True:
        y = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if y == "y" or y == "Y":
            save(data)
            exit()
        elif y == "n" or y == "N":
            exit()

keluar()