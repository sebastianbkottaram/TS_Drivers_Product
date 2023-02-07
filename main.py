import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from gspread_dataframe import set_with_dataframe

DRIVER_NAMES = [
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

# LANG_ODM_NAMES = [
#     "Go",
#     "Java",
#     "JavaScript",
#     "Mongoose",
#     "Node.js",
#     "PHP",
#     "Python",
#     "Ruby",
#     "Spring Data",
#     "Swift",
#     ".NET"
# ]


def get_components(component_driver, value):
    components_list = value.split(";")

    for component in components_list:

        if component.strip() in DRIVER_NAMES:
            continue
        elif component.strip() in component_driver:
            component_driver[component.strip()] += 1
        else:
            component_driver[component.strip()] = 1

    return component_driver


def create_worksheets(component_dict, component_name):
    data_frame = pd.DataFrame({'Components': component_dict.keys(), 'count': component_dict.values()})

    # write to dataframe

    worksheet = sheet.add_worksheet(title=component_name, rows=300, cols=300)

    set_with_dataframe(worksheet, data_frame)


if __name__ == "__main__":
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        '/Users/sebaty/PycharmProjects/excel/data/sebatyexcel-e4284260d5f2.json', scope)

    client = gspread.authorize(creds)

    sheet = client.open('sample_spreadsheet')

    sheet_instance = sheet.get_worksheet(0)

    records_data = sheet_instance.get_all_records()

    javaCases = pythonCases = nodeCases = cSharpCases = cplusCases = cCases = goCases = phpCases = rubyCases = \
        rustCases = scalaCases = swiftCases = otherCases = 0

    javaComponents = {}
    pythonComponents = {}
    nodeComponents = {}
    cSharpComponents = {}
    cplusComponents = {}
    cComponents = {}
    goComponents = {}
    phpComponents = {}
    rubyComponents = {}
    rustComponents = {}
    scalaComponents = {}
    swiftComponents = {}
    otherComponents = {}

    print(records_data)

    for fields in records_data:
        if 'Java' in fields.get("Components") or 'Spring' in fields.get("Components"):
            javaCases += 1
            get_components(javaComponents, fields.get("Components"))
        elif 'Python' in fields.get("Components"):
            pythonCases += 1
            get_components(pythonComponents, fields.get("Components"))
        elif 'Node' in fields.get("Components") or 'Mongoose' in fields.get("Components"):
            nodeCases += 1
            get_components(nodeComponents, fields.get("Components"))
        elif 'C#' in fields.get("Components") or '.Net' in fields.get("Components"):
            cSharpCases += 1
            get_components(cSharpComponents, fields.get("Components"))
        elif 'C++' in fields.get("Components"):
            cplusCases += 1
            get_components(cplusComponents, fields.get("Components"))
        elif 'C Driver' in fields.get("Components"):
            cCases += 1
            get_components(cComponents, fields.get("Components"))
        elif 'Go' in fields.get("Components"):
            goCases += 1
            get_components(goComponents, fields.get("Components"))
        elif 'PHP' in fields.get("Components"):
            phpCases += 1
            get_components(phpComponents, fields.get("Components"))
        elif 'Ruby' in fields.get("Components"):
            rubyCases += 1
            get_components(rubyComponents, fields.get("Components"))
        elif 'Rust' in fields.get("Components"):
            rustCases += 1
            get_components(rustComponents, fields.get("Components"))
        elif 'Scala' in fields.get("Components"):
            scalaCases += 1
            get_components(scalaComponents, fields.get("Components"))
        elif 'Swift' in fields.get("Components"):
            swiftCases += 1
            get_components(swiftComponents, fields.get("Components"))
        else:
            otherCases += 1
            get_components(otherComponents, fields.get("Components"))

    data_frame = pd.DataFrame({'Languages': ['C', 'C++', 'C#', 'Go', 'Java', 'Node.js', 'PHP', 'Python', 'Ruby', 'Rust',
                                             'Scala', 'Swift', 'Others'],
                               'Count': [cCases, cplusCases, cSharpCases, goCases, javaCases, nodeCases, phpCases,
                                         pythonCases, rubyCases, rustCases, scalaCases, swiftCases, otherCases]})

    # write to dataframe

    worksheet = sheet.add_worksheet(title='Programming Language Cases', rows=50, cols=50)

    set_with_dataframe(worksheet, data_frame)

    create_worksheets(cComponents, "C")

    create_worksheets(cplusComponents, "C++")

    create_worksheets(cSharpComponents, "C#")

    create_worksheets(javaComponents, "Java")

    create_worksheets(nodeComponents, "Node.js")

    create_worksheets(phpComponents, "PHP")

    create_worksheets(pythonComponents, "Python")

    create_worksheets(rubyComponents, "Ruby")

    create_worksheets(rustComponents, "Rust")

    create_worksheets(scalaComponents, "Scala")

    create_worksheets(swiftComponents, "Swift")

    create_worksheets(otherComponents, "Others")
