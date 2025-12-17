import os
from random import randint



"""
INTRUCTIONS

This file will take a directory_path and will go through
every file in every folder inside this directory.

The sript will, then, rename the files by removing the
characters until the first character is a number.
The idea behind this is that every file has a pattern
that goes like this "[Type]_[date]_[time]" and by removing
the first characters up until the first number,
the file would be named with the date and time.



"""



# ====== USAGE ======
# Replace this path with the folder you want to clean up
directory_path = r"C:\Users\Usuário\Pictures\Phone Storage\Camera"  # Example for Windows
# directory_path = "/home/user/Pictures"  # Example for Linux/Mac


def rename_files_by_date(root_directory):
    print(f"Changin the files in the following folderpath:\n{root_directory}")
    filesCount = 0;
    filesChanged = 0;

    numbers = "0123456789"
    
    # Walk through all subdirectories and files
    for folder_path, _, files in os.walk(root_directory):
        for filename in files:
            filesCount += 1;
            # Find the first underscore
            if filename[0] not in numbers:
                # Split at the first underscore and keep the part after it
                for count in range(0, len(filename)):
                    if filename[count] in numbers:
                        new_name = filename[count:];
                        
                        # Build full paths
                        old_file = os.path.join(folder_path, filename);
                        new_file = os.path.join(folder_path, new_name);
                        
                        # Rename only if the new name is different
                        if old_file != new_file:
                            if os.path.exists(new_file):
                                parts = new_name.rsplit(".");
                                new_name = parts[0] + "(" + str(randint(1, 999)) + ")." + parts[1];
                                new_file = os.path.join(folder_path, new_name);
                            print(f"Renaming: {filename} -> {new_name}");
                            filesChanged += 1;
                            os.rename(old_file, new_file);
                        break
    print("\nNumber of files:", filesCount, "| Files renamed:", filesChanged)

rename_files_by_date(directory_path)

input("Press Enter to close the program...")
