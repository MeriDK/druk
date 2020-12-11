def luv(w, h, width=0.3):
    if width == 0:
        return 0
    res = int(w / width) + int(h / width)
    if w / width - int(w / width) > 0.5:
        res += 1
    if h / width - int(h / width) > 0.5:
        res += 1
    return res * 2


def lam(h, w, l=0.3):
    global price
    res = price * h * w
    if l < 1:
        res += luv(w, h, l) * 2.5
        l = luv(w, h, l)
    else:
        res += l * 2.5
    return res, l


def calc(elements):
    res = 0
    s = 0
    l = 0
    for el in elements:
        if len(el) == 2:
            t = lam(el[0], el[1])
        else:
            t = lam(el[0], el[1], el[2])
        res += t[0]
        l += t[1]
        s += el[0] * el[1]
    return res, s, l


lit360 = 89
lam360 = 68
lit720 = 102
lam720 = 89
lituv = 121
lamuv = 106

price = lit720
print(calc([[1, 0.5, 0.4]]))

# volodia 03/11/20 Vactor-A 575

