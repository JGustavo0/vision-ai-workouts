import logging
import os

def setup_logging():
    environment = os.getenv('ENVIRONMENT', 'production').lower()

    if environment == 'development':
        logging_level = logging.DEBUG
    elif environment == 'staging':
        logging_level = logging.INFO
    else:
        # Default to production level logging
        logging_level = logging.WARNING

    logging.basicConfig(level=logging_level)
