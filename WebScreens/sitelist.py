import csv

f = open('C:\\Users\\Igor\\top-1m.csv')
c = csv.reader(f)

w = open('C:\\Users\\Igor\\Documents\\Dev\\work\\WebScreens\\\\webscreenshot\\top1000.txt', mode="w", encoding="utf-8")

x=1
for row in c:
    if (x <= 1000):  
        data = row[1]
        if(data==""):
            data = row[-1]
            
        w.write(data+"\n")
        print(str(x) + "/1000: "+data)
        x+=1



f.close()
w.close()
    
