import os


class ImagePathResolver:

    def __init__(self):
        print("asbPaht "  + os.path.abspath("."))
        self.resourceAbsolutePath = os.path.abspath("res/images")

    def resolve(self, filename):
        return self.resourceAbsolutePath + "/" + filename