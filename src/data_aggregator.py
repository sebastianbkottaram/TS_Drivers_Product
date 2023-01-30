from typing import Dict

class DataValue:
    '''
    For type definition
    '''
    pass

class Histogram:
    '''
    Probably we should consider usage of https://realpython.com/python-histograms/
    at some point
    '''

    # key: String
    # value: DataValue
    __data: Dict[str, DataValue] = {}

    def __init__(self) -> None:
        self.__data = {}

    def add_value(self, key:str) -> DataValue:
        '''
        Add value to the Histogram, updating the internal counter
        '''
        data_value = self.__data.get(key)
        if data_value is None:
            data_value = DataValue(key)
        
        data_value.count += 1
        self.__data[key] = data_value

        return data_value
    
    def get(self, key: str) -> DataValue:
        return self.__data.get(key)
    
    def get_data(self) -> Dict[str, DataValue]:
        return self.__data

class DataValue:
    name: str = ""
    count: int = 0
    child_histogram: Histogram = None

    def __init__(self, name, count=0, child_historgram: Histogram=None) -> None:
        self.name=name
        self.count=count
        self.child_histogram=child_historgram
