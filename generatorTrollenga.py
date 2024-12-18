import random
import time
from pystyle import Write, Colors, Colorate

def load_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.readlines()

provocations = load_file('pr.txt')
poems = load_file('stixi.txt')

banwords = []
line_count = 4
generation_tempo = 1.0

def create_poem():
    global poems, line_count
    return ''.join(random.choices(poems, k=line_count))

def create_provocation():
    global provocations, line_count
    return ''.join(random.choices(provocations, k=line_count))

def add_banword(word):
    global banwords
    banwords.append(word)

def display_logo(theme):
    logo = f"""
    ⠤⣤⣤⣤⣄⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⠤⠤⠴⠶⠶⠶⠶
     ⢠⣤⣤⡄⣤⣤⣤⠄⣀⠉⣉⣙⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠘⣉⢡⣤⡤⠐⣶⡆⢶⠀⣶⣶⡦
     ⣄⢻⣿⣧⠻⠇⠋⠀⠋⠀⢘⣿⢳⣦⣌⠳⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠞⣡⣴⣧⠻⣄⢸⣿⣿⡟⢁⡻⣸⣿⡿⠁
     ⠈⠃⠙⢿⣧⣙⠶⣿⣿⡷⢘⣡⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣷⣝⡳⠶⠶⠾⣛⣵⡿⠋⠀⠀
⠀⠀⠀⠀ ⠉⠻⣿⣶⠂⠘⠛⠛⠛⢛⡛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠀⠉⠒⠛⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀ ⠀⣿⡇⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀ ⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀ ⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀ ⠀⠀⢻⡁⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀ ⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀ ⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀ ⠀⠀⠀⠿⠀⠀⠀⠀⠀⠀⠀⠀
"""
    print (Colorate.Horizontal(theme, logo))

def display_menu(theme):
    menu_text = """
    
    
    [1] Buat sajak
    [2] Ciptakan Provokasi
    [3] Ubah Jumlah Baris
    [4] Ubah Tingkat Generasi
    [5] Tambahkan Kata Ban
    [6] Tema
    [7] Exit
    
    
"""
    Write.Print(menu_text, theme, interval=0.01)

def main():
    global line_count, generation_tempo

    current_theme = Colors.red_to_yellow
    display_logo(current_theme)

    while True:
        display_menu(current_theme)
        choice = input("Pilih sebuah opsi: ")

        if choice == '1':
            poem = create_poem()
            for word in banwords:
                poem = poem.replace(word, '*' * len(word))
            print(f"\n{Colorate.Horizontal(current_theme, poem)}\n")

        elif choice == '2':
            provocation = create_provocation()
            for word in banwords:
                provocation = provocation.replace(word, '*' * len(word))
            print(f"\n{Colorate.Horizontal(current_theme, provocation)}\n")

        elif choice == '3':
            line_count = int(input("Masukkan jumlah baris baru: "))

        elif choice == '4':
            generation_tempo = float(input("Masukkan kecepatan generasi baru (dalam hitungan detik): "))

        elif choice == '5':
            banword = input("Masukkan kata larangan: ")
            add_banword(banword)

        elif choice == '7':
            break

        elif choice == '6':
            print ("Pilih tema baru:")
            print ("1. red_to_yellow")
            print ("2. green_to_blue")
            new_theme_choice = input("Masukkan nomor topik baru: ")
            if new_theme_choice == '1':
                current_theme = Colors.red_to_yellow
            elif new_theme_choice == '2':
                current_theme = Colors.green_to_blue
            else:
                print ("Pemilihan topik salah, coba lagi.")

        else:
            print ("Pilihan salah, coba lagi.")

        time.sleep(generation_tempo)

if __name__ == "__main__":
    main()
