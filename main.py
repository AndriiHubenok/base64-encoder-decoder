import sys

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def encode(text):
    """
    at a time (24 bits), split into four 6-bit groups, map each group
    through ALPHA, and pad the final group with '=' characters if the
    input length isn't a multiple of 3.
    """
    chars = list(text)
    ascii_chars = [ord(c) for c in chars]
    binary_chars = [bin(c)[2:].zfill(8) for c in ascii_chars]
    binary_string = ''.join(binary_chars)

    six_bit_list = list()
    six_bit_str = ''
    for bit in binary_string:
        six_bit_str += bit
        if len(six_bit_str) == 6:
            six_bit_list.append(int(six_bit_str, 2))
            six_bit_str = ''

    if len(six_bit_str) > 0:
        six_bit_list.append(int(six_bit_str.ljust(6, '0'), 2))

    response = ''.join(ALPHA[c] for c in six_bit_list)

    pad_count = (4 - (len(response) % 4)) % 4
    response += '=' * pad_count

    return response

def decode(b64):
    """
    look up each character's 6-bit value in ALPHA (ignoring '=' padding),
    recombine into bytes, and decode the result back to text.
    """
    encoded_chars = list(b64)
    binary_chars = list()
    for c in encoded_chars:
        if c == '=':
            continue
        index = ALPHA.index(c)
        binary_chars.append(bin(index)[2:].zfill(6))

    binary_string = ''.join(binary_chars)

    decoded_chars = list()
    eight_bit_str = ''
    for bit in binary_string:
        eight_bit_str += bit
        if len(eight_bit_str) == 8:
            decoded_chars.append(chr(int(eight_bit_str, 2)))
            eight_bit_str = ''

    response = "".join(decoded_chars)

    return response

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
