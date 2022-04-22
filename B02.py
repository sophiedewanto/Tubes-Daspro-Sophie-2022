import time

pertanyaan = input("Apa pertanyaanmu? ")

time = int(time.time()*1000)

jawaban = ["Ya","Tidak mungkin","Bisa jadi","Coba tanya lagi","Tidak","Tentunya","Mungkin","Kurasa tidak","Harus","Mungkin suatu hari"]

print(jawaban[time%10])