import os, csv
from PIL import Image, ImageFilter

def zad1():
    # создаем новую папку для обработанных изображений
    if not os.path.exists('processed_images'):
        os.makedirs('processed_images')

    # обходим все файлы в папке и обрабатываем каждое изображение
    for filename in os.listdir(r'processed_images'):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            with Image.open(os.path.join(r'processed_images', filename)) as img:
                # здесь можно проводить любую операцию с изображением
                # например, изменять размер и сохранять его в новой папке
                img = img.resize((500, 500))
                img.save(os.path.join('processed_images', filename))
                img.show()


zad1()


def zad2():
    # создаем новую папку для обработанных изображений
    if not os.path.exists('processed_images'):
        os.makedirs('processed_images')

    # обходим все файлы в папке и обрабатываем только изображения с расширениями .jpg и .png
    for filename in os.listdir(r'processed_images'):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            with Image.open(os.path.join(r'processed_images', filename)) as img:
                # здесь можно проводить любую операцию с изображением
                # например, изменять размер и сохранять его в новой папке
                img = img.filter(ImageFilter.SMOOTH_MORE)
                img.save(os.path.join('processed_images', filename))
                img.show()
zad2()


def zad3():
    total_cost = 0

    with open('products.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)

        print("Нужно купить:")
        for row in reader:
            product = row[0]
            quan = int(row[1])
            price = int(row[2])
            cost = quan * price
            total_cost += cost

            print(f"{product} - {quan} шт. за {price} руб.")

        print(f"Итоговая сумма: {total_cost} руб.")


zad3()