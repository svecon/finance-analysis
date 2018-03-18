import csv, os, glob

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

filenames = glob.glob('*statement.csv')

runningTotal = 0
for filename in reversed(filenames):
    with open(filename, encoding='UTF-8') as csvfile:
        add = 0
        sub = 0

        yeardate = filename.replace('_statement.csv', '').replace('_', '/')
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            if (len(row)<3): continue

            volume = row[2]
            volume = volume.replace(',', '.')
            
            if (not is_number(volume)): continue
            volume = float(volume)


            if (volume > 0):
                add += volume
            else:
                sub += volume
        
        runningTotal += add + sub
        print(yeardate, add, sub, sep='\t')

