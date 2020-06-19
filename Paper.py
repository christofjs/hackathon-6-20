# Paper class that has methods to modify and create and image
from PIL import Image, ImageDraw
import Config as Config


class Paper:
    def __init__(self, name, width=Config.PAPER_WIDTH, height=Config.PAPER_HEIGHT, color=Config.PAPER_COLOR):
        """Creates an image that is associated with the object"""

        self.name = str(name)  # Name to be used when saving the file
        self._height = height
        self._width = width
        self._color = color

        self._clear()  # Sets the image to a blank page

    def _clear(self):
        """Resets the image to its default color"""

        self.image = Image.new("RGB", (self._width, self._height), self._color)

    def draw(self, x, y, dx, dy, color):
        """Draws a colored rectangle onto the image using the coordinates of the top left and its size"""

        draw = ImageDraw.Draw(self.image)

        draw.rectangle([(x,y),(dx,dy)], color, outline=None)

    def save(self):
        """Saves the image to a physical file that is the name the object was created with"""

        self.image.save(self.name + ".png")

    def show(self):
        """Opens the image in whatever is your system default, doesn't require saving"""

        self.image.show()

    def drawChar(self, char, x, y, color=Config.FONT_COLOR):
        """Takes a Character object and draws it on the image at the given coordinates using parameters inside the
        Character"""

        pixels, width, height = char.pixels, char.width, char.height
        pixel_size = char.pixel_size
        dx, dy = 0, 0

        # Loops though the character's list that specifies where to draw
        for row in range(char.height):

            for column in range(char.width):

                if pixels[row][column]:  # If there is a 1 at the specified index in the char, draw a pixel(s)
                    self.draw(x + dx, y + dy, x + dx + pixel_size, y + dy + pixel_size, color)

                dx += pixel_size + 1  # Increase the horizontal offset

            dy += pixel_size + 1  # Increase the vertical offset
            dx = 0  # Reset the horizontal offset
