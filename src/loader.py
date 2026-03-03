import csv
import logging

logger = logging.getLogger(__name__)

def load_csv(file_path):
    records = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                records.append(row)
    except Exception as e:
        logger.error(f"Error loading file {file_path}: {e}")
    return records