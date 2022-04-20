def keluar():
    while True:
        save_and_exit = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if save_and_exit == "y" or y == "Y":
            save(data)
            exit()
        elif save_and_exit == "n" or y == "N":
            exit()

keluar()