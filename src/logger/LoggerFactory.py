import logging

class LoggerFactory:


    @staticmethod
    def getStreamLogger(forName):
        logger = logging.getLogger(forName)
        logger.setLevel(logging.DEBUG)
        # create stdout logger handler
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger