import os
import sys

HEADER = ".txi"

def decode_txi_to_txt():
    base = input("\nEnter absolute path of .txi file (no extension): ").strip()
    txi_file = f"{base}.txi"

    if not os.path.isabs(txi_file):
        print("Error: please provide an absolute path.")
        sys.exit(1)
    if not os.path.exists(txi_file):
        print(f"Error: '{txi_file}' does not exist.")
        sys.exit(1)

    try:
        with open(txi_file, "r", encoding="utf-8") as rf:
            lines = rf.readlines()
    except Exception as e:
        print(f"Error reading .txi: {e}")
        sys.exit(1)

    if not lines or lines[0].strip() != HEADER:
        print("Error: invalid .txi header.")
        sys.exit(1)

    body = "".join(lines[1:])
    decoded_size = len(body.encode("utf-8"))

    out_txt = os.path.splitext(txi_file)[0] + "_decoded.txt"
    try:
        with open(out_txt, "w", encoding="utf-8") as wf:
            wf.write(body)
    except Exception as e:
        print(f"Error writing decoded .txt: {e}")
        sys.exit(1)

    print(f"→ Wrote '{out_txt}' (raw text)")
    print(f".txi Body Size:     {decoded_size} bytes")
    print(f"Decoded Size:       {decoded_size} bytes")
    print("Decompression Ratio: N/A (no compression)")
