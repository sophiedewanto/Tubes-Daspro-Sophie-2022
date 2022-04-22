def kerangajaib():
    import time

    pertanyaan = input("Apa pertanyaanmu? ")
    time = int(time.time()*1000)
    jawaban = ["Ya","Tidak mungkin","Bisa jadi","Coba tanya lagi","Tidak","Tentunya","Mungkin","Kurasa tidak","Pasti","Mungkin suatu hari"]
    return(print(jawaban[time%10]))

kerangajaib()