os.path.join('usr', 'bin', 'spam') ===> 'usr\\bin\\spam'
os.getcwd()
os.chdir('C:\\')
os.makedirs('C:\\new Folder')
os.path.abspath(path) ===> returns absolute pathof file
os.path.isabs(path)
os.path.relpath(path, start) ===> returns string from start to path
os.path.basename('C:\\Windows\\System32\\calc.exe')   >>>  'calc.exe'
os.path.dirname('C:\\Windows\\System32\\calc.exe')   >>>   'C:\\Windows\\System32'
os.path.split('C:\\Windows\\System32\\calc.exe')   >>>  ('C:\\Windows\\System32', 'calc.exe')
calcFilePath.split(os.path.sep)   >>>  ['C:', 'Windows', 'System32', 'calc.exe']
os.path.getsize(path)   >>> returns number of bytes
os.listdir(path)   >>> returns list of strings of all files in the path dir
os.path.exists(path)
os.path.isfile(path)
os.path.isdir(path)

open() #(path, 'r/w/a') read, write, append
read() >>> one string per file
readlines() >>> one string per line
write()
close()

import shelve
shelfFile = shelve.open('data')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile['cats'] >>> ['Zophie', 'Pooka', 'Simon']
shelfFile.close() 














import os, shutil
