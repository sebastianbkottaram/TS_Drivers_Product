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
    "Go",
    "Java",
    "Node.js",
    "PHP",
    "Python",
    "Ruby",
]

EXCLUDE_LIST = [
    "Atlas",
    "Compass",
    "Atlas Search",
    "Online Archive",
    "Administrative",
    "Ops Manager Installation",
    "Atlas Database Access Configuration",
    "Atlas mongod Version Upgrade",
    "Atlas Serverless",
    "Generic Kubernetes",
    "Sharding",
    "WiredTiger Storage",
    "mongoimport",
    "mongodump",
    "mongorestore",
    "Atlas Data Explorer",
    "AWS",
    "AWS Lambda",
    "Containerization",
    "Atlas Data Lake",
    "Atlas Data Federation",
    "Private Endpoint",
    "Atlas Connection Limitations",
    "LDAP",
    "DNS",
    "Selfhosted mongod Version Upgrade",
    "SDAM",
    "Installation",
    "Replication",
    "Sharding",
    "Atlas Alerts",
    "Atlas Metrics",
    "Atlas Integrations",
    "Ops Manager",
    "OM/CM Version Change",
    "Ops Manager Automation",
    "Kubernetes Operator",
    "Ops Manager Version Upgrade",
    "Atlas Connection Limitations",
    "Atlas Storage",
    "WiredTiger Storage",
    "FIPS",
    "Kerberos",
    "Atlas mongod Version Downgrade",
    "Migration",
    "Atlas Cluster Resources Change",
    "Atlas Performance Advisor",
    "NTSE",
    "Access List",
    "Atlas Triggers",
    "Cloud Manager",
    "OM/CM Automation",
    "SlotBased Execution",
    "OM/CM API",
    "MongoDB Enterprise Server",
    "Configuration",
    "Realm Functions",
    "Stability",
    "Realm .NET SDK",
    "Realm",

    ]


def get_components(component_driver, assigned_component, case_number, case_number_list):
    components_list = assigned_component.split(",")

    for component in components_list:

        if component.strip() in DRIVER_NAMES:
            continue
        elif component.strip() in EXCLUDE_LIST:
            continue
        elif component.strip() in component_driver:
            component_driver[component.strip()] += 1
            updated_case_number = "%s  %s"%(case_number_list[component.strip()], case_number)
            case_number_list[component.strip()] = updated_case_number

        else:
            component_driver[component.strip()] = 1
            case_number_list[component.strip()] = str(case_number)

    return component_driver


def create_worksheets(component_dict, component_name, case_number):
    data_frame = pd.DataFrame(
        {'Components': component_dict.keys(), 'Count': component_dict.values(), 'CaseNumber': case_number.values()})

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
        rustCases = scalaCases = swiftCases = 0

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

    javaCaseNumber = {}
    pythonCaseNumber = {}
    nodeCaseNumber = {}
    cSharpCaseNumber = {}
    cplusCaseNumber = {}
    cCaseNumber = {}
    goCaseNumber = {}
    phpCaseNumber = {}
    rubyCaseNumber = {}
    rustCaseNumber = {}
    scalaCaseNumber = {}
    swiftCaseNumber = {}
    otherCaseNumber = {}

    for fields in records_data:
        if 'JavaScript' in fields.get("Components") or 'Mongoose' in fields.get("Components"):
            nodeCases += 1
            get_components(nodeComponents, fields.get("Components"), fields.get("Case Number"), nodeCaseNumber)
        elif 'Java' in fields.get("Components") or 'Spring' in fields.get("Components"):
            javaCases += 1
            get_components(javaComponents, fields.get("Components"), fields.get("Case Number"), javaCaseNumber)
        elif 'Python' in fields.get("Components"):
            pythonCases += 1
            get_components(pythonComponents, fields.get("Components"), fields.get("Case Number"), pythonCaseNumber)
        elif 'Node.js' in fields.get("Components"):
            nodeCases += 1
            get_components(nodeComponents, fields.get("Components"), fields.get("Case Number"), nodeCaseNumber)
        elif 'C# Driver' in fields.get("Components") or '.NET' in fields.get("Components"):
            cSharpCases += 1
            get_components(cSharpComponents, fields.get("Components"), fields.get("Case Number"), cSharpCaseNumber)
        elif 'C++ Driver' in fields.get("Components"):
            cplusCases += 1
            get_components(cplusComponents, fields.get("Components"), fields.get("Case Number"), cplusCaseNumber)
        elif 'C Driver' in fields.get("Components"):
            cCases += 1
            get_components(cComponents, fields.get("Components"), fields.get("Case Number"), cCaseNumber)
        elif 'Go' in fields.get("Components"):
            goCases += 1
            get_components(goComponents, fields.get("Components"), fields.get("Case Number"), goCaseNumber)
        elif 'PHP' in fields.get("Components"):
            phpCases += 1
            get_components(phpComponents, fields.get("Components"), fields.get("Case Number"), phpCaseNumber)
        elif 'Ruby' in fields.get("Components"):
            rubyCases += 1
            get_components(rubyComponents, fields.get("Components"), fields.get("Case Number"), rubyCaseNumber)
        elif 'Rust' in fields.get("Components"):
            rustCases += 1
            get_components(rustComponents, fields.get("Components"), fields.get("Case Number"), rustCaseNumber)
        elif 'Scala' in fields.get("Components"):
            scalaCases += 1
            get_components(scalaComponents, fields.get("Components"), fields.get("Case Number"), scalaCaseNumber)
        elif 'Swift' in fields.get("Components"):
            swiftCases += 1
            get_components(swiftComponents, fields.get("Components"), fields.get("Case Number"), swiftCaseNumber)
        else:
            print(fields)
            continue

    data_frame = pd.DataFrame({'Languages': ['C', 'C++', 'C#', 'Go', 'Java', 'Node.js', 'PHP', 'Python', 'Ruby', 'Rust',
                                             'Scala', 'Swift'],
                               'Count': [cCases, cplusCases, cSharpCases, goCases, javaCases, nodeCases, phpCases,
                                         pythonCases, rubyCases, rustCases, scalaCases, swiftCases]})

    # write to dataframe

    worksheet = sheet.add_worksheet(title='Language Components', rows=50, cols=50)

    set_with_dataframe(worksheet, data_frame)

    create_worksheets(cComponents, "C", cCaseNumber)

    create_worksheets(cplusComponents, "C++", cplusCaseNumber)

    create_worksheets(cSharpComponents, "C#", cSharpCaseNumber)

    create_worksheets(javaComponents, "Java", javaCaseNumber)

    create_worksheets(nodeComponents, "Node.js", nodeCaseNumber)

    create_worksheets(phpComponents, "PHP", phpCaseNumber)

    create_worksheets(pythonComponents, "Python", pythonCaseNumber)

    create_worksheets(rubyComponents, "Ruby", rubyCaseNumber)

    create_worksheets(rustComponents, "Rust", rustCaseNumber)

    create_worksheets(scalaComponents, "Scala", scalaCaseNumber)

    create_worksheets(swiftComponents, "Swift", swiftCaseNumber)
