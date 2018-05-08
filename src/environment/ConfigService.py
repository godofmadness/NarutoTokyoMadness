from ..environment.Environment import Environment

class ConfigService:

    def __init__(self, config):
        self.ENV_FLAG = "-e"
        self.config = config
        self.environment = Environment.DEBUG.value[0]
        self.inflateConfig()

    def inflateConfig(self):
        for paramIndex in range(len(self.config)):
            print(self.config[paramIndex])
            if self.config[paramIndex] == self.ENV_FLAG:
                self.environment = self.config[paramIndex + 1]

    def getEnvironment(self):
        return self.environment