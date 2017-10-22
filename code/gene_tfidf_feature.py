from load_model import bingtop,twittertop,intertop,count_vect,tfidf_transform,svd_transform,bing_all_tfidf,bing_all_tfidf,bing_all_svd,twitter_all_tfidf,twitter_all_svd,inter_all_tfidf,inter_all_svd,count_vect_solo_bing,tfidf_transform_solo_bing,svd_transform_solo_bing,bing_solo_tfidf,bing_solo_svd,count_vect_solo_twitter,tfidf_transform_solo_twitter,svd_transform_solo_twitter,twitter_solo_tfidf,twitter_solo_svd,count_vect_solo_inter,tfidf_transform_solo_inter,svd_transform_solo_inter,inter_solo_tfidf,inter_solo_svd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np



def cosine_sim(x, y):
    try:
        d = cosine_similarity(x, y)
        d = d[0][0]
    except:
        print x
        print y
        d = 0.
    return d

def tfidf_svd_feat(term,topic):

  ################################################
  query_in_bing_num=sum([1 for i in term if i in  bingtop[topic]])
  query_in_twitter_num=sum([1 for i in term if i in twittertop[topic]])
  query_in_inter_num=sum([1 for i in term if i.encode('utf-8') in intertop[topic]])
  ################################################
  aa=[' '.join(term)]
  ################################################
  """all"""
  cd=count_vect.transform(aa)
  aa_tfidf=tfidf_transform.transform(cd)
  
  all_bingidf_cos=cosine_sim(aa_tfidf,bing_all_tfidf[topic])
  all_twitteridf_cos=cosine_sim(aa_tfidf,twitter_all_tfidf[topic])
  all_interidf_cos=cosine_sim(aa_tfidf,inter_all_tfidf[topic])

  aa_svd=svd_transform.transform(cd)

  all_bingsvd_cos=cosine_sim(aa_svd,bing_all_svd[topic])
  all_twittersvd_cos=cosine_sim(aa_svd,twitter_all_svd[topic])
  all_intersvd_cos=cosine_sim(aa_svd,inter_all_svd[topic])
  # ##############################################
  ca=count_vect_solo_bing.transform(aa)
  cb=count_vect_solo_twitter.transform(aa)
  cc=count_vect_solo_inter.transform(aa)

  ###############################################
  """tfidf solo"""
  term_solo_bing=tfidf_transform_solo_bing.transform(ca)
  solo_bing_tfidf=cosine_sim(term_solo_bing,bing_solo_tfidf[topic])
  term_solo_twitter=tfidf_transform_solo_twitter.transform(cb)
  solo_twitter_tfidf=cosine_sim(term_solo_twitter,twitter_solo_tfidf[topic])
  term_solo_inter=tfidf_transform_solo_inter.transform(cc)
  solo_inter_tfidf=cosine_sim(term_solo_inter,inter_solo_tfidf[topic])
  # ###############################################
  # """svd solo"""
  term1_solo_bing=svd_transform_solo_bing.transform(ca)
  solo_bing_svd=cosine_sim(term1_solo_bing,bing_solo_svd[topic])
  term1_solo_twitter=svd_transform_solo_twitter.transform(cb)
  solo_twitter_svd=cosine_sim(term1_solo_twitter,twitter_solo_svd[topic])
  term1_solo_inter=svd_transform_solo_inter.transform(cc)
  solo_inter_svd=cosine_sim(term1_solo_inter,inter_solo_svd[topic])

  yield [query_in_bing_num,query_in_twitter_num,query_in_inter_num,all_bingidf_cos,all_twitteridf_cos,all_interidf_cos,all_bingsvd_cos,all_twittersvd_cos,all_intersvd_cos,\
        solo_bing_tfidf,solo_twitter_tfidf,solo_inter_tfidf,solo_bing_svd,solo_twitter_svd,solo_inter_svd]



  

