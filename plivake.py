def calc(h, w, poriz=0, lam=0):
    price = 109     # 95 for solvent
    return (price + 50 * lam) * h * w + poriz


print(calc(0.24, 0.3, 0, 0) * 15 + 50)
