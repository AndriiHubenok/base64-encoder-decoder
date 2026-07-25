import sys
import custom_base64

for raw in sys.stdin:
    line = raw.rstrip("\n")
    if not line: continue
    parts = line.split(" ", 1)
    cmd = parts[0]
    arg = parts[1] if len(parts) > 1 else ""
    if cmd == "ENCODE":
        print(custom_base64.encode(arg))
    elif cmd == "DECODE":
        try: print(custom_base64.decode(arg))
        except Exception: print("INVALID")
    elif cmd == "VAL":
        try: print(custom_base64.get_value(arg))
        except Exception: print("INVALID")
    elif cmd == "CHAR":
        try: print(custom_base64.get_char(arg))
        except Exception: print("INVALID")
