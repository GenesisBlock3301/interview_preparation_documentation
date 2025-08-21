import os

# Remove the outer "Interview_Preparation" layer
structure = {
    "01_Company_Research": {},

    "02_Programming_Fundamentals": {
        "01_Python_Core.md": "",
        "02_OOP.md": "",
        "03_Data_Structures.md": "",
        "04_Algorithms.md": "",
        "05_SQL.md": "",
        "06_Problem_Solving_Practice.md": "",
    },

    "03_System_Design": {
        "01_High_Level_Design.md": "",
        "02_Low_Level_Design.md": "",
        "03_Design_Principles.md": "",
        "04_Design_Patterns.md": "",
    },

    "04_Computer_Science_Core": {
        "01_Operating_System.md": "",
        "02_Networking.md": "",
    },

    "05_Machine_Learning_and_AI": {
        "01_ML_Fundamentals.md": "",
        "02_Deep_Learning.md": "",
        "03_Computer_Vision.md": "",
    },

    "06_Soft_Skills_and_Behavioral": {
        "01_Communication.md": "",
        "02_Leadership.md": "",
        "03_Teamwork.md": "",
    },

    "07_FAQ_and_QA.md": ""
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
