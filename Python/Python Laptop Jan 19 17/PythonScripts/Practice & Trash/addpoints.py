import pyperclip

string = pyperclip.paste()
points = string.split("\r\n")

print(points)

for i in range(len(points)):
    points[i] = '* ' + points[i]
    print(points[i])


