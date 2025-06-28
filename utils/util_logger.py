import logging
logger = logging.getLogger(__name__)

logging.basicConfig(filename='logs.log', level=logging.INFO)

if __name__ == "__main__":
    logger.info("Start")


def log(text):
    logger.info(text)
