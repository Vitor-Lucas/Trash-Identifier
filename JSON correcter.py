import glob

'''
Since each of our group members made their own annotations, the JSON files that were exported had 
their classification as 0. So, we had to create a script that changed the category's classification 
to the ones we needed
'''

categories = {
    'cardboard': 1,
    'glass': 0,
    'battery': 2,
    'metal': 3,
    'plastic': 4
}

for category in categories.keys():
    print('----------------------------------')
    print(f'Category: {category} is being changed')
    print('----------------------------------')
    for file_path in glob.glob(f"{category}/obj_train_data/*.txt"):
        print(f'File: {file_path} opened')
        with open(file_path, 'r') as file:
            copied_file = []
            for line in file.readlines():
                line = f"{categories[category]}" + line[1:]
                copied_file.append(line)

        with open(file_path, 'w') as file:
            for line in copied_file:
                file.write(line)
        print(f'File {file_path} closed')