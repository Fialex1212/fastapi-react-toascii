class ASCIIConverter:
    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    
    @staticmethod
    def resize_image(image, new_width=200):
        width, height = image.size
        ratio = height / width
        new_height = int(new_width*ratio*0.45)
        resized_image = image.resize((new_width, new_height))
        return(resized_image)

    @staticmethod
    def grayify(image):
        grayscale_image = image.convert("L")
        return(grayscale_image)

    @staticmethod
    def pixels_to_ascii(image):
        pixels = image.getdata()
        characters = "".join([ASCIIConverter.ASCII_CHARS[pixel * len(ASCIIConverter.ASCII_CHARS) // 256] for pixel in pixels])
        return characters