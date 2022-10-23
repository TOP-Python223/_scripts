
class RasterImage:
    @staticmethod
    def draw():
        """Полиморфный метод."""
        print('растровое изображение')


class VectorImage:
    @staticmethod
    def render():
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
    if img.__class__ is RasterImage:
        img.draw()
    elif img.__class__ is VectorImage:
        img.render()

