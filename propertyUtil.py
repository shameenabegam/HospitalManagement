class PropertyUtil:

    @staticmethod
    def getDatabaseName(property_File):
        with open(property_File, 'r') as file:
            properties = {}
            for line in file:
                key, value = line.strip().split('=')
                properties[key.strip()] = value.strip()
        
        return properties['dbname']
