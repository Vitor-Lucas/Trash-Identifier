from quickdraw import QuickDrawData

'''
This script is useless considering the final product, but we decided to keep this here because
it was really fun to program it

'''


def get_image(categoria:str):
    # Gets an image
    qd = QuickDrawData()
    drawing = qd.get_drawing(f"{categoria}")

    # Converts the image from 255x255 to 28x28
    image = drawing.image
    image.thumbnail((28, 28))
    return image


def recolor(image):
    pix = image.load()
    width, height = image.size
    for line in range(height):
        for col in range(width):
            cor_pixel = pix[line, col]
            white = (255, 255, 255)
            if cor_pixel != white:
                pix[line, col] = (0, 0, 0)
    return image


def process_image(image):
    # Transforms an image in a binary list
    # 0 being black
    # 1 being white
    pix = image.load()
    width, height = image.size
    img_01 = []
    for line in range(height):
        for col in range(width):
            cor_pixel = pix[line, col]
            white = (255, 255, 255)

            if cor_pixel != white:
                img_01.append(1)
                continue
            img_01.append(0)

    return img_01


categories = ['airplane', 'windmill', 'alarm clock', 'axe', 'house', 'ice cream', 'key', 'moon', 'sun', 'watermelon']

# gets ten thousand images for each cartegory and transforms them into binary lists
for category in categories:
    with open(f'{category}.txt', 'w') as file:
        for _ in range(10_000):
            binary_list = process_image(get_image(category))
            file.write(f'{binary_list}\n')