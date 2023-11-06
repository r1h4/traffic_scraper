import params
from model import obstruction
from utils import get_obstructions
import csv


if __name__ == '__main__':
    raw_obstructions = get_obstructions.from_api_as_json()

    with open('data/traffic.csv', 'w', encoding='iso-8859-1') as outfile:
        csv_writer = csv.writer(outfile, delimiter=params.csv_separator, quotechar="'")
        if params.output_format == 'csv':
            csv_writer.writerow(params.csv_header)

        for entry in raw_obstructions['features']:
            temp_obstr = obstruction.Obstruction()
            temp_obstr.from_json(entry)
            if params.output_format == 'csv':
                csv_writer.writerow(temp_obstr.to_csv_row())
            elif params.output_format == 'wdx3':
                csv_writer.writerow(temp_obstr.to_csv_row_wdx3())
            else:
                print('No valid output-format given.')
