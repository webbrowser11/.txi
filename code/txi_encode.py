import os
import sys
import lzma

HEADER = b".txi\n"  # bytes now

def encode_txt_to_txi():
    txt_base = input("\nEnter absolute path of .txt file (no extension): ").strip()
    txt_file = f"{txt_base}.txt"

    if not os.path.isabs(txt_file):
        print("Error: please provide an absolute path.")
        sys.exit(1)
    if not os.path.exists(txt_file):
        print(f"Error: '{txt_file}' does not exist.")
        sys.exit(1)

    # Read as bytes
    with open(txt_file, "rb") as rf:
        data = rf.read()

    original_size = len(data)

    # Compress using LZMA
    compressed = lzma.compress(data)
    compressed_size = len(compressed)

    out_file = os.path.splitext(txt_file)[0] + ".txi"

    try:
        with open(out_file, "wb") as wf:
            wf.write(HEADER)
            wf.write(compressed)
    except Exception as e:
        print(f"Error writing .txi: {e}")
        sys.exit(1)

    ratio = compressed_size / original_size if original_size else 0

    print(f"→ Wrote '{out_file}' (LZMA compressed)")
    print(f"Original Size:   {original_size} bytes")
    print(f"Compressed Size: {compressed_size} bytes")
    print(f"Compression Ratio: {ratio:.2f}")
