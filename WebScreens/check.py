import os, sys, datetime, time, csv, re


def get_files_by_file_size(dirname, reverse=False):
    """ Return list of file paths in directory sorted by file size """

    # Get list of files
    filepaths = []
    for basename in os.listdir(dirname):
        filename = os.path.join(dirname, basename)
        if os.path.isfile(filename):
            filepaths.append(filename)

    # Re-populate list with filename, size tuples
    for i in range(len(filepaths)):
        filepaths[i] = (filepaths[i], os.path.getsize(filepaths[i]))

    # Sort list by file size
    # If reverse=True sort from largest to smallest
    # If reverse=False sort from smallest to largest
    filepaths.sort(key=lambda filename: filename[1], reverse=reverse)

    # Re-populate list with just filenames
    for i in range(len(filepaths)):
        filepaths[i] = filepaths[i][0]

    return filepaths



#f = open('C:\\Users\\Igor\\top-1m.csv')
#c = csv.reader(f)
reg = re.compile(r'(\w*[_])([^_]+)(.*)')

mainlist = []

'''
domlist = []




x=1
for row in c:
    if (x <= 1000):  
        data = row[1]
        if(data==""):
            data = row[-1]
            
        domlist.append(str(data))
        #print(str(x) + "/1000: "+data)
        x+=1

print(len(domlist))
'''

os.chdir('C:\\Users\\Igor\\Documents\\Dev\\work\\WebScreens\\webscreenshot\s\\')
cwd = os.getcwd()

fileList = get_files_by_file_size(cwd, reverse=False)



for file in fileList:
    try:
        regx = reg.search(file)
             
        http, domain, end = regx.groups()
        mainlist.append(domain)
    except (Exception) as e:
        print('Error: %s' %e)



for x in range(100):
    print("http://"+mainlist[x])

'''

for s in domlist:
    data = s
    w.write(data+"\n")
    print("Writing: "+data)



f.close()
w.close()

'''











'''
for file in fileList:
    try:
        regx = reg.search(file)
             
        http, domain, end = regx.groups()

        if (domain in domlist):
            domlist.remove(domain)
            print("removed domain: " + domain)

        '''
'''
        if os.path.exists(picPath) == False:
            print('Create path: ' + picPath)
            os.makedirs(picPath)

        print('Moving File: '+ file + '  to  '+ picPath)
        #shutil.move(os.path.abspath(file), picPath)
        shutil.copy(os.path.abspath(file), picPath)

        filesCopied += 1'''
'''
    except (Exception) as e:
        print('Error: %s' %e)
        
print(domlist)
w = open('C:\\Users\\Igor\\Documents\\Dev\\work\\WebScreens\\\\webscreenshot\\missed.txt', mode="w", encoding="utf-8")
'''