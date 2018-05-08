from .HUDStatusBar import HUDStatusBar

class HUDStatsBarFactory:

    @staticmethod
    def getInstanse(display, showOnLeftSide):
        return HUDStatusBar(display, showOnLeftSide)
