import os
import sys
import lzma

HEADER = b".txi\n"

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
        with open(txi_file, "rb") as rf:
            header = rf.readline()
            if header != HEADER:
                print("Error: invalid .txi header.")
                sys.exit(1)

            compressed_data = rf.read()
    except Exception as e:
        print(f"Error reading .txi: {e}")
        sys.exit(1)

    compressed_size = len(compressed_data)

    try:
        decompressed = lzma.decompress(compressed_data)
    except Exception as e:
        print(f"Error during decompression: {e}")
        sys.exit(1)

    decompressed_size = len(decompressed)

    out_txt = os.path.splitext(txi_file)[0] + "_decoded.txt"

    try:
        with open(out_txt, "wb") as wf:
            wf.write(decompressed)
    except Exception as e:
        print(f"Error writing decoded .txt: {e}")
        sys.exit(1)

    ratio = decompressed_size / compressed_size if compressed_size else 0

    print(f"→ Wrote '{out_txt}' (LZMA decompressed)")
    print(f"Compressed Size:   {compressed_size} bytes")
    print(f"Decoded Size:      {decompressed_size} bytes")
    print(f"Decompression Ratio: {ratio:.2f}")
