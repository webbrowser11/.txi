import sys
import time
import shutil
from txi_encode import encode_txt_to_txi
from txi_decode import decode_txi_to_txt  # type: ignore[import]

def print_banner():
    banner = [
        "╔══════════════════════════════════════════╗",
        "║              The .txi Project            ║",
        "║            (c) 2025 Webbrowser11         ║",
        "║         Licensed under MIT License       ║",
        "╚══════════════════════════════════════════╝",
    ]
    width = shutil.get_terminal_size().columns
    for line in banner:
        print(line.center(width))
    print()

def run_all():
    print_banner()
    while True:
        print("\nChoose an option:")
        print(" 1. Convert .txt ➔ .txi (raw, human-readable)")
        print(" 2. Convert .txi ➔ .txt (raw)")
        print(" Q. Quit")
        print("Please note: .txi files now contain your text directly—fully human-readable.")

        choice = input("\nEnter your choice (1, 2, or Q): ").strip().lower()
        if choice == "1":
            encode_txt_to_txi()
        elif choice == "2":
            decode_txi_to_txt()
        elif choice == "q":
            print("\nGoodbye, and thanks for using the .txi Project!")
            time.sleep(1)
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    run_all()