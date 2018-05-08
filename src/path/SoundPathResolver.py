import os

class SoundPathResolver:

    def __init__(self):
        print("asbPaht "  + os.path.abspath("."))
        self.resourceAbsolutePath = os.path.abspath("res/sound")

    def resolve(self, filename):
        return self.resourceAbsolutePath + "/" + filename