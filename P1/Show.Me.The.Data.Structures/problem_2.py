"""
Finding Files
For this problem, the goal is to write code for finding all files 
under a directory (and all directories beneath it) that end with ".c"
"""
import os

def find_files(suffix, path):  
  assert(suffix)
  assert(path)
  found_files = []

  if os.path.isfile(path):
    if path.endswith(suffix):
      found_files.append(path)
  elif os.path.isdir(path):
    for child in os.listdir(path):
      found_files.extend(find_files(suffix, os.path.join(path, child)))

  return found_files
"""
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
"""
print('-----------------TEST1-------------------')
paths_list = []
print(find_files('c', 'testdir'))

print('-----------------TEST-2-------------------')
paths_list = []
print(find_files('c', 'testdir2')) #returns empty because there is no *.c file in the directory `testdir2`

print('-----------------TEST-3-------------------')
paths_list = []
print(find_files('c', 'testdir3'))#returns testdir3/subdir1/subdir2/huffman.c

print('-----------------TEST-4-------------------')
paths_list = []
print(find_files('c', 'testdir4'))#returns error message saying path doesn't exist.