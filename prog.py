from amzqr import amzqr

version, level, qr_name = amzqr.run(
    # Сам текст
    words = "Hellow, Maximka!",
    # Размер QR-кода
    version = 4,
    level = 'H',
    # Фоновая картинка
    picture = "./test.gif",
    # Цветной QR-код
    colorized = True,
    # Контрастность
    contrast = 1.3,
    # Осветление
    brightness = 1.1,
    # Название выходного файла
    save_name = "./QR.gif",
)