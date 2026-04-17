import math

def hitung_pangkat():
    try:
        angka = int(input("masukkan suatu bilangan bulat : "))
        pangkat_max = int(input("masukkan pangkat yang diinginkan : "))
        
        for i in range(1, pangkat_max + 1):
            hasil = int(math.pow(angka, i))
            print(f"hasil {angka} pangkat {i} adalah {hasil}")
    except ValueError:
        print("Input harus berupa angka bulat!")

def hitung_deret():
    try:
        n = int(input("Masukkan jumlah N : "))
        
        fib = [1, 1]
        for i in range(2, (n * 2) + 5):
            fib.append(fib[-1] + fib[-2])
        
        total = 0.0
        for i in range(n):
            if i == 0:
                total = 1.0
            else:
                pembilang = fib[i * 2]
                penyebut = fib[(i * 2) + 1] 
                
                if i % 2 != 0:
                    total -= (pembilang / penyebut)
                else:
                    total += (pembilang / penyebut)
        
        print(f"{total:.7f}")
    except ValueError:
        print("Input harus berupa angka!")

def main():
    while True:
        print("\nNim Ganjil")
        print("1. A pangkat B")
        print("2. Hitung 1 - 2/3 + 5/8 - 13/21 + ...")
        print("0. keluar")
        
        pilihan = input("Masukkan : ")
        
        if pilihan == '1':
            hitung_pangkat()
        elif pilihan == '2':
            hitung_deret()
        elif pilihan == '0':
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()