def format_number(string):
    j = len(string) % 3
    substrings = [string[3 * i + j:3 * (i + 1) + j] for i in                                         range(len(string)//3)]
    if j != 0:
        substrings.insert(0, string[:j])
    return ".".join(substrings)