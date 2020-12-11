from PIL import Image

path = '\\\\192.168.1.155\\!!! Druk !!!\\2020\\11.2020\\20.11\\UV\\Lubomur\\'
name = 'R_UV_mat_10sht_УФ друк біл мат (Близенько заб алк)  10шт_Ariya.tif'
img = Image.open(path + name)
dpi = img.info['dpi'][0]
w, h = img.size
print(round(10 * w * h * (0.01 * 2.54 / dpi) ** 2, 2))    # 1 inch = 2.54 cm
