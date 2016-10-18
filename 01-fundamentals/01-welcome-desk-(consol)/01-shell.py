# Good online PDF
# - http://hplgit.github.io/edu/ostasks/ostasks.pdf



# Even in the terminal you have to import os
import os

# Get current working directory
os.getcwd()

# List everything in the directory
os.listdir(os.curdir)

# Navigate into a directory
# *REMINDER drag folder into terminal to display URI
os.chdir("/example/folder/")

# Make a folder
os.mkdir(’mydir’)

# Rename a file
os.rename(oldname, newname)


##################################################
# Fix for pycharm lost directory from move issue #
##################################################

# Now open a directory "/tmp"
fd = os.open( "/tmp", os.O_RDONLY )

# Use os.fchdir() method to change the dir
os.fchdir(fd)

# Close opened directory.
os.close( fd )

