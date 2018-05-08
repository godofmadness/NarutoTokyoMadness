from ..path.SoundPathResolver import SoundPathResolver
import threading

class SoundEffectService:

    def __init__(self, player):
        self.pathResolver = SoundPathResolver()
        self.player = player


    def play(self, soundName):
        self.player.music.load(self.pathResolver.resolve(soundName))
        thread = threading.Thread(target=self.player.music.play, args=(1,))
        thread.start()



