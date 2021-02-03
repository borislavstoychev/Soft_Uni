import os


def extract_fails(dir):
    return [el for el in dir if "." in el]


def report_files_extensions(files):
    report = {}
    for file in files:
        name, extension = file.split(".")
        if extension not in report:
            report[extension] = []
        report[extension].append(name)
    return report


dir_content = os.listdir()
files = extract_fails(dir_content)
report_info = report_files_extensions(files)
result = ""
for key, value in sorted(report_info.items(), key=lambda el: el[0]):
    result += f".{key}\n"
    for v in value:
        result += f"- - - {v}.{key}\n"
with open('C:\\Users\\Kofto\\OneDrive\\Работен плот\\my_report_result.txt', "w") as file:
    file.write(result)

