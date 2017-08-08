import os, shutil, pprint, re, sys, datetime, time, pprint

os.chdir('C:\\Users\\Igor\\Desktop\\Camera\\Camera\\')
cwd = os.getcwd()

fileList = os.listdir(cwd)
months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

#Regex
multiRegex = re.compile(r'\w*_(\d\d\d\d)(\d\d)(\d\d)_\w*.\w+') #Camera Format
eRegex = re.compile(r'(\w*_)?(\d*).(\w+)') #Epoch Time

'''
for file in fileList:
    date = os.path.getmtime(os.path.abspath(file))
    print(date)
    sys.exit(0)
'''
numFiles = len(fileList)
filesCopied = 0
notAdded = []

for file in fileList:
    try:
        mr = multiRegex.search(file)
        # mr is empty if epoch time, convert to IMG_xx_xx.x format
        if mr == None:
            
            mr = eRegex.search(file)
            unixTime = mr.group(2)
            date = datetime.datetime.fromtimestamp(int(unixTime)/1000).strftime('%Y%m%d_%H%M%S')

            if mr.group(3) == 'mp4':
                newFile = 'VID_'
            else:
                newFile = 'IMG_'

            newFile = newFile + date + '(S).' +mr.group(3)
            #print(file + ' converted to:  '+ newFile)
            #print(os.path.abspath(file)+', '+ os.path.dirname(os.path.abspath(file))+'\\'+newFile)
            #shutil.move(os.path.abspath(file), os.path.dirname(os.path.abspath(file))+'\\'+newFile)

            file = newFile
            mr = multiRegex.search(newFile)

            
        year, month, day = mr.groups()
        month = int(month)

        picPath = ('C:\\Users\\Igor\\Desktop\\Camera2\\' + str(year) + '\\' + str(month) + ' - ' + str(months[month]))

        if os.path.exists(picPath) == False:
            print('Create path: ' + picPath)
            os.makedirs(picPath)

        print('Moving File: '+ file + '  to  '+ picPath)
        #shutil.move(os.path.abspath(file), picPath)
        shutil.copy(os.path.abspath(file), picPath)

        filesCopied += 1
        
    except (Exception) as e:
        print('Error: %s' %e)
        notAdded.append(file)
            
print('Copied ' + str(filesCopied) + ' out of ' + str(numFiles)+'\nNot copied:')
pprint.pprint(notAdded)
sys.exit(0)
