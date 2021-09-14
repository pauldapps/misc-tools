# misc-tools
A repo for the small tools which come in handy day-to-day.

        ```
        >>> measurement = 'serverroom'
        >>> tags = {'category': 'general', 'priority': 'high', 'owningParty': 'maintenace'}
        >>> field = {'humidity': 0.99} #get_sensor_humidity
        
        >>> format_line_protocol(measurement,field,tags)

        >>> 'serverroom,category=general,priority=high,owningParty=maintenace humidity=0.99'
        ```