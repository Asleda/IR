from collections import defaultdict
from load_model import bingtop,twittertop,intertop,allwords,porn
from hy import RedisQueue
import requests
import socket
import json
from update import clean_text
import numpy as np
from gene_tfidf_feature import tfidf_svd_feat
import time
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
toplist=[]
topic_dict={}
for i in range(46,234):
  toplist.append('RTS{}'.format(i))
  topic_dict['RTS{}'.format(i)]=[]



# topdic={}
# for i in toplist:
#   topdic[i]= [hash(ii)for ii in bingtop[i]]+[hash(ii) for ii in twittertop[i]]+[hash(ii) for ii in intertop[i]]




q=RedisQueue('tweet21')
header={'Content-Type':'application/json'}
num=[]

redun=[]


def try_divide(x, y, val=0.0):

  if y != 0.0:
    val = float(x) / y
  return val


def JaccardCoef(A, B):
  A, B = set(A), set(B)
  intersect = len(A.intersection(B))
  union = len(A.union(B))
  j_d = try_divide(intersect, union)
  return j_d

def redundancy(query,checklist):
  for item in checklist:
    sc=JaccardCoef(query,item)
    redun.append(sc)
  return max(redun)
def push_rel_2(idd,text,topic):
  if len(topic_dict[topic])==10:
    pass
  if len(topic_dict[topic])<10:
    if len(topic_dict[topic])==0:
      topic_dict[topic].append(text)
      try:
      	res=requests.post('http://scspc654.cs.uwaterloo.ca/tweet/{0}/{1}/A9ImWPyrAzxo'.format(topic,idd),headers=header)
      	print res.status_code
      except Exception,exc:
      	pass
      
     
    if redundancy(text,topic_dict[topic])<=.5:
      topic_dict[topic].append(text)
      try:
      	res=requests.post('http://scspc654.cs.uwaterloo.ca/tweet/{0}/{1}/A9ImWPyrAzxo'.format(topic,idd),headers=header)
      	print res.status_code
      except Exception,exc:
      	pass

def push_rank_2(idd,text,topic,score,time):
  text=' '.join(text)
  message='{0}_{1}_{2}_{3}_{4}'.format(time,topic,idd,text,score)
   
  
  # try:
  # 	s.connect(('192.168.1.10', 9992)) 
  # 	s.send(message)
  # 	print("Send B:",message)
  # 	s.close()
  # except socket.error,exc:
  # 	pass
  with open('./02_run2.txt','a') as w:
  	w.write(message)
  	w.write('\n')




while True:
  doc=q.get()
  doc=json.loads(doc)
  for item in clean_text(doc['text'].encode('utf-8'),stop_word=True):
    if len(item[0])>3 and len([1 for ii in item[0] if hash(ii) in allwords])>0 and len([1 for it in item[0] if hash(it) in porn])==0:
      topra=[]
      for top in toplist:
        for ilist in tfidf_svd_feat(item[0],top):
          ratio=sum(ilist[3:])/float(12)

        
        
          topra.append(ratio)
      score=max(topra)
      # print'score is ',score
      if score>=.52:
        t=toplist[np.argmax(topra)]
        print 'this 2 is',t,doc['tweetid']
        push_rel_2(doc['tweetid'],item[0],t)
        push_rank_2(doc['tweetid'],item[0],t,score*100,20170802)
      if score<.52 and score>=.41:
        t=toplist[np.argmax(topra)]
        print 'this 1 is ',t,doc['tweetid']
        push_rank_2(doc['tweetid'],item[0],t,score*80,20170802)














































