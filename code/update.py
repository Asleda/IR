
import sys 
sys.path.append('../')
from collections import defaultdict
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
from nltk.corpus import stopwords
import spacy
import string
import re
from sklearn.decomposition import TruncatedSVD


cachestopwords=stopwords.words('english')
punctuations=string.punctuation
nlp=spacy.load('en_core_web_sm')







# ##########################
bing_bg=defaultdict(list)
bing_tg=defaultdict(list)
bing_ug=defaultdict(list)
##########################
twitter_bg=defaultdict(list)
twitter_tg=defaultdict(list)
twitter_ug=defaultdict(list)
##########################
inter_bg=defaultdict(list)
inter_tg=defaultdict(list)
inter_ug=defaultdict(list)
##########################
bingtop=defaultdict(list)
twittertop=defaultdict(list)
intertop=defaultdict(list)
###############################



join_str="_"

######################################################################################
def getUnigram(words):
    """
        Input: a list of words, e.g., ['I', 'am', 'Denny']
        Output: a list of unigram
    """
    assert type(words) == list
    return words
    

def getBigram(words, join_string, skip=0):
  """
     Input: a list of words, e.g., ['I', 'am', 'Denny']
     Output: a list of bigram, e.g., ['I_am', 'am_Denny']
     I use _ as join_string for this example.
  """
  assert type(words) == list
  L = len(words)
  if L > 1:
    lst = []
    for i in range(L-1):
      for k in range(1,skip+2):
        if i+k < L:
          lst.append( join_string.join([words[i], words[i+k]]) )
  else:
    # set it as unigram
    lst = getUnigram(words)
  return lst
    
def getTrigram(words, join_string, skip=0):
  """
     Input: a list of words, e.g., ['I', 'am', 'Denny']
     Output: a list of trigram, e.g., ['I_am_Denny']
     I use _ as join_string for this example.
  """
  assert type(words) == list
  L = len(words)
  if L > 2:
    lst = []
    for i in range(L-2):
      for k1 in range(1,skip+2):
        for k2 in range(1,skip+2):
          if i+k1 < L and i+k1+k2 < L:
            lst.append( join_string.join([words[i], words[i+k1], words[i+k1+k2]]) )
  else:
    # set it as bigram
    lst = getBigram(words, join_string, skip)
  return lst
#######################################################################################
with open('../data/bing_stop.txt','rt') as r:
  for line in r.readlines():
    items=line.split('|')
    topic=items[0]
    words=[i for i in items[1].strip('\n').split(' ') if i!='']
    

    bing_ug[topic].append(getUnigram(words))
    bing_bg[topic].append(getBigram(words,join_str))
    bing_tg[topic].append(getTrigram(words,join_str))
  for key,value in bing_bg.items():
    bing_bg[key]=list(set(y for x in value for y in x))
  for key,value in bing_tg.items():
    bing_tg[key]=list(set(y for x in value for y in x))
  for key,value in bing_ug.items():
    bing_ug[key]=list(set(y for x in value for y in x))
joblib.dump(bing_ug,'../data/model/bing_ug.model')
joblib.dump(bing_bg,'../data/model/bing_bg.model')
joblib.dump(bing_tg,'../data/model/bing_tg.model')
###################################
with open('../data/twitter_stop.txt','rt') as r:
  for line in r.readlines():
    items=line.split('|')
    topic=items[0]
    words=[i for i in items[1].strip('\n').split(' ') if i!='']
    

    twitter_ug[topic].append(getUnigram(words))
    twitter_bg[topic].append(getBigram(words,join_str))
    twitter_tg[topic].append(getTrigram(words,join_str))
  for key,value in twitter_bg.items():
    twitter_bg[key]=list(set(y for x in value for y in x))
  for key,value in twitter_tg.items():
    twitter_tg[key]=list(set(y for x in value for y in x))
  for key,value in twitter_ug.items():
    twitter_ug[key]=list(set(y for x in value for y in x))
joblib.dump(twitter_ug,'../data/model/twitter_ug.model')
joblib.dump(twitter_bg,'../data/model/twitter_bg.model')
joblib.dump(twitter_tg,'../data/model/twitter_tg.model')
###################################
with open('../data/inter_stop.txt','rt') as r:
  for line in r.readlines():
    items=line.split('|')
    topic=items[0]
    words=[i for i in items[1].strip('\n').split(' ') if i!='']
    

    inter_ug[topic].append(getUnigram(words))
    inter_bg[topic].append(getBigram(words,join_str))
    inter_tg[topic].append(getTrigram(words,join_str))
  for key,value in inter_bg.items():
    inter_bg[key]=list(set(y for x in value for y in x))
  for key,value in inter_tg.items():
    inter_tg[key]=list(set(y for x in value for y in x))
  for key,value in inter_ug.items():
    inter_ug[key]=list(set(y for x in value for y in x))
joblib.dump(inter_ug,'../data/model/inter_ug.model')
joblib.dump(inter_bg,'../data/model/inter_bg.model')
joblib.dump(inter_tg,'../data/model/inter_tg.model')
#######################################################################################

with open('../data/bing_top25.txt','rt') as r:
  for line in r.readlines():
    items=line.split('|')
    topic=items[0]
    for i in items[1].strip('\n').split(' '):
      if i!='':
        bingtop[topic].append(i)
joblib.dump(bingtop,'../data/model/bingtop.model')

##################################################
with open('../data/twitter_top20.txt','rt') as r:
  for line in r.readlines():
    items=line.split('|')
    topic=items[0]
    for i in items[1].strip('\n').split(' '):
      if i!='':
        twittertop[topic].append(i)
joblib.dump(twittertop,'../data/model/twittertop.model')


##################################################

with open('../data/inter_top10.txt','rt') as r:
  for line in r.readlines():
    items=line.split('|')
    topic=items[0]
    for i in items[1].strip('\n').split(' '):
      if i!='':
        intertop[topic].append(i)
joblib.dump(intertop,'../data/model/intertop.model')

##################################################################################
"""this use all stopword generate dic"""
def stem_tokens(tokens):
  tokens=' '.join(tokens)
  doc=nlp(unicode(tokens,errors='replace'))
  stemmed = [token.lemma_.lower() for token in doc if token.lemma_!="-PRON-"]
  return stemmed
def clean_text(text,stop_word=False):
  url_exist=0
  
  if re.search(r'((https|http|ftp|rtsp|mms)?:\/\/)[^\s]+',text) or re.search(r'\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}',text):
    text=re.sub(r'((https|http|ftp|rtsp|mms)?:\/\/)[^\s]+|\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}','',text)
    url_exist=1
  if re.search(r'@[a-zA-Z0-9]+',text):
    text=re.sub(r'@[a-zA-Z0-9]+','',text)
  if re.search(r'\bx[a-z0-9]{2}',text):
    text=re.sub(r'\bx[a-z0-9]{2}','',text)
 
  token_pattern = r"(?u)\b\w\w+\b"
  token_pattern = re.compile(token_pattern, flags = re.UNICODE | re.LOCALE)
  term = [token.lower() for token in token_pattern.findall(text) ]
  term = stem_tokens(term)
  term=[token for token in term if re.search(r'_',token)==None ]
  term=[token for token in term if token!='rt']
  term=[token for token in term if len(token)<15]
  if stop_word==True:
    term=[token for token in term if token not in cachestopwords]
  term=[token for token in term  if re.search(r'\b\d+',token)==None]

  yield (term,url_exist)

def bing_intel_tweet(path):
  with open(path,'rt') as r:
    for line in r.readlines():
      row=line.split('|')
      topic=row[0]
      text=[i for i in row[1:]]
      #for text in row[1:]:
      

      yield (text,topic)

def  make_dic(path):
  topic_text_dic=defaultdict(list)
  
  for item in bing_intel_tweet(path):
    text=item[0]
    topic=item[1]
    for i in text:
      for ii in clean_text(i,stop_word=True):
        if len(ii[0])!=0:
          topic_text_dic[topic].append(ii[0])
  return topic_text_dic

dic_list=[]
texts=[]
bing_all_tfidf,bing_all_svd={},{}
twitter_all_tfidf,twitter_all_svd={},{}
inter_all_tfidf,inter_all_svd={},{}




tfidf_text=['../data/bing.txt','../data/twitter.txt','../data/inter.txt']
for i in tfidf_text:
  dic_list.append(make_dic(i))
  texts=[' '.join(bbb) for b in dic_list for bb in b.values() for bbb in bb]

count_vect=CountVectorizer()
tfidf_transform = TfidfTransformer()
svd_transform = TruncatedSVD(n_components=30,n_iter=7,random_state=42)

tfidf_transform.fit_transform(count_vect.fit_transform(texts))
svd_transform.fit_transform(count_vect.fit_transform(texts))


#########################
for key,value in bingtop.items():
  value_tf=tfidf_transform.transform(count_vect.transform([' '.join(value)]))
  value_svd=svd_transform.transform(count_vect.transform([' '.join(value)]))
  bing_all_tfidf[key]=value_tf
  bing_all_svd[key]=value_svd

#########################
for key,value in twittertop.items():
  value_tf=tfidf_transform.transform(count_vect.transform([' '.join(value)]))
  value_svd=svd_transform.transform(count_vect.transform([' '.join(value)]))
  twitter_all_tfidf[key]=value_tf
  twitter_all_svd[key]=value_svd
#########################
for key,value in intertop.items():
  value_tf=tfidf_transform.transform(count_vect.transform([' '.join(value)]))
  value_svd=svd_transform.transform(count_vect.transform([' '.join(value)]))
  inter_all_tfidf[key]=value_tf
  inter_all_svd[key]=value_svd


joblib.dump(bing_all_tfidf,'../data/model/bing_all_tfidf.model')
joblib.dump(bing_all_svd,'../data/model/bing_all_svd.model')

joblib.dump(twitter_all_tfidf,'../data/model/twitter_all_tfidf.model')
joblib.dump(twitter_all_svd,'../data/model/twitter_all_svd.model')

joblib.dump(inter_all_tfidf,'../data/model/inter_all_tfidf.model')
joblib.dump(inter_all_svd,'../data/model/inter_all_svd.model')

joblib.dump(count_vect,'../data/model/count_vect.model')
joblib.dump(tfidf_transform,'../data/model/tfidf_transform.model')
joblib.dump(svd_transform,'../data/model/svd_transform.model')
###########################################################################################
#tfidf_text=['../data/bing.txt','../data/twitter.txt','../data/inter.txt']
bing_texts=[' '.join(bb) for b in make_dic('../data/bing.txt').values()  for bb in b]
twitter_texts=[' '.join(bb) for b in make_dic('../data/twitter.txt').values() for bb in b]
inter_texts=[' '.join(bb) for b in make_dic('../data/inter.txt').values() for bb in b]

count_vect_solo_bing=CountVectorizer()
tfidf_transform_solo_bing= TfidfTransformer()
svd_transform_solo_bing= TruncatedSVD(n_components=30,n_iter=7,random_state=42)
tfidf_transform_solo_bing.fit_transform(count_vect_solo_bing.fit_transform(bing_texts))
svd_transform_solo_bing.fit_transform(count_vect_solo_bing.fit_transform(bing_texts))

bing_solo_tfidf,bing_solo_svd={},{}
for key,value in bingtop.items():
  value_tf=tfidf_transform_solo_bing.transform(count_vect_solo_bing.transform([' '.join(value)]))
  value_svd=svd_transform_solo_bing.transform(count_vect_solo_bing.transform([' '.join(value)]))
  bing_solo_tfidf[key]=value_tf
  bing_solo_svd[key]=value_svd

joblib.dump(count_vect_solo_bing,'../data/model/count_vect_solo_bing.model')
joblib.dump(tfidf_transform_solo_bing,'../data/model/tfidf_transform_solo_bing.model')
joblib.dump(svd_transform_solo_bing,'../data/model/svd_transform_solo_bing.model')
joblib.dump(bing_solo_tfidf,'../data/model/bing_solo_tfidf.model')
joblib.dump(bing_solo_svd,'../data/model/bing_solo_svd.model')
####################################################
count_vect_solo_twitter=CountVectorizer()
tfidf_transform_solo_twitter= TfidfTransformer()
svd_transform_solo_twitter= TruncatedSVD(n_components=30,n_iter=7,random_state=42)
tfidf_transform_solo_twitter.fit_transform(count_vect_solo_twitter.fit_transform(twitter_texts))
svd_transform_solo_twitter.fit_transform(count_vect_solo_twitter.fit_transform(twitter_texts))

twitter_solo_tfidf,twitter_solo_svd={},{}
for key,value in twittertop.items():
  value_tf=tfidf_transform_solo_twitter.transform(count_vect_solo_twitter.transform([' '.join(value)]))
  value_svd=svd_transform_solo_twitter.transform(count_vect_solo_twitter.transform([' '.join(value)]))
  twitter_solo_tfidf[key]=value_tf
  twitter_solo_svd[key]=value_svd

joblib.dump(count_vect_solo_twitter,'../data/model/count_vect_solo_twitter.model')
joblib.dump(tfidf_transform_solo_twitter,'../data/model/tfidf_transform_solo_twitter.model')
joblib.dump(svd_transform_solo_twitter,'../data/model/svd_transform_solo_twitter.model')
joblib.dump(twitter_solo_tfidf,'../data/model/twitter_solo_tfidf.model')
joblib.dump(twitter_solo_svd,'../data/model/twitter_solo_svd.model')
####################################################
count_vect_solo_inter=CountVectorizer()
tfidf_transform_solo_inter= TfidfTransformer()
svd_transform_solo_inter= TruncatedSVD(n_components=30,n_iter=7,random_state=42)
tfidf_transform_solo_inter.fit_transform(count_vect_solo_inter.fit_transform(inter_texts))
svd_transform_solo_inter.fit_transform(count_vect_solo_inter.fit_transform(inter_texts))

inter_solo_tfidf,inter_solo_svd={},{}
for key,value in intertop.items():
  value_tf=tfidf_transform_solo_inter.transform(count_vect_solo_inter.transform([' '.join(value)]))
  value_svd=svd_transform_solo_inter.transform(count_vect_solo_inter.transform([' '.join(value)]))
  inter_solo_tfidf[key]=value_tf
  inter_solo_svd[key]=value_svd

joblib.dump(count_vect_solo_inter,'../data/model/count_vect_solo_inter.model')
joblib.dump(tfidf_transform_solo_inter,'../data/model/tfidf_transform_solo_inter.model')
joblib.dump(svd_transform_solo_inter,'../data/model/svd_transform_solo_inter.model')
joblib.dump(inter_solo_tfidf,'../data/model/inter_solo_tfidf.model')
joblib.dump(inter_solo_svd,'../data/model/inter_solo_svd.model')

###########################
allwords=[]
stop_list=['bing_stop','twitter_stop','inter_stop']
for i in stop_list:
  with open('../data/{}.txt'.format(i),'rt') as r:
    for line in r.readlines():
      a=line.split('|')
      for ii in a[1].strip('\n').split(' '):
        
        allwords.append(hash(ii))
joblib.dump(allwords,'../data/model/allwords.model')

      






