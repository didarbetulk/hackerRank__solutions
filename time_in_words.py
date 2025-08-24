def num_to_words(n):
    base = ["", "one","two","three","four","five","six","seven","eight","nine",
            "ten","eleven","twelve","thirteen","fourteen","fifteen",
            "sixteen","seventeen","eighteen","nineteen"]
    if 1 <= n < 20:
        return base[n]
    if 20 <= n < 30:
        return "twenty" + ("" if n == 20 else " " + base[n - 20])
    if n == 30:
        return "half"
    raise ValueError("n out of supported range")

def timeInWords(h, m):
    if m == 0:
        return f"{num_to_words(h)} o' clock"

    past = True
    mm = m
    if m > 30:
        past = False
        mm = 60 - m
        h = 1 if h == 12 else h + 1

    if mm == 15:
        phrase = "quarter"
    elif mm == 30:
        phrase = "half"
    else:
        unit = "minute" if mm == 1 else "minutes"
        phrase = f"{num_to_words(mm)} {unit}"

    return f"{phrase} {'past' if past else 'to'} {num_to_words(h)}"


# main kismi: input oku ve sonucu yazdir
if __name__ == "__main__":
    h = int(input().strip())
    m = int(input().strip())
    print(timeInWords(h, m))
#daha optimum bir cozum olabilri.[FARKLİ ZAMANDA TEKRAR COZ]
