
import re

file_path = "example.txt"

pattern = re.compile(r'https?://\S+|www\.\S+')

lines_to_keep = []

found_links = False

with open(file_path, 'r') as input_file:
    for line in input_file:
        links = re.findall(pattern, line)
        if links:
            found_links = True
            lines_to_keep.append(' '.join(links) + '\n')

if found_links:
    with open(file_path, 'w') as output_file:
        output_file.writelines(lines_to_keep)
else:
    print("No links were found in the file. The file remains unchanged.")
