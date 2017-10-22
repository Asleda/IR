import tweepy
import time
from tweepy import StreamListener
import json
import time
from langdetect import detect_langs,detect
import sys
sys.path.append('../')
from httplib import IncompleteRead

import string
from hy import RedisQueue
q=RedisQueue('tweet22')

def log_error(msg):
    timestamp = time.strftime('%Y%m%d:%H%M:%S')
    sys.stderr.write("%s: %s\n" % (timestamp,msg))

class StreamWatcherListener(tweepy.StreamListener):
    
  def on_status(self, status):
    
    
    if status.lang=='en':
      #print status
      try:
        text=status.retweeted_status.text.strip('\n')

      except Exception as e:
        text=status.text.strip('\n')
      
      en_num=len([i  for i in text  if i in string.ascii_letters])
      all_num=len([i for i in text])
      asii_ratio=float(en_num)/all_num
      if asii_ratio>=0.8 and all_num>=30:
        doc={'tweetid':status.id,'text':text.encode('utf-8')}
        doc=json.dumps(doc)
        q.put(doc)
        print doc
        
      
      
      
      

      


    

      
      
      
  

  def on_error(self, status_code):
    log_error("Status code: %s." % status_code)
    time.sleep(3)
    return True  # keep stream alive

  def on_timeout(self):
    log_error("Timeout.")


def main():
    
    # auth = tweepy.OAuthHandler('EZJw7FUPtMzsqNiTUEvjVeo2u',  'tqtzpuSB95BgOzO20POexaqk3KKnUd7YEFb34nKShqjGg97PLu')
    # auth.set_access_token('866636850680614912-ns9DMn9hux2HzydryjpmL2A1KPUX7vN', 'B9FTvsF57evHvDiVkOgoAC0xNMqieDhM5mXmWgTygpz7S')
  while  True:
    try:
      auth = tweepy.OAuthHandler('GfkEDJRYxWuUtciXGMXVEeypZ', 'UIqWf8eXoFPb86FVcPJ5Dqf65EIelfs1H7nXGQzrmOWVUcGGXp')
      auth.set_access_token('866636850680614912-LmnMSNMY6aIGbH2pgKN6E04YZN0Ja2w', 'bL4FtVGs08bVhSJlHfl6d2oiSZyWZ7mjhUOD2FLNxyY8z')
      # pro = { "http": "http://127.0.0.1:43943", 
      #             "https": "http://127.0.0.1:43943",}
  
      mylistener = StreamWatcherListener()
      stream = tweepy.Stream(auth, listener=mylistener)
      stream.sample()
    except Exception as  e:
      print e
      continue

if __name__ == '__main__':
  try:
    main()
   
    
  except KeyboardInterrupt:
    pass
  except Exception as e:
    log_error("Exception: %s" % str(e))
    time.sleep(3)