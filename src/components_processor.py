from typing import Iterable, List, Union
from data_aggregator import Histogram

DRIVER_NAMES  = [
    "C# Driver",
    "C++ Driver",
    "C Driver",
    "Go Driver",
    "Java Driver",
    "Node.js Driver",
    "PHP Driver",
    "Python Driver",
    "Ruby Driver",
    "Rust Driver",
    "Scala Driver",
    "Swift Driver",
]

LANG_ODM_NAMES = [
    "Go",
    "Java",
    "JavaScript",
    "Mongoose",
    "Node.js",
    "PHP",
    "Python",
    "Ruby",
    "Spring Data",
    "Swift",
    ".NET"
]

class ComponentsProcessor:
    __histogram:Histogram = None

    def __init__(self, histogram:Histogram) -> None:
        self.__histogram = histogram

    def process(self, components: str) -> None:
        '''
        Process given components string. If the component is an empty string, the function is returned.
        Split the components string by ';' and checks whether it contains a Driver or a Driver Language
        '''
        if components == "":
            return

        components_list = components.split(";")
        driver_name, other_components = self._get_driver_name(components_list)
        
        # Check if driver or language names found in the components_list 
        if driver_name == "":
            return

        data_value = self.__histogram.add_value(driver_name)
        
        if len(other_components) != 0:

            if data_value.child_histogram == None:
                data_value.child_histogram = Histogram()
            
            # Treat other child components of this driver_name
            for child_component in other_components:
                data_value.child_histogram.add_value(child_component)

    def _get_driver_name(self, components: List[str]) -> Iterable[Union[str, List[str]]]:
        '''
        Receives components_list and checks whether it contains a component which is in the list of DRIVER_NAMES or is in the list of LANG_ODM_NAMES.
        If found, returns that component name and the components_list without the found component.
        '''
        ret_driver_name = ""
        ret_lang_odm_name = ""
        ret_components = []

        for component in components:

            component = component.strip()

            # Check if component is a driver name which was not found before
            if (component in DRIVER_NAMES) and (ret_driver_name == ""):
                ret_driver_name = component

            # Check if component is a language or an ODM which was not found before
            # This check is made only until the ret_driver_name  is empty, which means not found.
            elif ret_driver_name == "" and (component in LANG_ODM_NAMES) and (ret_lang_odm_name == ""):
                ret_lang_odm_name = component
            else:
                ret_components.append(component)

        if ret_driver_name != "":
            return ret_driver_name, ret_components

        if ret_lang_odm_name != "":
            return ret_lang_odm_name, ret_components
        
        # If not found return empty component
        return "", ret_components