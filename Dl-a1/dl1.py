import tweepy
import json
import time


ckey = 'qxv1oeg63LrfNDPPvoaaZsfhp'
csecret = 'vJagyLtkwMfEAdKexNXP5jlaUxutWugdpOKNLIQlrYl0VoCANN'
atoken = '81104885-WAbORw6NpXk0iQurbNQtXZhmh3r3E0PWeBY0wYwxB'
asecret = 'gd1ST26f2wYfKnE6bag0ryIkfAb0eJxUDrjn0C9G3pChg'


results = open('twitter','w')
akey = tweepy.OAuthHandler(ckey,csecret)  
print akey

akey.set_access_token(atoken,asecret)
urlcount = set()
api = tweepy.API(akey)
pool = tweepy.Cursor(api.search,q="http:").items()

while True:

   try:

       tweet = pool.next()
       
       line= tweet._json

       row={}
       tcreated_date= line['user']['created_at']
       tid= line['id_str']
       row['tweetid'] = tid

       row['tweetcreateddate'] = tcreated_date
       for link in line['entities']['urls']:

        urlcount.add(link['url'])

        row['url']=link['url']
        results.write(json.dumps(row) + '\n')

        if len(urlcount) == 10000:
             break

   except tweepy.TweepError as e:
        print e
        time.sleep(60 * 2)
        continue

   except StopIteration:

        break


