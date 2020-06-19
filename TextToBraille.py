from PIL import Image, ImageDraw

class Character:
    def __init__(self, display_list, width=3, pixel_size=5):
        self._list = display_list
        self.pixel_size = pixel_size
        self.width = width
        self.height = -(-len(display_list) // self.width)
        display_list = [[0 for n in range(self.width)].copy() for i in range(self.height)]
        print(display_list)
        for pixel in range(len(self._list)):
            row = pixel // self.width
            column = pixel % self.width
            display_list[row][column] = int(self._list[pixel])
        self.pixels = display_list



class Paper:
    def __init__(self, name, width=100, height=100, color="white"):
        self.name = str(name)
        self._height = height
        self._width = width
        self._color = color
        self._clear()
    def _clear(self):
        self.image = Image.new("RGB", (self._width, self._height), self._color)
    def draw(self, x, y, dx, dy, color="black"):
        draw = ImageDraw.Draw(self.image)
        draw.rectangle([(x,y),(dx,dy)], color, outline=None)
    def save(self):
        self.image.save(self.name + ".png")
    def show(self):
        self.image.show()
    def drawChar(self, char, x, y, color="black"):
        pixels, width, height = char.pixels, char.width, char.height
        pixel_size = char.pixel_size
        dx, dy = 0, 0
        for row in range(char.height):
            for column in range(char.width):
                if pixels[row][column]:
                    self.draw(x + dx, y + dy, x + dx + pixel_size, y + dy + pixel_size, color)
                dx += pixel_size + 1
            dy += pixel_size + 1
            dx = 0



test_char_list = "101000101000101"
test_char = Character(test_char_list)
test_paper = Paper("Test2")
test_paper.drawChar(test_char, 10, 10)
test_paper.show()