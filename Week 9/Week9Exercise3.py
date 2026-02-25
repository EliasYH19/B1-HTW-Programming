import os

def file_manager_demo():
    """Demonstrates file and directory operations using os module"""
    
    # 1. Display current working directory
    current_dir = os.getcwd()
    print(f"Current Directory: {current_dir}\n")
    
    # 2. Create a new folder
    folder_name = "lab_files"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"7 Created folder: {folder_name}")
    else:
        print(f"Folder '{folder_name}' already exists")
    
    # 3. Create three empty text files
    file_names = ["file1.txt", "file2.txt", "file3.txt"]
    for file_name in file_names:
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'w') as f:
            f.write(f"This is {file_name}")
        print(f"7 Created file: {file_name}")
    
    # 4. List all files in the folder
    print(f"\n=== Files in {folder_name} ===")
    files = os.listdir(folder_name)
    for file in files:
        print(f"- {file}")
        
    # 5. Rename one file
    old_path = os.path.join(folder_name, "file2.txt")
    new_path = os.path.join(folder_name, "renamed_file.txt")
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"\n7 Renamed 'file2.txt' to 'renamed_file.txt'")
    
    # Show files after rename
    print(f"\n=== Files after rename ===")
    files = os.listdir(folder_name)
    for file in files:
        print(f"- {file}")
        
    # 6. Cleanup - remove files and folder
    print(f"\n=== Cleaning up ===")
    for file in os.listdir(folder_name):
        file_path = os.path.join(folder_name, file)
        os.remove(file_path)
        print(f"7 Deleted: {file}")
        
    os.rmdir(folder_name)
    print(f"7 Removed folder: {folder_name}")
    print("\nAll cleanup completed successfully!")

# Run the demonstration
file_manager_demo()