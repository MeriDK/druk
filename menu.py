import pandas as pd
from PIL import Image
from os import listdir, path
import PIL

PIL.Image.MAX_IMAGE_PIXELS = 933120000


class Product:
    def __init__(self):

        self.name = ''
        self.path = '\\\\192.168.1.155\\!!! Druk !!!\\2020\\11.2020\\'
        self.material = pd.DataFrame([])
        self.df = pd.DataFrame([])

        self.size = (0, 0)
        self.area = 0
        self.price = 0
        self.luv = 0
        self.amount = 1

        self.prepare_data()
        if self.name[-1] in ('/', '\\'):
            self.calculate_folder()
        else:
            self.calculate()

        if self.luv:
            print(self.luv, 'люв')
        print('Загальна площа:', self.area)
        print('Загальна ціна:', self.price)

    def prepare_data(self):
        print('Input data')
        inp = input().split(maxsplit=2)

        # add date folder
        date = inp[1].split('/')
        self.path += date[0] + '.' + date[1] + '\\'

        # set name
        self.name = inp[2]

        # add printer to path and get df
        if self.name[:3] == '720' or self.name[:5] == 'R_720':
            self.path += '720\\'
            self.df = pd.read_csv('eco.csv')
            print('Екосольвент')
        elif self.name[:3] == '360' or self.name[:5] == 'R_360':
            self.path += '360\\'
            self.df = pd.read_csv('sol.csv')
            print('Сольвент')
        elif self.name[:2] == 'UV' or self.name[:4] == 'R_UV':
            self.path += 'UV\\'
            self.df = pd.read_csv('uv.csv')
            print('УФ')
        else:
            print('Incorrect file name. Can\'t get printer')
            exit()

        # get material
        self.material = self.get_material()
        print(self.material['Матеріал'].values[0])

        # get manager
        managers = listdir(self.path)
        if inp[0] == 'Володя':
            for el in managers:
                if el[:2] == 'Vo' or el[:4] == 'R_Vo':
                    self.path += el + '\\'
        elif inp[0] == 'Любомир':
            for el in managers:
                if el[0] == 'L' or el[:3] == 'R_L':
                    self.path += el + '\\'
        elif inp[0] == 'Віра':
            for el in managers:
                if el[:2] == 'Vi' or el[:4] == 'R_Vi':
                    self.path += el + '\\'
        else:
            print('Incorrect input. Can\'t find manager')
            exit()

    def get_material(self):
        name = self.name.lower()
        if 'lyt' in name or ('lit' in name and 'beklit' not in name) or 'banLYT' in name or 'лит' in name:
            return self.df[self.df['Матеріал'] == 'Банерна тканина «Frontlit» лита']
        elif 'banLAM' in name or ('lam' in name and 'gl' not in name and 'mat' not in name and 'proz' not in name):
            return self.df[self.df['Матеріал'] == 'Банерна тканина «Frontlit» ламінована']
        elif 'sitka' in name or 'citka' in name:
            return self.df[self.df['Матеріал'] == 'Сітка банерна']
        elif ('gl' in name or 'mat' in name or 'proz' in name) and 'holst' not in name or 'гл' in name:
            return self.df[self.df['Матеріал'] == 'Самоклеюча плівка Ritrama']
        elif 'holst' in name:
            return self.df[self.df['Матеріал'] == 'Холст']
        elif 'solex' in name:
            return self.df[self.df['Матеріал'] == 'Самоклеюча плівка Китайська']
        elif 'siti' in name or 'сітік' in name or 'citi' in self.name:
            return self.df[self.df['Матеріал'] == 'Папір для друку постерний']
        elif 'vision' in name:
            return self.df[self.df['Матеріал'] == 'Самоклеюча плівка «One Way Vision»']
        elif 'blu' in name:
            return self.df[self.df['Матеріал'] == 'Папір Blueback']
        else:
            print('Unknown material')
            exit()

    def get_size(self):
        img = Image.open(self.path + self.name)
        dpi = img.info['dpi'][0]
        w, h = img.size
        w, h = w * 0.01 * 2.54 / dpi, h * 0.01 * 2.54 / dpi  # 1 inch = 2.54 cm
        w, h = round(w, 2), round(h, 2)
        return w, h

    def get_luv(self, width):
        res = int(self.size[0] / width) + int(self.size[1] / width)
        if self.size[0] / width - int(self.size[1] / width) > 0.5:
            res += 1
        if self.size[0] / width - int(self.size[1] / width) > 0.5:
            res += 1
        return res * 2

    def calculate(self):
        # get amount
        if 'sht' in self.name or 'шт' in self.name.lower():
            print('Введіть кількість для', self.name)
            self.amount = int(input())

        # get size
        if self.name [-4:] not in ('.cdr', '.tif', '.jpg', '.pdf', 'tiff', '.png', '.psb'):
            self.name += '.tif'
        try:
            self.size = self.get_size()
        except FileNotFoundError:
            try:
                self.name = 'R_' + self.name
                self.size = self.get_size()
            except (FileNotFoundError, PIL.UnidentifiedImageError):
                print(self.path + self.name)
                print('Can\'t open file. Enter size')
                w, h = input().split()
                self.size = round(float(w), 2), round(float(h), 2)

        area = self.size[0] * self.size[1] * self.amount
        print(self.size[0], 'x', self.size[1], '\nПлоща:', area)
        self.area += area

        # calculate price
        price = self.material.iloc[0][3]
        self.price += area * price

        # add luv
        luv = 0
        if 'luv30' in self.path + self.name or 'люв30' in self.path + self.name:
            luv = self.get_luv(0.3)
            print('Люверси кожні 30 см')
        elif 'luv40' in self.path + self.name or 'люв40' in self.path + self.name:
            luv = self.get_luv(0.4)
            print('Люверси кожні 40 см')
        elif 'luv' in self.path + self.name or 'люв' in self.path + self.name:
            print('Добавити люверси кожні ? м або ? люверсів')
            width = float(input())
            if width > 1 or width == 0:
                luv = int(width)
            else:
                luv = self.get_luv(width)
        if luv:
            self.luv += luv * self.amount
            self.price += luv * 2.5 * self.amount

        # add lam
        if self.material['Матеріал'].values[0] in ('Самоклеюча плівка Ritrama', 'Самоклеюча плівка Китайська',
                                                   'Самоклеюча плівка «One Way Vision»'):
            if 'lam' in self.path + self.name:
                print('Додано ламінацію')
                self.price += 50 * area

        # add porizka
        if 'porizka' in self.name.lower() or 'plot' in self.name.lower():
            print('Введіть вартість порізки')
            self.price += int(input())

    def calculate_folder(self):
        if path.exists(self.path + self.name):
            self.path = self.path + self.name
        else:
            self.path = self.path + 'R_' + self.name

        for el in listdir(self.path):
            self.name = el
            self.calculate()

# print('Виберіть матеріал')
# print(df['Матеріал'].to_string())
# mat = int(input())
# return mat


if __name__ == '__main__':
    product = Product()

#     print('Додаткові послуги?\n+\n-')
#     if input() == '+':
#         # додати скотч
#         print('Добавити скотч?\n+\n-')
#         if input() == '+':
#             total += 2 * (w + h) * 20
#             print(2 * (w + h) * 20)
#
#         # додати макет
#         print('Добавити макет?\n+\n-')
#         if input() == '+':
#             print('Введіть суму')
#             total += int(input())



