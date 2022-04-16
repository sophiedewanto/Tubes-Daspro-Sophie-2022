data_user = [["id","username","nama","password","role","saldo"], 
            [0,"rafi","rafi","rafi","admin",10000], 
            [1,"bat_man","batman","kelelawar","user",30000], 
            [2,"baim","ibrahim","baimsipsip","user",50000],
            [3,"ard_studios","ardhan","dandan123","user",40000],
            [4,"super_man","superman","kuat","user",20000]]

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

def topup(data):
    username = input("Masukan username: ")
    tambah_saldo = int(input("Masukan saldo: "))
    if 0 < search(username,data,1) < length(data):
        saldo = data[search(username,data,1)][5] + tambah_saldo
        if tambah_saldo < 0:
            if (-tambah_saldo) > data[search(username,data,1)][5]:
                print("Masukan tidak valid.")
            else:
                print(f"Top up berhasil. Saldo {username} berkurang menjadi {saldo}.")
        else:
            print(f"Top up berhasil. Saldo {username} bertambah menjadi {saldo}.")
    else:
        print(f"Username {username} tidak ditemukan.")
    
    return data

topup(data_user)