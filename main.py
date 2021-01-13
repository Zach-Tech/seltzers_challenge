# accum("abcd") -> A-Bb-Ccc-Dddd"

def cum(s):
    result = ''
    x = 0
    while x < len(s):
        n = 0
        while n < x + 1:
            if n == 0:
                result += s[x].upper()
            else:
                result += s[x].lower()
            n += 1
        result += '-'
        x += 1
    return result[:len(result) - 1]


print(cum("abcd"))
