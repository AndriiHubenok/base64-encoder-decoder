ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def encode(data):
    """
    at a time (24 bits), split into four 6-bit groups, map each group
    through ALPHA, and pad the final group with '=' characters if the
    input length isn't a multiple of 3.
    """
    if isinstance(data, str):
        data = data.encode('utf-8')

    binary_chars = [bin(b)[2:].zfill(8) for b in data]
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

def decode(b64, is_bytes=False):
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
            byte_val = int(eight_bit_str, 2)

            if is_bytes:
                decoded_chars.append(format(byte_val, '02x'))
            else:
                decoded_chars.append(chr(byte_val))

            eight_bit_str = ''

    response = "".join(decoded_chars)

    return response

def encode_bytes(byte_text):
    """
    encode bytes directly from hex string
    """
    if not byte_text:
        return ""

    raw_bytes = bytes.fromhex(byte_text)

    return encode(raw_bytes)

def decode_str_to_hex(string):
    """
    decode string back to hex string
    """
    if not string:
        return ""

    return decode(string, is_bytes=True)

def get_value(char):
    """
    index (0-63)
    """
    return ALPHA.index(char)

def get_char(value):
    """
    print ALPHA[i]
    """
    return ALPHA[int(value)]

def count_padding(n):
    """
    count number of '=' characters at the end of the string
    """
    return (3 - int(n)) % 3