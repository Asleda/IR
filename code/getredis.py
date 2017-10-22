from hy import RedisQueue
import time
from update import clean_text
import json
import sys
sys.path.append('../')
from load_model import allwords,firstmodel,minmax,secondmodel
from  gene_count_feature import  count_feat
from gene_distance_feature import  distance_feat
from gene_tfidf_feature import tfidf_svd_feat
from update import getBigram,getTrigram
import numpy as np
import requests
import socket

q=RedisQueue('tweet4')
header={'Content-Type':'application/json'}

topic_list=[]
topic_dict={}
redun=[]
for i in range(46,234):
  topic_list.append('RTS{}'.format(i))
  topic_dict['RTS{}'.format(i)]=[]


# def try_divide(x, y, val=0.0):

#   if y != 0.0:
#     val = float(x) / y
#   return val


# def JaccardCoef(A, B):
#   A, B = set(A), set(B)
#   intersect = len(A.intersection(B))
#   union = len(A.union(B))
#   j_d = try_divide(intersect, union)
#   return j_d

# def redundancy(query,checklist):
#   for item in checklist:
#     sc=JaccardCoef(query,item)
#     redun.append(sc)
#   return max(redun)


def push_rel_2(idd,text,topic):
  if len(topic_dict[topic])==10:
    pass
  if len(topic_dict[topic])<10:
    if len(topic_dict[topic])==0:
      topic_dict[topic].append(text)
      res=requests.post('http://scspc654.cs.uwaterloo.ca/tweet/{0}/{1}/Voat1N7Fd0Wc'.format(topic,idd),headers=header)
      print res.status_code
    if redundancy(text,topic_dict[topic])<.6:
      topic_dict[topic].append(text)
      res=requests.post('http://scspc654.cs.uwaterloo.ca/tweet/{0}/{1}/Voat1N7Fd0Wc'.format(topic,idd),headers=header)
      print res.status_code

def push_rank(idd,text,topic,score,time):
  text=' '.join(text)
  message='{0}|{1}|{2}|{3}|{4}\n'.format(time,topic,idd,text,score)
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
  s.connect(('192.168.1.10', 9991)) 
  s.send(message)
  print("Send B:",message)
  s.close()



while True:
  doc=q.get()
  doc=json.loads(doc)
  #print doc['text'].encode('utf-8')
  
  #for item in clean_text(doc['text'].encode('utf-8'),stop_word=True):
    #if len(item[0])>3 and len([1 for ii in item[0] if hash(ii) in allwords])>0:
  query=list(doc['text'])

  query_b=getBigram(query,'_')
  query_t=getTrigram(query,'_')
  query_all=[]
  for top in topic_list:
    count_ff=count_feat(query,query_b,query_t,top,doc['url'])
      
    distance_ff=distance_feat(query,query_b,query_t,top)
    tfidf_ff=tfidf_svd_feat(query,top)
        
    query_ff=[i+ii+iii for i in count_ff for ii in distance_ff for iii in tfidf_ff][0]
        #print 'combine feature is ',query_ff
    query_all.append(query_ff)
  query_all=minmax.transform(np.array(query_all))
  result=secondmodel.predict(query_all)
  print result
      #print query_all
      # pre_1=(firstmodel.predict_proba(query_all)[:,1]>.3).astype(int)
      # fir_index=[index for index,item in enumerate(pre_1) if item==1]
      # if fir_index!=[]:
      #   secode_result=secondemodel.predict(query_all[fir_index])
      #   re_2=[index_2 for index_2,i in enumerate(secode_result) if i==2]
      #   re_1=[index_1 for index_1,i in enumerate(secode_result) if i==1]
      #   if re_2!=[]:
      #     rel_top_2=topic_list[fir_index[re_2]]
      #     for topic2 in rel_top_2:
      #       push_rel_2(doc['tweetid'],item[0],topic2)
            #push_rank(doc['tweetid'],item[0],topic2,100,2017)

        # if re_1!=[]:
        #   rel_top_1=topic_list[fir_index[re_1]]
        #   for topic1 in rel_top_1:
        #     push_rank(doc['tweetid'],item[0],topic1,80,2017)



















        

        








      
      


  
