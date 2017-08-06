#Author: Blake Conrad
#Purpose: Takes a table of the form:
#
# fields, dateTimes
# id f1 f2 ... fN 07/03/2030 00:00 .. 07/03/2030 23:45 08/03/2030 00:00 .. 10/03/2030 23:45
#
# into
#
# fields, date, times
# id f1 f2 ... fN DAY 00:00 00:15 00:30 .. 23:45
#
#
field_names = []
data = []
n=4 # because you had 4 fields before datetimes started

with open("Workbook1.csv", "r") as f_in:
    field_names = map(lambda x:x.rstrip(), f_in.readline().split(","))
    data = map(lambda x:x.rstrip(), f_in.readlines()[:])

unique_dates = list(set(map(lambda x:x.split(" ")[0],field_names[n:])))
unique_times = list(set(map(lambda x:x.split(" ")[1],field_names[n:])))

new_fields = field_names[:n] + ["day"] + map(lambda x:x.split(" ")[1],
field_names[n:100])
field_names[4:100]   #1st day
field_names[104:196] #2nd day
field_names[196:292] #3rd day
field_names[292:388] #4th day

def flatten_to_strings(listOfLists):
    """Flatten a list of (lists of (lists of strings)) for any level 
    of nesting"""
    result = []

    for i in listOfLists:
        # Only append if i is a basestring (superclass of string)
        if isinstance(i, basestring):
            result.append(i)
        # Otherwise call this function recursively
        else:
            result.extend(flatten_to_strings(i))
    return result

new_data = []
for row in data:
    newRow1=[]
    newRow2=[]
    newRow3=[]
    newRow4=[]
    splits = row.split(",")
    newRow1.append(splits[:n])
    newRow1.append('7/3/30')
    newRow1.append(splits[n:100])
    
    newRow2.append(splits[:n])
    newRow2.append('8/3/30')
    newRow2.append(splits[104:196])
    
    newRow3.append(splits[:n])
    newRow3.append('9/3/30')
    newRow3.append(splits[196:292])
    
    newRow4.append(splits[:n])
    newRow4.append('10/3/30')
    newRow4.append(splits[292:388])
    
    newRow1[:] = flatten_to_strings(newRow1)
    newRow2[:] = flatten_to_strings(newRow2)
    newRow3[:] = flatten_to_strings(newRow3)
    newRow4[:] = flatten_to_strings(newRow4)
               
    new_data.append(newRow1)
    new_data.append(newRow2)
    new_data.append(newRow3)
    new_data.append(newRow4)
