# Character class that has array to represent pixels to display
import Config as Config


class Character:
    def __init__(self, braille_code, pixel_size=Config.FONT_SIZE):

        braille_code = str(braille_code)  # Turn into a list
        self._list = "000000000000000"  # List that represents which pixels to fill, is a 3 * 5 rectangle

        self.pixel_size = pixel_size
        self.width = 3
        self.height = 5

        self.pixels = [[0 for n in range(3)].copy() for i in range(5)]  # List to be used by Paper to display a char

        # Update display_list to match the braille code, see http://braillebug.org/braille_deciphering.asp#:~:text=Capitalizing%20in%20Braille,the%20whole%20word%20is%20capitalized.
        self.pixels[0][0] = int(braille_code[0])
        self.pixels[2][0] = int(braille_code[1])
        self.pixels[4][0] = int(braille_code[2])
        self.pixels[0][2] = int(braille_code[3])
        self.pixels[2][2] = int(braille_code[4])
        self.pixels[4][2] = int(braille_code[5])
