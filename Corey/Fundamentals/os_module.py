import os
from datetime import datetime
# print(dir(os))

print(os.getcwd())

os.chdir('C:\\Users\\mange\\PycharmProjects\\GFG_Problems\\Corey')
print(os.getcwd())
print(os.listdir())

# Making directory
os.mkdir('Demo-1') # Useful only for creating single directory
os.makedirs('Demo-2\\sub-dir1') # Useful for creating nested directory

print(os.listdir())

# Removing directory
os.rmdir('Demo-1')
os.removedirs('Demo-2\\sub-dir1')

print(os.listdir())

# Renaming a file
# os.rename('process-images.py','processed-images.py')
# print(os.listdir())

# Getting file information
modtime = os.stat('multi-processing3.py').st_mtime
print(datetime.fromtimestamp(modtime))

# traverse through directories
os.chdir('C:\\Users\\mange\\OneDrive')

for dirpath, dirname, filename in os.walk(os.getcwd()):
    print("Current path: ", dirpath)
    print("Directories: ", dirname)
    print("Files: ", filename)
    print()

# Environment variables
print(os.environ.get('CASSANDRA_HOME'))

# To add filename or to join paths use os.path.join
filepath = os.path.join(os.environ.get('CASSANDRA_HOME'), 'test.txt')
print(filepath)

# Other uses of os.path
print(os.path.dirname('C:\\Users\\mange\\OneDrive'))
print(os.path.basename(filepath))
print(os.path.split(filepath))
print(os.path.isfile(filepath))
print(os.path.isdir(filepath))
print(os.path.exists(filepath))
print(os.path.splitext(filepath))

print(dir(os.path))