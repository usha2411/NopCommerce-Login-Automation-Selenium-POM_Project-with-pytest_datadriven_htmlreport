import logging

class Log_Maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename="D:/Pycharm/nopcommerce_automation/logs/nopcommerce",format='%(asctime)s:%(levelname)s:%(message)s',force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger