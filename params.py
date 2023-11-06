api_link = 'https://api.viz.berlin.de/daten/baustellen_sperrungen.json'
# csv or wdx3
output_format = 'csv'
default_city = 'Berlin'
default_direction = 'AB'
default_dexx = 'deXXX'
datetime_input_format = '%d.%m.%Y %H:%M'
datetime_output_format = '%d.%m.%Y - %H:%M'
csv_header = ('\"ID\"',
              '\"TYPE\"',
              '\"FROM\"',
              '\"TO\"',
              '\"CITY\"',
              '\"CITY_ABBR\"',
              '\"STREET\"',
              '\"HOUSE\"',
              '\"LAT\"',
              '\"LNG\"',
              '\"REASON\"',
              '\"HINT\"',
              '\"EXTERNAL_ID\"',
              '\"HEIGHT\"',
              '\"WIDTH\"',
              '\"LENGTH\"',
              '\"WEIGHT\"',
              '\"IMPORTANT\"',
              '\"NAME\"'
              )
csv_separator = ';'
