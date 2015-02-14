import json
import requests

statcodes={}
input=open('twitter.txt','r')
output = open('urlresponsecodes', 'w')

for row in input:
    irow=json.loads(row)
    try:
        status = requests.head(eachLink['url'], allow_redirects=True)
        array = []
        array.append(status.status_code)
        history = status.history
        
        for line in history:
            arr.append(line.status_code)
        statcodes['statuscodes'] = arr
        statcodes['tweetcreatedDate']=irow['tweetcreateddate']
        statcodes['urlaftercurl']=status.url

        urlresponsecodes.write(json.dumps(statcodes) + '\n')
    except:    
        continue