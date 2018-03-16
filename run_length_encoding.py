def run_length_encoding(in_str):
    out_str = []
    count = 1
    start_char = in_str[0]
    for char in in_str[1:]:
        if char == start_char:
            count += 1
        else:
            out_str.extend([start_char, count])
            start_char = char
            count = 1
    out_str.extend([start_char, count])
    return out_str