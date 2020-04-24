import json
import xml.etree.ElementTree as etree

class JSONParser:
    def __init__(self, filepath):
        with open(filepath, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)
        

    @property
    def parse_data(self):
        return self.data

class XMLParser:
    def __init__(self, filepath):
        self.root = etree.parse(filepath)

    @property
    def parse_data(self):
        return self.root

def parser_factory(filepath):
    parser = None
    if filepath.endswith('json'):
        parser = JSONParser
    elif filepath.endswith('xml'):
        parser = XMLParser
    else:
        raise ValueError('error: cannot connect to {}'.format(filepath))
    return parser(filepath)

def get_parser(filepath):
    factory = None
    try:
        factory = parser_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory

def main():
    xml_factory = get_parser("test.json")
    print()

    xml_factory = get_parser("test.xml")
    xml_data = xml_factory.parse_data
    
    liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))  
    print('found: {} persons'.format(len(liars)))    
    
    for liar in liars:        
        print('first name: {}'.format(liar.find('firstName').text))        
        print('last name: {}'.format(liar.find('lastName').text))        
        [p.text for p in liar.find('phoneNumbers')]    
        print()

    json_factory = get_parser('test.json')    
    json_data = json_factory.parse_data    
    print('found: {} donuts'.format(len(json_data)))    
    for donut in json_data:    
        print('name: {}'.format(donut['name']))    
        print('price: ${}'.format(donut['ppu']))    
        [print(t) for t in donut['topping']]


if __name__ == '__main__':
    main()
    