import random

def tebak_angka():
    print("\n🎉 Selamat datang di Game Tebak Angka! 🎉")
    print("Saya telah memilih angka antara 1 dan 100. Coba tebak!")

    angka_rahasia = random.randint(1, 100)
    percobaan = 0

    while True:
        try:
            tebak = int(input("Masukkan tebakanmu: "))
            percobaan += 1

            if tebak < 1 or tebak > 100:
                print("🚫 Tebakan harus antara 1 dan 100!")
            elif tebak < angka_rahasia:
                print("🔻 Terlalu rendah!")
            elif tebak > angka_rahasia:
                print("🔺 Terlalu tinggi!")
            else:
                print(f"🎊 Benar! Angka yang dipilih adalah {angka_rahasia}.")
                print(f"Kamu menebaknya dalam {percobaan} percobaan.")
                break
        except ValueError:
            print("⚠️ Masukkan angka yang valid!")

if __name__ == "__main__":
    tebak_angka()
