"""
Python program to

● create directories using mkdir( ) and makedirs ( )

● remove directories using rmdir( ) and removedirs( )

change current directory
"""

import os

os.mkdir("test_dir")  
os.makedirs("parent_dir/child_dir") 
os.makedirs("parent_dir/child2_dir")

print("Directories created.")

temp = input("Blocking further execution to observe directories, enter to continue: ")

os.chdir("parent_dir")
print("Current directory changed to:", os.getcwd())

os.rmdir("child_dir")  
os.rmdir("child2_dir")
os.chdir("..")  
os.removedirs("parent_dir") 
os.rmdir("test_dir")

print("Directories removed.")
