import os



def find_files(suffix, path):
    if path is None:
        return "You forgot to input a path"
    elif not isinstance(path, str):
        return "Double check your path input"

    files = []

    for file in os.listdir(path):

        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            if file.endswith(suffix):
                files.append(file_path)

        if os.path.isdir(file_path):
            new_files = find_files(suffix, file_path)
            files.extend(new_files)

    return files

#set up directory to be searched
test_path = os.getcwd() + "\\Show.Me.The.Data.Structures\\testdir"

# General test cases
print(find_files(".h", test_path))
print(find_files(".c", test_path))
print(find_files(".gitkeep", test_path))

#Edge cases
print(find_files('', None))
print(find_files('', 23)) #GOAT