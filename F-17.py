def keluar():
    while True:
        save_and_exit = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if save_and_exit == "y" or save_and_exit == "Y":
            save(data)
            exit()
        elif save_and_exit == "n" or save_and_exit == "N":
            exit()

keluar()