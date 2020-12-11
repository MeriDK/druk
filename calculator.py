clients = {
    'client1': 2,
    'client2': 2,
    'client3': 3,
    'client4': 3,
    'client5': 2
}

prices = {
    'eco': {
        'lam': {1: 200, 2: 150, 3: 100, 4: 80},
        'lita': {1: 250, 2: 200, 3: 150, 4: 120},
        'plivka': {1: 180, 2: 150, 3: 130, 4: 110}
    },
    'solvent': {
        'lam': {1: 150, 2: 100, 3: 50, 4: 30},
        'lita': {1: 200, 2: 150, 3: 100, 4: 70},
        'plivka': {1: 130, 2: 100, 3: 80, 4: 60}
    },
    'uv': {
        'lam': {1: 230, 2: 180, 3: 130, 4: 110},
        'lita': {1: 280, 2: 230, 3: 180, 4: 150},
        'plivka': {1: 210, 2: 180, 3: 160, 4: 140}
    }
}

adds = {
    'luv': {1: 2.5, 2: 2, 3: 1.5, 4: 1},
    'spider': 400,
    'lam': 50,
    'porizka': 70
}


def get_category(client):
    return clients.get(client, 1)


def get_price(printer, category):
    try:
        return prices[printer][category]
    except KeyError:
        return 0


def add_service(type):
    pass




def luv(w, h, width=0.3):
    res = int(w / width) + int(h / width)
    if w / width - int(w / width) > 0.5:
        res += 1
    if h / width - int(h / width) > 0.5:
        res += 1
    return res * 2


print(luv(5.9, 2.97, 0.4)*2)


def test():
    """
    1 литий банер 1.2 х 2.5 еко + люверси по 0.4 = 1.2 * 2.5 * 210 + 2.5 * 18 = 675 грн.
    2 ламінований банер сольвент 0.4 х 1.2 + люверси 4 шт = 0.4 * 1.2 * 78 + 2.5 * 4 = 47.44 грн.
    2 уф литий банер 3 х 12 + люверси 0.3 + паук = 3 * 12 * 138 + 2.5 * 100 + 400 = 5618 грн.
    3 наклейки еко + ламінація 1 х 1 = 1 * 1 * (129 + 50) = 179 грн.
    1 наклейка сольвент 0.4 х 0.1 = 0.4 * 0.1 * 150 = 6 грн.
    """
    print(calculate(1.2, 2.5, 'eco', 'litii', 2, [['luv', 0.4]]))
    print(calculate(0.4, 1.2, 'solvent', 'lam', 2, [['luv', 4]]))
    print(calculate())


def calculate(h, w, printer, material, category, additional):
    return 0















