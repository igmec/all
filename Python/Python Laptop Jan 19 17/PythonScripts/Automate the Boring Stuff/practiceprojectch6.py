tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

maxLen = [0]*len(tableData)

for i in range(len(tableData)):    
    for j in range(len(tableData[i])):
        if len(tableData[i][j]) > maxLen[i]:
            maxLen[i] = len(tableData[i][j])
        

for i in range(len(tableData[0])):
    for j in range(len(tableData)):
        print((tableData[j][i]).rjust(maxLen[j]), end='  ')

    print()
        
