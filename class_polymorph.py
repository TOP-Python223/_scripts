
class RasterImage:
    @staticmethod
    def draw():
        """Полиморфный метод."""
        print('растровое изображение')


class VectorImage:
    @staticmethod
    def draw():
        """Полиморфный метод."""
        print('векторное изображение')


images = [
    RasterImage(),
    RasterImage(),
    VectorImage(),
    RasterImage(),
    VectorImage(),
]
for img in images:
    img.draw()
