import sys
from time import sleep
from playsound import playsound
import threading

def print_lirik():
    lyrics = [
        ("Satu Bulan", 0.2, 0.24),
        
        # Nambah space
        ("", 0, 0),  # Space
        
        ("Belum ada satu bulan..", 1.2, 2.0),
        ("Ku yakin masih ada sisa wangiku di bajumu", 1.4, 0.8),
        ("Namun, kau tampak baik saja", 0.6, 0.0),
        ("Bahkan senyummu lebih lepas", 0.0, 0.0),
        ("Sedang aku di sini hampir... gila", 0.1, 4.0),
        
        # Nambah space
        ("", 0, 0),  # Space
        
        ("Kita tak temukan jalan", 1.4, 1.5),
        ("Sepakat akhiri setelah beribu debat panjang", 2.0, 0.5),
        ("Namun kau tampak baik saja", 0.0, 0.0),
        ("Bahkan senyummu lebih lepas", 0.0, 0.0),
        ("Sedang aku di sini belum terima", 0.1, 3.2),
        
        # Nambah space
        ("", 0, 0),  # Space
        
        ("Bohongkah tangismu sore itu di pelukku?", 0.8, 0.5),
        ("Nyatanya pergiku pun tak lagi mengganggumu", 1.0, 0.7),
        ("Apa sudah ada kabar lain yang kautunggu?", 1.0, 0.3),
        
        # Nambah space
        ("", 0, 0),  # Space
        
        ("Sudah adakah yang gantikanku", 1.0, 1.2),
        ("Yang khawatirkanmu setiap waktu", 1.0, 1.3),
        ("Yang cerita tentang apa pun sampai hal-hal tak perlu", 1.1, 0.0),
        ("Kalau bisa, jangan buru-buru", 0.0, 1.9),
        ("Kalau bisa, jangan ada dulu", 0.7, 11.3),
        
        # Nambah space
        ("", 0, 0),  # Space
        
        ("Baru lewat satu bulan..", 1.1, 1.4),
        ("Kemarin ulang tahunku tak ada pesan darimu", 1.2, 0.7),
        ("Tak apa, mungkin kau lupa", 1.2, 0.8),
        ("Atau sudah ada hati yang harus kaujaga", 1.3, 0.6),
        
        # Nambah space
        ("", 0, 0),  # Space
        
        ("Sudah adakah yang gantikanku", 1.1, 1.0),
        ("Yang kauantar-jemput setiap Sabtu", 1.2, 0.9),
        ("Yang selalu ingatkan untuk pakai sabuk pengamanmu", 1.4, 0.0),
        ("Kalau bisa, jangan buru-buru", 1.0, 0.9),
        
        # Nambah space
        ("", 0, 0),  # Space
        
        ("Sudah adakah yang gantikanku", 1.2, 1.7),
        ("Yang khawatirkanmu setiap waktu", 1.2, 1.3),
        ("Yang cerita tentang apa pun sampai hal-hal tak perlu", 1.3, 0.0),
        ("Kalau bisa, jangan buru-buru", 0.0, 0.8),
        ("Kalau bisa, jangan ada dulu", 1.1, 11.4),
        
        # Nambah space
        ("", 0, 0),  # Space
        
        ("Hu-hu-uh", 1.4, 1.6),
        ("Hu-uh", 1.5, 0.8)
    ]
    
    for line, char_delay, extra_delay in lyrics:
        for char in line:
            print(char, end='', flush=True)  # Print per karakter
            sleep(0.1)  # Jeda per karakter
        print()  # Pindah ke baris baru setelah satu lirik selesai
        
        if char_delay > 0:
            sleep(char_delay)
        if extra_delay > 0:
            sleep(extra_delay)

def play_music():
    playsound('D:/Project Nathan/Python/Satu Bulan/Satu_Bulan.mp3') # Ganti dengan path file lagu yang kamu save

if __name__ == "__main__":
    print("=========================")
    print("Author: [Nathaniel Tee]")
    print("License: MIT License")
    print("=========================")

    # Membuat thread untuk memutar lagu
    music_thread = threading.Thread(target=play_music)
    music_thread.start()

    # Menampilkan lirik
    print_lirik()

    # Menunggu lagu selesai
    music_thread.join()
