def format_line_protocol(measurement: str,field: dict,tags: dict={}) -> str:
    """Converts input into influxDB line protocol format.

    Args:
        measurement (str): This is the overarching "thing" you're monitoring.
        field (dict): This is the metric you're collecting for the "thing."
        tags (dict, optional): These are optional other attributes you want to attach to the measurement. Defaults to {}.

    Raises:
        Exception: Multiple fields/metrics specified. Please format each field/metric separately.

    Returns:
        str: Line protocol formated string ready to be pushed to InfluxDB.

    Examples:
        ```
        >>> measurement = 'serverroom'
        >>> tags = {'category': 'general', 'priority': 'high', 'owningParty': 'maintenace'}
        >>> field = {'humidity': 0.99} #get_sensor_humidity
        
        >>> format_line_protocol(measurement,field,tags)

        >>> 'serverroom,category=general,priority=high,owningParty=maintenace humidity=0.99'
        ```
    """
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
