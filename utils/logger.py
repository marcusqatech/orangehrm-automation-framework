import logging
import os

# Create the 'logs' directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/test_logs.log"),
        logging.StreamHandler()  # Print logs to the console as well
    ]
)

# Get the logger
logger = logging.getLogger()

def getLogger():
    return logger
