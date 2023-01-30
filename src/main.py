import csv
import os
from components_processor import ComponentsProcessor
import data_aggregator

DATA_SOURCE_FILE = "data_source.csv"
#DATA_SOURCE_FILE = "data_source_test.csv"

def csv_reader(components_processor:ComponentsProcessor) -> None:
    '''
    Based on https://www.programiz.com/python-programming/csv
    '''

    with open(os.path.join(get_resources_path(), DATA_SOURCE_FILE), 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Retrieve the cell with components and send for processing
            components_processor.process(row[0])

def csv_writer(histogram: data_aggregator.Histogram):
    data = histogram.get_data()

    os.makedirs(os.path.join(get_resources_path(),"out"), exist_ok=True)

    # Write the top level "drivers.csv" file 
    with open(os.path.join(get_resources_path(),"out", "drivers.csv"), 'w') as file:
        writer = csv.writer(file)
        for driver_name, data_value in data.items():
            writer.writerow([driver_name, data_value.count])

            if data_value.child_histogram != None:
                 with open(os.path.join(get_resources_path(),"out", driver_name + ".csv"), 'w') as child_comp_file:
                    child_comp_writer = csv.writer(child_comp_file)

                    child_histogram: data_aggregator.Histogram = data_value.child_histogram
                    for component, value in child_histogram.get_data().items():
                        child_comp_writer.writerow([component, value.count])


def get_resources_path() -> None:
    '''
    Returns path to the resources folder
    '''
    res_env = os.environ.get("RESOURCES_FOLDER")
    if res_env == None:
        raise Exception("RESOURCES_FOLDER undefined")
    
    return res_env

def main():
    '''
    main
    '''
    histogram = data_aggregator.Histogram()
    components_processor = ComponentsProcessor(histogram)
    csv_reader(components_processor)
    csv_writer(histogram)
    
if __name__ == "__main__":
    main()