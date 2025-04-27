import os
import sys

HEADER = ".txi"

def encode_txt_to_txi():
    txt_base = input("\nEnter absolute path of .txt file (no extension): ").strip()
    txt_file = f"{txt_base}.txt"

    if not os.path.isabs(txt_file):
        print("Error: please provide an absolute path.")
        sys.exit(1)
    if not os.path.exists(txt_file):
        print(f"Error: '{txt_file}' does not exist.")
        sys.exit(1)

    with open(txt_file, "r", encoding="utf-8") as rf:
        text = rf.read()
    original_size = len(text.encode("utf-8"))

    out_file = os.path.splitext(txt_file)[0] + ".txi"
    try:
        with open(out_file, "w", encoding="utf-8") as wf:
            wf.write(HEADER + "\n")
            wf.write(text)
    except Exception as e:
        print(f"Error writing .txi: {e}")
        sys.exit(1)

    print(f"→ Wrote '{out_file}' (raw text)")
    print(f"Original Size:   {original_size} bytes")
    print(f"Final Size:      {original_size} bytes")
    print("Compression Ratio: N/A (no compression)")
