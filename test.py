import os

# Remove the outer "Interview_Preparation" layer
structure = {
    "01_Company_Research": {},
    "02_Programming_and_Algorithms": {
        "01_Data_Structures.md": "",
        "02_Algorithms.md": "",
        "03_Coding_Practice_Problems.md": "",
    },
    "03_Machine_Learning_Fundamentals": {},
    "04_Deep_Learning": {
        "01_Theory.md": "",
        "02_Projects.md": "",
        "03_Coding_Exercises.md": "",
    },
    "05_Computer_Vision": {
        "01_Concepts.md": "",
        "02_Projects.md": "",
    },
    "06_System_Design": {},
    "07_Soft_Skills": {},
    "08_Questions_and_Answers": {},
}

def create_structure(base_path, structure_dict):
    for name, content in structure_dict.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)  # Create folder
            create_structure(path, content)  # Recursive call for subfolders
        else:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)  # Create file with content (empty here)

if __name__ == "__main__":
    create_structure(".", structure)
    print("Folder structure created successfully in current directory!")
