import os
from pathlib import Path
from datetime import datetime, time
import pathlib
import glob
from tempfile import TemporaryDirectory, TemporaryFile
import tempfile
import shutil
import zipfile 
import tarfile
import fileinput
import sys



                                                    #read and write
with open ('C:/Users/duyan/OneDrive - Hanoi University/Chuyên ngành/SS1/ass2/data.txt', 'w') as f:   #(with as : context manager)
    f.write ("my name is duy anh")
with open ('C:/Users/duyan/OneDrive - Hanoi University/Chuyên ngành/SS1/ass2/data.txt', 'r') as f:

    data=f.read()


                                                    # list all in a directory
                                  
# os.listdir()	        Returns a list of all files and folders in a directory
# os.scandir()	        Returns an iterator of all the objects in a directory including file attribute information
# pathlib.Path.iterdir()	Returns an iterator of all the objects in a directory including file attribute information



# entries = os.listdir('C:/Users/duyan/OneDrive - Hanoi University/Chuyên ngành/SS1/Lect')

# entries = os.scandir('C:/Users/duyan/OneDrive - Hanoi University/Chuyên ngành/SS1/Lect')

# with os.scandir('C:/Users/duyan/OneDrive - Hanoi University/Chuyên ngành/SS1/Lect') as entri:
#     for entr in entri: 
#         print  (entr.name)
#     print()

# entries = Path('C:/Users/duyan/OneDrive - Hanoi University/Chuyên ngành/SS1/Lect')

# for entry in entries.iterdir(): 
# 	print(entry.name)

                        #list all files in diretory
basepath1 ='C:/Users/duyan/OneDrive - Hanoi University/Chuyên ngành/SS1/ass2'               
#using os.listdir()
# for entry in os.listdir(basepath):
#     if os.path.isfile (os.path.join(basepath,entry)): 
#         print(entry)

#using os.scandir
# with os.scandir(basepath) as entries: 
#     for entry in entries: 
#         if entry.is_file(): 
#             print(entry.name)

#using path lib 
basepath2 = Path('C:/Users/duyan/OneDrive - Hanoi University/Chuyên ngành/SS1/ass2')
# for item in path.iterdir(): 
#     if item.is_file():
 
# files= (entry for entry in basepath2.iterdir() if entry.is_file())
# for item in files:
#     print(item.name)


            #list subdirectory 
#using os.listdir
# for entry in os.listdir(basepath1): 
#     if os.path.isdir(os.path.join(basepath1,entry)):
#         print (entry)

#using scandir
# with os.scandir(basepath1) as entries: 
#     for entry in entries: 
#         if entry.is_dir():
#             print (entry.name)

#using path lib
# same as listing file 



                                            #getting file's attribute
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date
# scandir
# with os.scandir(basepath1) as dir_contents: 
#     for entry in dir_contents: 
#         print((entry.stat()).st_mtime)


# path lib 
# for path in basepath2.iterdir(): 
#     print(f' {path.name}: {convert_date((path.stat()).st_mtime)}')



                    # making directory
# os.mkdir
# os.mkdir(basepath1 +'/duyanh')


# path lib
# p = Path(basepath1+ '/duyanh')
# p.mkdir(exist_ok= True) #to ignore error
# try: 
#     p.mkdir()
# except FileExistsError as ex: 
#     print(ex)


                # making  multiple directories
#os.makedirs
# os.makedirs('2001/6/10', mode=0o770)


#path lib 
# p = pathlib.Path('2001/6/10')
# p.mkdir(parents=True)




                                 #Filename pattern matching 
# startswith()	                        Tests if a string starts with a specified pattern and returns True or False      
# endswith()	                        Tests if a string ends with a specified pattern and returns True or False           ex:  endswith(".txt")
# fnmatch.fnmatch(filename, pattern)	Tests whether the filename matches the pattern and returns True or False            ex:  fnmatch.fnmatchh(filenam, '*.txt'),  .fnmatch(filename, 'data_*_backup.txt')
# glob.glob()	                        Returns a list of filenames that match a pattern                                    ex: glob.glob('*.py)
# pathlib.Path.glob()	                Finds patterns in path names and returns a generator object   




                                    #Traversing Directories and Processing Files
# for dirpath, dirnames, files in os.walk(basepath1+ '/', topdown= False):
#     print(f'Found directory: {dirpath}')
#     for file_name in files:
#         print(file_name)



                                    # Making Temporary Files and Directories
# Create a temporary file and write some data to it
# fp = TemporaryFile('w+t')
# fp.write('Hello universe!')

# # Go back to the beginning and read data from file
# fp.seek(0)
# data = fp.read()
# print(data)
# # Close the file, after which it will be removed
# fp.close()

# create temp directory
# with tempfile.TemporaryDirectory() as tmpdir:
#     print('Created temporary directory ', tmpdir)
#     print(os.path.exists(tmpdir))

# # Created temporary directory  /tmp/tmpoxbkrm6c
# # True
# print()
# print()

# # Directory contents have been removed
# print(tmpdir)
# # '/tmp/tmpoxbkrm6c'
# print(os.path.exists(tmpdir))
# # False




                                        #Deleting Files and Directories

                        #Delete file
#os.unlink / os.remove
#os.unlink ('C:/Users/duyan/OneDrive - Hanoi University/Chuyên ngành/SS1/ass2/data.txt')
file = basepath1 + '/duyanh/duyanh copy.py'
# try: 
#     os.remove(file)
# except OSError as e: 
#     print(f'Error {file} : {e.strerror}')


#Path lib 
# dlt = Path(file)
# try:
#     dlt.unlink()
# except IsADirectoryError as e:
#     print(f'Error: {dlt} : {e.strerror}')



                #Delete directory 
trash_dir = basepath1 + '/duyanh/sub_dir'
#os.rmdir() / pathlib.rmdir()   (work only when directory is empty)
# try:
#     os.rmdir(trash_dir)
# except OSError as e:
#     print(f'Error: {trash_dir} : {e.strerror}')



#path lib 
# dlt = Path(trash_dir)

# try:
#     dlt.rmdir()
# except OSError as e:
#     print(f'Error: {dlt} : {e.strerror}')



#shutil.rmtree()
# trash = basepath1+ '/duyanh/sub_dir copy'
# try:
#     shutil.rmtree(trash)
# except OSError as e:
#     print(f'Error: {trash} : {e.strerror}')


# os.remove()	            Deletes a file and does not delete directories
# os.unlink()	            Is identical to os.remove() and deletes a single file
# pathlib.Path.unlink()	    Deletes a file and cannot delete directories
# os.rmdir()	            Deletes an empty directory
# pathlib.Path.rmdir()	    Deletes an empty directory
# shutil.rmtree()	        Deletes entire directory tree and can be used to delete non-empty directories




                            #Copying, Moving, and Renaming Files and Directories 


                            #copying 
#copy file 
# src = basepath1+ '/duyanh/duyanh copy 2.py' # file 
# dst = basepath1+ '/duyanh/sub_dir copy' #directory
# shutil.copy(src, dst)  # if dst is a file, its content will be replaced by file src
#Using .copy2() preserves details about the file such as last access time, permission bits, last modification time, and flags.

#copy directory
# fd1 = basepath1 + '/duyanh/haha' 
# shutil.copytree(fd1, 'hoho')  # dst hoho must not alreaady exist


                            #moving 
# shutil.move (basepath1+ '/duyanh/haha/' ,basepath1+ '/duyanh/backup/')   ## if directory dst not exist, src will be renamed to dst / if exist, move content from src to dst
                           

                            #rename
# os.rename (src,dst) 

# path lib 
#data_file = Path ( 'file.txt'(path to the file) )
# data_file.rename ( 'newfile.txt' )  




                                    #Archive 

                #reading zip file

# #first step: create zip file object                
# with zipfile.ZipFile('data.zip', 'r') as zipobj: 

# # get list of files in archive, call namelist() on zipfile object 
#     zipobj.namelist()   # return a list of names of the files and directories in the archive 
# # retrive information of archive
#     bar_info = zipobj.getinfo('pass a path of a single member of the archive here ')
#     bar_info.file_size # return size 
# # date_time ; filename ; compress_size





                    #Extracting  zip 

# os.listdir('.')  #show current directory has only data.zip 
# ['data.zip']

# data_zip = zipfile.ZipFile('data.zip', 'r')

# # Extract a single file to current directory
# data_zip.extract('file1.py')    #extract to the current directory , also take a path as parameter to specify a direcotry to extract, if not exist,  create auto  


# os.listdir('.')
# ['file1.py', 'data.zip']

# # Extract all files into a different directory
# data_zip.extractall(path='extract_dir/')  #extract all to different dir (extract_dir/) 

# os.listdir('.')
# ['file1.py', 'extract_dir', 'data.zip']

# os.listdir('extract_dir')
# ['file1.py', 'file3.py', 'file2.py', 'sub_dir']

# data_zip.close()


                    #extract from password protected archive
# with zipfile.ZipFile('secret.zip', 'r') as pwd_zip:
#     # Extract from a password protected archive
#     pwd_zip.extractall(path='extract_dir', pwd='Quish3@o')

#This opens the secret.zip archive in read mode. A password is supplied to .extractall(), and the archive contents are extracted to extract_dir. The archive is closed automatically after the extraction is complete thanks to the with statement.


                    #create a new zip archive
# create new archive and add
# file_list = ['file1.py', 'sub_dir/', 'sub_dir/bar.py', 'sub_dir/foo.py']
# with zipfile.ZipFile('new.zip', 'w') as new_zip:   #open in write mode erases current contents and create new archives 
#     for name in file_list:
#         new_zip.write(name)


# add to exist archive 
# Open a ZipFile object in append mode
# with zipfile.ZipFile('new.zip', 'a') as new_zip:    #open in append mode allow to add file without being erase
#     new_zip.write('data.txt')
#     new_zip.write('latin.txt')



                #Open TAR archive
# with tarfile.open('example.tar', 'r') as tar_file:
#     print(tar_file.getnames()) 
# equal to 
# tar = tarfile.open('example.tar', mode='r')
# tar.getnames()

# output: ['CONTRIBUTING.rst', 'README.md', 'app.py']

#To open compressed TAR files, pass in a mode argument to tarfile.open() that is in the form filemode[:compression]  
# Mode	            Action
# r	             Opens archive for reading with transparent compression
# r:gz	         Opens archive for reading with gzip compression
# r:bz2	         Opens archive for reading with bzip2 compression
# r:xz         	 Opens archive for reading with lzma compression
# w	             Opens archive for uncompressed writing
# w:gz	         Opens archive for gzip compressed writing
# w:xz	         Opens archive for lzma compressed writing
# a	             Opens archive for appending with no compression


# getnames(): returns files's name in TAR file 



# for entry in tar.getmembers():
#     print(entry.name)
#     print(' Modified:', time.ctime(entry.mtime))
#     print(' Size    :', entry.size, 'bytes')
#     print()

# output 
# CONTRIBUTING.rst
#  Modified: Sat Nov  1 09:09:51 2018
#  Size    : 402 bytes

# README.md
#  Modified: Sat Nov  3 07:29:40 2018
#  Size    : 5426 bytes

# app.py
#  Modified: Sat Nov  3 07:29:13 2018
#  Size    : 6218 bytes


                    # Extracting Files From a TAR Archive
#extract a single file  extract()

# tar.extract('README.md')
# os.listdir('.')
# output : ['README.md', 'example.tar']

#extract all 
# tar.extractall(path="extracted/")  #path: specified directory when extract 

# extract for reading and writing 
# f = tar.extractfile('app.py')
# f.read()
# tar.close()



                                #Creating New TAR Archives

# file_list = ['app.py', 'config.py', 'CONTRIBUTORS.md', 'tests.py']   # list of file to be added 
# with tarfile.open('packages.tar', mode='w') as tar:   #context manager to open new archive called packaged.tar in write mode 
#     for file in file_list:
#         tar.add(file)

# # Read the contents of the newly created archive
# with tarfile.open('package.tar', mode='r') as t:
#     for member in t.getmembers():
#         print(member.name)

# output: 
# app.py
# config.py
# CONTRIBUTORS.md
# tests.py



                        #Working With Compressed Archives

    #Example: to read or write data to a TAR archive compressed using gzip, use the 'r:gz' or 'w:gz'
# files = ['app.py', 'config.py', 'tests.py']
# with tarfile.open('packages.tar.gz', mode='w:gz') as tar:
#     tar.add('app.py')
#     tar.add('config.py')
#     tar.add('tests.py')

# with tarfile.open('packages.tar.gz', mode='r:gz') as t:
#     for member in t.getmembers():
#         print(member.name)

# output:
# app.py
# config.py
# tests.py



                        #An Easier Way of Creating Archives
#shutil.make_archive()  take at least 2 argument: name of archive and an archive format  ( support zip,tar,bztar,gztar) 
#  By default compress all files in the current directory into archive specified in arguments, an pass in an optional root_dir argument to compress files in a different directory

# #shutil.make_archive(base_name, format, root_dir)
# shutil.make_archive('data/backup', 'tar', 'data/')
# This copies everything in data/ and creates an archive called backup.tar in the filesystem and returns its name


# extract archive: 
# shutil.unpack_archive('backup.tar', 'extract_dir/')  # pass an archive name and dst directory  
# copy content of backup.tar into extract_dir/   - Same to ZIP 




                        #Reading Multiple Files
        #format 
# for line in fileinput.input():
#     process(line)


#Let’s use fileinput to build a crude version of the common UNIX utility cat.
#The cat utility reads files sequentially, writing them to standard output.
#When given more than one file in its command line arguments, cat will concatenate the text files and display the result in the terminal:


# File: fileinput-example.py
# files = fileinput.input()
# for line in files:
#     if fileinput.isfirstline():
#         print(f'\n--- Reading {fileinput.filename()} ---')
#     print(' -> ' + line, end='')
# print()

#output: 
# $ python3 fileinput-example.py bacon.txt cupcake.txt
# --- Reading bacon.txt ---
#  -> Spicy jalapeno bacon ipsum dolor amet in in aute est qui enim aliquip,
#  -> irure cillum drumstick elit.
#  -> Doner jowl shank ea exercitation landjaeger incididunt ut porchetta.
#  -> Tenderloin bacon aliquip cupidatat chicken chuck quis anim et swine.
#  -> Tri-tip doner kevin cillum ham veniam cow hamburger.
#  -> Turkey pork loin cupidatat filet mignon capicola brisket cupim ad in.
#  -> Ball tip dolor do magna laboris nisi pancetta nostrud doner.

# --- Reading cupcake.txt ---
#  -> Cupcake ipsum dolor sit amet candy I love cheesecake fruitcake.
#  -> Topping muffin cotton candy.
#  -> Gummies macaroon jujubes jelly beans marzipan.


#fileinput allows you to retrieve more information about each line such as whether or not it is the first line (.isfirstline()), the line number (.lineno()), and the filename (.filename())