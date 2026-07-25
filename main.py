import sys

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def encode(text):
    # TODO: implement base64 encoding manually: take the bytes of `text` 3
    # at a time (24 bits), split into four 6-bit groups, map each group
    # through ALPHA, and pad the final group with '=' characters if the
    # input length isn't a multiple of 3.
    return ""

def decode(b64):
    # TODO: implement base64 decoding manually: for every 4 characters,
    # look up each character's 6-bit value in ALPHA (ignoring '=' padding),
    # recombine into bytes, and decode the result back to text.
    return ""

for raw in sys.stdin:
    line = raw.rstrip("\n")
    if not line: continue
    parts = line.split(" ", 1)
    cmd = parts[0]
    arg = parts[1] if len(parts) > 1 else ""
    if cmd == "ENCODE":
        print(encode(arg))
    elif cmd == "DECODE":
        try: print(decode(arg))
        except Exception: print("INVALID")
