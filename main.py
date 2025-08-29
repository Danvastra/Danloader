from pytubefix import YouTube
import os
import platform
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

while True:
    def clear_terminal():
        # Mengecek sistem operasi dan membersihkan terminal sesuai
        if platform.system() == "Windows":
            os.system('cls')  # Untuk Windows
        else:
            os.system('clear')  # Untuk Linux/macOS

    # Panggil fungsi untuk membersihkan terminal
    clear_terminal()

    print(f"{Fore.WHITE}________________________________")
    print(f"\n{Fore.YELLOW} + Danloader v1 {Fore.WHITE}by {Fore.LIGHTRED_EX}Danvastra {Fore.YELLOW}+ ")
    print(f"{Fore.WHITE}________________________________")

    def download_youtube_video():
        try:
            print(f"\n{Fore.YELLOW} + {Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}Valid URL{Fore.LIGHTWHITE_EX}] : {Fore.LIGHTCYAN_EX}https://www.youtube.com {Fore.LIGHTRED_EX}or {Fore.LIGHTCYAN_EX}https://youtu.be {Fore.LIGHTRED_EX}")
            
            # Input URL video
            link = input(f"{Fore.YELLOW} + {Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}Masukkan URL video {Fore.LIGHTRED_EX}YouTube{Fore.LIGHTWHITE_EX}] : {Fore.WHITE}").strip()
            
            # Validasi URL
            if not (link.startswith("https://www.youtube.com") or link.startswith("https://youtu.be")):
                print(f"{Fore.YELLOW} + {Fore.RED}❌ URL tidak valid. Masukkan URL video YouTube yang benar.")
                return

            yt = YouTube(link)
            
            # Informasi video
            print(f"\n{Fore.YELLOW} + {Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}Judul Video{Fore.LIGHTWHITE_EX}] : {Fore.LIGHTYELLOW_EX}{yt.title}")
            print(f"{Fore.YELLOW} + {Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}Channel{Fore.LIGHTWHITE_EX}] : {Fore.LIGHTYELLOW_EX}{yt.author}")
            print(f"{Fore.YELLOW} + {Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}Durasi{Fore.LIGHTWHITE_EX}] : {Fore.LIGHTYELLOW_EX}{yt.length} detik")
            print(f"{Fore.YELLOW} + {Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}Views{Fore.LIGHTWHITE_EX}] : {Fore.LIGHTYELLOW_EX}{yt.views}\n")
            
            # Pilih format download (MP4 atau MP3)
            print(f"{Fore.YELLOW} + {Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}Pilih format download{Fore.LIGHTWHITE_EX}] :")
            print(f"{Fore.YELLOW} + {Fore.GREEN}1. MP4 (Video)")
            print(f"{Fore.YELLOW} + {Fore.GREEN}2. MP3 (Audio)")

            choice = input(f"{Fore.YELLOW} + {Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}Masukkan pilihan (1/2){Fore.LIGHTWHITE_EX}] : {Fore.WHITE}").strip()
            
            if choice not in ['1', '2']:
                print(f"{Fore.YELLOW} + {Fore.RED}❌ Pilihan tidak valid! Harap pilih antara 1 atau 2.")
                return
            
            # Lokasi penyimpanan
            save_path = input(f"{Fore.YELLOW} + {Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}Masukkan lokasi penyimpanan{Fore.LIGHTWHITE_EX}] : {Fore.WHITE}").strip()
            if not save_path:
                save_path = os.getcwd()
            
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            # Download video atau audio sesuai pilihan
            if choice == '1':
                print(f"\n{Fore.YELLOW} + {Fore.LIGHTRED_EX}Mengunduh video dengan kualitas tertinggi MP4...")
                stream = yt.streams.get_highest_resolution()  # MP4 kualitas terbaik
                stream.download(output_path=save_path)
                print(f"\n{Fore.YELLOW} + {Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}Video berhasil diunduh ke{Fore.LIGHTWHITE_EX}] : {Fore.LIGHTYELLOW_EX}{os.path.join(save_path, stream.default_filename)}")

            elif choice == '2':
                print(f"\n{Fore.YELLOW} + {Fore.LIGHTRED_EX}Mengunduh audio MP3...")
                stream = yt.streams.filter(only_audio=True).first()  # MP3 (hanya audio)
                audio_file = stream.download(output_path=save_path)
                # Convert file ke MP3
                base, ext = os.path.splitext(audio_file)
                new_file = base + '.mp3'
                os.rename(audio_file, new_file)
                print(f"\n{Fore.YELLOW} + {Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}Audio MP3 berhasil diunduh ke{Fore.LIGHTWHITE_EX}] : {Fore.LIGHTYELLOW_EX}{new_file}")

        except Exception as e:
            print(f"\n{Fore.YELLOW} + {Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX} Terjadi kesalahan{Fore.LIGHTWHITE_EX}] : {e}")

    if __name__ == "__main__":
        download_youtube_video()

    lanjutDownload = input(f"{Fore.YELLOW} + {Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}Mau Lanjut Download Lagi(y/n){Fore.LIGHTWHITE_EX}] : ").lower()
    if lanjutDownload != "y":
        print("\n")
        print(f"{Fore.YELLOW} + {Fore.LIGHTCYAN_EX}Terimakasih Sudah Mencoba Program ini!")
        break
