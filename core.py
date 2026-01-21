# core.py
# CipherBloom - PurpleRose Decoder

import os
from colorama import Fore, Style, init
from base64_decoder import decode_base64
from gzip_decoder import decode_gzip
from zlib_decoder import decode_zlib

init(autoreset=True)

def banner():
    print(Fore.MAGENTA + Style.BRIGHT + r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⢔⣒⠂⣀⣀⣤⣄⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⣿⠋⢠⣟⡼⣷⠼⣆⣼⢇⣿⣄⠱⣄
⠀⠀⠀⠀⠀⠀⠀⠹⣿⡀⣆⠙⠢⠐⠉⠉⣴⣾⣽⢟⡰⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⠀⠤⢴⣿⠿⢋⣴⡏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡙⠻⣿⣶⣦⣭⣉⠁⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠈⠉⠉⠉⠉⠇⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⣘⣦⣀⠀⠀⣀⡴⠊⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⢻⣿⣿⣿⣿⠻⣧⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠫⣿⠉⠻⣇⠘⠓⠂⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
    print(Fore.MAGENTA + Style.BRIGHT + "PurpleRose - CipherBloom Decoder\n")

def detect_format(data: bytes) -> str:
    try:
        decode_base64(data)
        return "Base64"
    except Exception:
        pass
    try:
        decode_zlib(data)
        return "zlib"
    except Exception:
        pass
    try:
        decode_gzip(data)
        return "gzip"
    except Exception:
        pass
    return "Unknown"

def save_output(decoded: bytes, outname: str):
    try:
        text = decoded.decode("utf-8")
        with open(outname, "w", encoding="utf-8") as f:
            f.write(text)
        print(Fore.GREEN + f"[√] Saved as text: {outname}")
    except Exception:
        with open(outname, "wb") as f:
            f.write(decoded)
        print(Fore.GREEN + f"[√] Saved as binary: {outname}")

def run_decoder():
    banner()
    filename = input(Fore.YELLOW + "File path: ").strip()
    if not os.path.exists(filename):
        print(Fore.RED + "[×] File not found.")
        return

    with open(filename, "rb") as f:
        raw = f.read().strip()

    outname = input(Fore.YELLOW + "Output file: ").strip()
    fmt = detect_format(raw)
    print(Fore.CYAN + f"[?] Format detected: {fmt}")

    if fmt == "Base64":
        decoded = decode_base64(raw)
    elif fmt == "zlib":
        decoded = decode_zlib(raw)
    elif fmt == "gzip":
        decoded = decode_gzip(raw)
    else:
        print(Fore.RED + "[×] Format not recognized.")
        return

    save_output(decoded, outname)

def main():
    while True:
        run_decoder()
        choice = input(Fore.YELLOW + "\nSelect option: [1] Continue  [2] Exit → ").strip()
        if choice == "1":
            continue  # restart loop
        elif choice == "2":
            print(Fore.MAGENTA + "Exiting... PurpleRose Decoder closed.")
            break
        else:
            print(Fore.RED + "Invalid choice. Exiting.")
            break

if __name__ == "__main__":
    main()
