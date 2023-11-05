from model import obstruction
from utils import get_obstructions
import csv


if __name__ == '__main__':
    raw_obstructions = get_obstructions.from_api_as_json()

    with open('data/traffic.csv', 'w') as outfile:
        csv_writer = csv.writer(outfile)

        for entry in raw_obstructions['features']:
            temp_obstr = obstruction.Obstruction()
            temp_obstr.from_json(entry)
            csv_writer.writerow(temp_obstr.to_csv_row())
