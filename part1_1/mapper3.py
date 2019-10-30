import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    
    street_code1 = line[10]
    street_code2 = line[11]
    street_code3 = line[12]
    
    if street_code1 != 0 and street_code2 != 0 and street_code3 != 0:
        location = str(street_code1) + ":" + str(street_code2) + ":" + str(street_code3) 
        print '%s\t%d' % (location, 1)
