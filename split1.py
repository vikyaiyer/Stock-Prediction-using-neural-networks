import csv
with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    i=0
    j=0
    filename=1
    for row in readCSV:
        csvfile1 = open('dataRO/fileRO-{}.csv'.format(row[0]), 'r')#.readlines()
        outfilename = open('file-{}.csv'.format(filename),'a')
        for row in csvfile1:
            #print (csvfile1.name)
            if(i==0):
                i=i+1
                continue
            outfilename.writelines(row[0:])
            print(row[0:])
            if(i==10):
                i=0
                break
            i=i+1;
        j=j+1
        if(j%10==0):
            filename=filename+1
               #print (csvfile1.name)
                #csvfile1.readlines()
                #open(str(filename) + '.csv', 'w+').writelines(csvfile1[i:i+100])
    
