"""
measurement = 'serverroom'
tags = {'category': 'general', 'priority': 'high', 'owningParty': 'maintenace'}
field = {'humidity': 0.99} #get_sensor_humidity
format_line_protocol(measurement,field,tags)
'serverroom,category=general,priority=high,owningParty=maintenace humidity=0.99'
"""
def format_line_protocol(measurement: str,field: dict,tags: dict={}) -> str:
    str_output = f'{measurement}'
    if tags:
        for t in tags:
            str_output += f',{t}={tags[t]}'
    if len(field) == 1:
        f = list(field.keys())[0]
        str_output += f" {f}={field[f]}"
        return str_output
    else:
        raise Exception("Multiple fields/metrics specified. Please format each field/metric separately.") 
