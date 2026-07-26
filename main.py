import sys
import custom_base64

for raw in sys.stdin:
    line = raw.rstrip("\n")
    if not line: print(""); continue
    parts = line.split(" ", 1)

    cmd = parts[0]
    arg = parts[1] if len(parts) > 1 else ""

    if cmd == "ENCODE":
        print(custom_base64.encode_bytes(arg))

    elif cmd == "DECODE":
        print(custom_base64.decode_str_to_hex(arg))

    elif cmd == "ENCODE_URL":
        print(custom_base64.encode_url(arg))

    elif cmd == "DECODE_URL":
        print(custom_base64.decode_url(arg))

    elif cmd == "ROUNDTRIP":
        if custom_base64.decode_str_to_hex(custom_base64.encode_bytes(arg)) == arg:
            print("OK")
        else:
            print("FAIL")

    elif cmd == "VAL":
        try: print(custom_base64.get_value(arg))
        except Exception: print("INVALID")

    elif cmd == "CHAR":
        try: print(custom_base64.get_char(arg))
        except Exception: print("INVALID")

    elif cmd == "PAD_FOR":
        print(custom_base64.count_padding(arg))
