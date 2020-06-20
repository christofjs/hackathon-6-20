# Paper class that has methods to modify and create and image
from PIL import Image, ImageDraw, ImageOps
import Config as Config
import Dictionary as Dictionary
from Character import Character

class Paper:
    def __init__(self, name, width=Config.PAPER_WIDTH, height=Config.PAPER_HEIGHT, color=Config.PAPER_COLOR):
        """Creates an image that is associated with the object"""

        self.name = str(name)  # Name to be used when saving the file
        self._height = height
        self._width = width
        self._color = color

        self.charset = Dictionary.DICTIONARY  # Converts the dictionary from Dictionary into one with objects
        for x in self.charset:
            self.charset[x] = Character(self.charset[x])

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

    def drawSentence(self, string, x=Config.MARGIN, y=Config.MARGIN,
                     wrap_width=(Config.PAPER_WIDTH - (Config.MARGIN * 2)),
                     x_spacing=Config.X_SPACING,
                     y_spacing=Config.Y_SPACING,
                     color=Config.FONT_COLOR):
        """Draws a sentence starting at a point, wraps after passing a specified width
        (relative to the left edge of paper)"""

        # First convert the string into braille letters
        braille_code = []
        for letter in string:
            if letter.isupper():
                braille_code.append(self.charset["CAPITAL"])
                braille_code.append(self.charset[letter.lower()])
            elif letter.isnumeric():
                braille_code.append(self.charset["NUMERIC"])
                braille_code.append(self.charset[letter])
            else:
                braille_code.append(self.charset[letter])

        dx, dy = 0, 0
        character_width = Config.FONT_SIZE * 3 + x_spacing * 2
        character_height = Config.FONT_SIZE * 5 + y_spacing

        # Displaying the letters
        for character in braille_code:

            self.drawChar(character, x + dx, y + dy, color)

            if dx + character_width >= wrap_width:  # If it has hit the right margin, wrap
                dx = 0
                dy += character_height
            else:
                dx += character_width # Move to next char

            if dy + character_height >= Config.PAPER_HEIGHT - Config.MARGIN * 2:  # If it hits the end of the page
                print("Out of space on page.")
                return

    def mirror(self):  # Flips it so that you can poke it out
        self.image = ImageOps.mirror(self.image)