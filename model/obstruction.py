from datetime import datetime, timedelta
import params


class Obstruction:
    def __init__(self,
                 id=None,
                 val_from=None,
                 val_until=None,
                 city=None,
                 district=None,
                 street=None,
                 number=None,
                 lat=None,
                 lon=None,
                 fe_type=None,
                 reason=None,
                 description=None,
                 direction=None,
                 dexx=None):
        if id is None:
            self.id = datetime.now()
        else:
            self.id = id
        if val_from is None:
            self.val_from = datetime.now()
        else:
            self.val_from = datetime.strptime(val_from, params.datetime_input_format)

        if val_until is None:
            self.val_until = self.val_from + timedelta(1)
        else:
            self.val_until = datetime.strptime(val_until, params.datetime_input_format)

        if city is None:
            self.city = params.default_city
        else:
            self.city = city

        if district is None:
            self.district = ''
        else:
            self.district = district

        if street is None:
            self.street = ''
        else:
            self.street = street

        if number is None:
            self.number = ''
        else:
            self.number = str(number)

        if lat is None:
            self.lat = 0.0
        else:
            self.lat = lat

        if lon is None:
            self.lon = 0.0
        else:
            self.lon = lon

        if fe_type is None:
            self.fe_type = ''
        else:
            self.fe_type = fe_type

        if reason is None:
            self.reason = ''
        else:
            self.reason = reason

        if description is None:
            self.description = ''
        else:
            self.description = description

        if direction is None:
            self.direction = params.default_direction
        else:
            self.direction = direction

        if dexx is None:
            self.dexx = params.default_dexx
        else:
            self.dexx = dexx

    def from_json(self, json_data):
        if 'id' not in json_data['properties']:
            pass
        elif json_data['properties']['id'] is None:
            pass
        else:
            self.id = json_data['properties']['id']

        if 'from' not in json_data['properties']['validity']:
            self.val_from = datetime.now()
        elif json_data['properties']['validity']['from'] is None:
            self.val_from = datetime.now()
        else:
            self.val_from = datetime.strptime(json_data['properties']['validity']['from'], params.datetime_input_format)

        if 'to' not in json_data['properties']['validity']:
            self.val_until = self.val_from + timedelta(1)
        elif json_data['properties']['validity']['to'] is None:
            self.val_until = self.val_until + timedelta(1)
        else:
            self.val_until = datetime.strptime(json_data['properties']['validity']['to'], params.datetime_input_format)

        if 'street' in json_data['properties']:
            self.street = json_data['properties']['street']
        if 'geometries' in json_data['geometry']:
            self.lat = json_data['geometry']['geometries'][0]['coordinates'][1]
            self.lon = json_data['geometry']['geometries'][0]['coordinates'][0]
        else:
            self.lat = json_data['geometry']['coordinates'][1]
            self.lon = json_data['geometry']['coordinates'][0]

        if 'severity' not in json_data['properties']:
            pass
        elif json_data['properties']['severity'] is None:
            pass
        else:
            self.reason = json_data['properties']['severity']

        if 'subtype' not in json_data['properties']:
            pass
        elif json_data['properties']['subtype'] is None:
            pass
        elif json_data['properties']['subtype'] in ('Baustelle', 'Bauarbeiten', 'Fahrstreifensperrung'):
            self.fe_type = 'ROAD_WORKS'
        elif json_data['properties']['subtype'] == 'Sperrung':
            self.fe_type = 'ROAD_CLOSED'
        else:
            self.fe_type = 'INCIDENT'

        if 'content' not in json_data['properties']:
            pass
        elif json_data['properties']['content'] is None:
            pass
        else:
            self.description = json_data['properties']['content']

        if 'direction' not in json_data['properties']:
            pass
        elif json_data['properties']['direction'] == 'Beidseitig':
            self.direction = 'BD'
        else:
            self.direction = 'AB'

        # split street-info into number and district (if given)
        if '(' and ')' in self.street:
            self.district = self.street[self.street.find('(') + 1:self.street.find(')')]
            self.street = self.street[:self.street.find('(')]

    def to_csv_row_wdx3(self):
        csv_row = (
            self.val_from.strftime(params.datetime_output_format),
            self.val_until.strftime(params.datetime_output_format),
            self.city,
            self.district,
            self.street,
            self.number,
            self.lat,
            self.lon,
            self.fe_type,
            self.description,
            self.direction,
            self.dexx
        )
        return csv_row

    def to_csv_row(self):
        if self.fe_type == 'ROAD_CLOSED':
            important = True
        else:
            important = False

        fe_name = self.street
        if self.reason is None or self.reason == '':
            pass
        else:
            fe_name += ' - ' + self.reason

        csv_row = (
            self.id,
            self.fe_type,
            self.val_from.strftime(params.datetime_output_format),
            self.val_until.strftime(params.datetime_output_format),
            self.city,
            self.district,
            self.street,
            self.number,
            self.lat,
            self.lon,
            self.reason,
            self.description,
            self.id,
            '0.0',
            '0.0',
            '0.0',
            '0.0',
            important,
            self.street + ' - ' + self.reason
        )
        return csv_row
