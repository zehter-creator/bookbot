def string_accept(path):
    a = str.split(path)
    return len(a)

def string_to_count(string):
    f = str.lower(string)
    mer= {}
   
    for char in f:
        if char not in mer:
            mer[char] = f.count(char)
    return mer

def sort_on(item):
    return item["num"]

def sort_char(metin):
    chars = []
    for char, count in metin.items():
        chars.append({
        "char": char,
        "num": count
        })
    chars.sort(reverse=True, key=sort_on)
    return chars