import os

REPORT = os.path.expanduser("~") + "\OneDrive\Работен плот\output.txt"


def extract_fails(directory):
    return [el for el in directory if "." in el]


def report_files_extensions(all_files):
    report = {}
    for f in all_files:
        name, extension = f.split(".")
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
with open(REPORT, "w") as file:
    file.write(result)
