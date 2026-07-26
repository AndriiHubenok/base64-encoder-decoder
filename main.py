import sys
import custom_base64

for raw in sys.stdin:
    line = raw.rstrip("\n")
    if not line: print(""); continue
    parts = line.split(" ", 1)

    if len(parts) == 1:
        data = parts[0]

        try:
            bytes.fromhex(data)
            print(custom_base64.encode_bytes(data))

        except ValueError:
            print(custom_base64.decode_str_to_hex(data))
        continue

    cmd = parts[0]
    arg = parts[1] if len(parts) > 1 else ""
    if cmd == "ENCODE":
        print(custom_base64.encode(arg))

    elif cmd == "DECODE":
        try: print(custom_base64.decode(arg))
        except Exception: print("INVALID")

    elif cmd == "ENCODE_URL":
        print(custom_base64.encode_url(arg))

    elif cmd == "DECODE_URL":
        print(custom_base64.decode_url(arg))

    elif cmd == "VAL":
        try: print(custom_base64.get_value(arg))
        except Exception: print("INVALID")

    elif cmd == "CHAR":
        try: print(custom_base64.get_char(arg))
        except Exception: print("INVALID")

    elif cmd == "PAD_FOR":
        print(custom_base64.count_padding(arg))
