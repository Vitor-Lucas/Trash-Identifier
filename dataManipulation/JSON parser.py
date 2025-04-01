import glob

# final JSON file path
path = "metal.json"

with open(path, 'w') as final_file:
    # Gets all files that end with ".json"
    for file_path in glob.glob("JSONs/*.json"):
        with open(file_path, 'r') as file:
            final_file.write(file.read())