import time
import datetime
import json

input=open("cdate.txt",'r')
output = open('delta.txt', 'w')

for line in input:
    row=json.loads(line)
    try:
       
       tweetdate = row['tweetcreateddate']
       t1 = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweetdate,'%a %b %d %H:%M:%S +0000 %Y'))
       t2 = time.strptime(ts, '%Y-%m-%d %H:%M:%S')
       t3 = datetime.datetime.fromtimestamp(time.mktime(t1))
       current = datetime.datetime.now()
       tage = (current-t3).days
        
       carbondate = row['urlcreateddate']
       ct1 = time.strptime(carbondate, '%Y-%m-%dT%H:%M:%S')
       ct2 = datetime.datetime.fromtimestamp(time.mktime(ct1))
       current = datetime.datetime.now()
       cage = (current-ct2).days
        
       delta= abs(tage-cage)
       output.write(str(delta) + '\n')
       
     except:    
        continue


