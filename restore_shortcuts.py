# import OS module
import os
from typing import List

source_directory = f"{os.environ['USERPROFILE']}\\Documents\\Desktop"
destination_directory = f"{os.environ['USERPROFILE']}\\Desktop"

print(source_directory, destination_directory)


# Get the list of all files and directories
def get_files_list(directory) -> List[str]:
    return os.listdir(directory)


source_shortcuts = get_files_list(source_directory)
destination = get_files_list(destination_directory)


for shortcut in source_shortcuts:
    if shortcut not in destination:
        s = f'copy {source_directory}\\"{shortcut}" {destination_directory}\\"{shortcut}"'
        s = r'{}'.format(s)
        os.popen(s)
        print(shortcut, s)
