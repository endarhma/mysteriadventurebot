import time
import random


COLORS = {
    'reset': '\033[0m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'bright_red': '\033[1;31m',
    'bright_green': '\033[1;32m',
    'bright_yellow': '\033[1;33m',
    'bright_cyan': '\033[1;36m',
}


def say(text, color=None, end='\n'):
    prefix = COLORS.get(color, '') if color else ''
    suffix = COLORS['reset'] if prefix else ''
    print(f"{prefix}{text}{suffix}", end=end, flush=True)
    time.sleep(0.5)


SWORD_ART = r"""
    />_________________________________
[########[]_________________________________>
    \\
"""

SKULL_ART = r"""
    .-.
      (o.o)
    |=|
      __|__
    //.=|=.\\
   // .=|=. \\
   \\ .=|=. //
    \\(_=_)//
     (:| |:)
      || ||
      () ()
      || ||
      || ||
     ==' '==
"""

def game_utama():
    say("✨ --- MEMULAI PETUALANGAN DIGITAL --- ✨", color='magenta')
    nama = input("Siapa namamu? ")
    say(f"👋 Selamat datang, {nama}!", color='cyan')
    nyawa = 100
    path = None
    while True:
        say("Pilih jalur petualanganmu: 🎒", color='bright_yellow')
        say("1) Lembah Coding 💻", color='green')
        say("2) Gunung Bug 🏔️🐛", color='red')
        pilihan = input("Masukkan pilihan (1/2 atau nama jalur): ").strip().lower()
        if pilihan in ("1", "lembah coding", "lembah", "l"):
            path = "lembah"
            break
        elif pilihan in ("2", "gunung bug", "gunung", "g"):
            path = "gunung"
            break
        else:
            nyawa -= 20
            if nyawa <= 0:
                say("\n⚠️ Pilihan tidak valid! Nyawa -20.", color='bright_red')
                say("💥 Nyawa habis. Permainan berakhir.", color='bright_red')
                return
            say(f"\n⚠️ Pilihan tidak valid! Nyawa -20. Sisa nyawa: {nyawa} 💫", color='bright_yellow')
            say("Coba lagi.\n", color='yellow')

    if path == "lembah":
        say("\nKau melangkah menuju Lembah Coding, di mana baris kode tumbuh seperti rumput.")
        say("Seorang mentor bijak menantangmu menyelesaikan teka-teki logika dan debugging kecil.")
        success = random.random() < 0.8
    elif path == "gunung":
        say("\nKau memulai pendakian ke Gunung Bug, puncaknya dipenuhi tantangan tak terduga.")
        say("Di gunung ini, setiap langkah mungkin memicu error baru yang harus kau atasi.")
        success = random.random() < 0.5

    say("Tiba-tiba, sebuah tantangan muncul... ✨", color='bright_cyan')
    if success:
        for line in SWORD_ART.splitlines():
            say(line, color='bright_green')
        say("🗡️✨ Kau berhasil! Keberuntungan berpihak padamu.", color='bright_green')
    else:
        for line in SKULL_ART.splitlines():
            say(line, color='bright_red')
        nyawa -= 50
        if nyawa <= 0:
            say("\n💀 Kekalahan fatal. Nyawa habis. Permainan berakhir.", color='bright_red')
            return
        say(f"\n☠️ Kau gagal kali ini. Nyawa -50. Sisa nyawa: {nyawa}", color='red')

    say(f"\nPetualangan berlanjut... (Nyawa: {nyawa})")
    
if __name__ == "__main__":
    while True:
        game_utama()
        again = input("\nMain lagi? (y/n): 🔁 ").strip().lower()
        if again in ("y", "yes"):
            say("🔁 Baik, memulai ulang permainan...\n", color='bright_cyan')
            continue
        else:
            say("🙏✨ Terima kasih telah bermain! Sampai jumpa.", color='magenta')
            break