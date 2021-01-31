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
for key, value in sorted(report_info.items(), key=lambda el: el[0]):
    print(f".{key}")
    print(*[f"--- {v}"for v in value], sep="\n")