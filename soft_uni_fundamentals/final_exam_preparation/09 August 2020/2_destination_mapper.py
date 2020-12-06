import re

pattern = r"(=|/)([A-Z][A-Za-z]{2,})\1"
location = [match.group(2) for match in re.finditer(pattern, input())]
print(f"Destinations: {', '.join(location)}")
print(f"Travel Points: {len(list(''.join(location)))}")
