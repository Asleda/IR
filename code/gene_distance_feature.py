from load_model import bing_bg,bing_ug,bing_tg,twitter_ug,twitter_bg,twitter_tg,inter_ug,inter_bg,inter_tg
from update import getBigram,getTrigram
import numpy as np


###########################################################################################
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

def DiceDist(A, B):
  A, B = set(A), set(B)
  intersect = len(A.intersection(B))
  union = len(A) + len(B)
  d_d = try_divide(2*intersect, union)
  return d_d

def compute_dist(A, B, dist="jaccard_coef"):
  if dist == "jaccard_coef":
      d = JaccardCoef(A, B)
  elif dist == "dice_dist":
      d = DiceDist(A, B)
  return d

def pairwise_jaccard_coef(A, B):
  coef = np.zeros((A.shape[0], B.shape[0]), dtype=float)
  for i in range(A.shape[0]):
      for j in range(B.shape[0]):
          coef[i,j] = JaccardCoef(A[i], B[j])
  return coef
    
def pairwise_dice_dist(A, B):
  d = np.zeros((A.shape[0], B.shape[0]), dtype=float)
  for i in range(A.shape[0]):
      for j in range(B.shape[0]):
          d[i,j] = DiceDist(A[i], B[j])
  return d

def pairwise_dist(A, B, dist="jaccard_coef"):
  if dist == "jaccard_coef":
      d = pairwise_jaccard_coef(A, B)
  elif dist == "dice_dist":
      d = pairwise_dice_dist(A, B)
  return d
###########################################################################################


def  distance_feat(term_u,term_b,topic):
  query_u_bing_jd=compute_dist(term_u,bing_ug[topic],dist="jaccard_coef")
  query_u_twitter_jd=compute_dist(term_u,twitter_ug[topic],dist="jaccard_coef")
  query_u_inter_jd=compute_dist(term_u,inter_ug[topic],dist="jaccard_coef")

  query_u_bing_dd=compute_dist(term_u,bing_ug[topic],dist="dice_dist")
  query_u_twitter_dd=compute_dist(term_u,twitter_ug[topic],dist="dice_dist")
  query_u_inter_dd=compute_dist(term_u,inter_ug[topic],dist="dice_dist")




  query_u_bing_pjd=try_divide(sum([ii for i in pairwise_dist(np.array(term_u),np.array(bing_ug[topic]),dist="jaccard_coef") for ii in i]),np.array(term_u).shape[0]*np.array(bing_ug[topic]).shape[0])
  query_u_twitter_pjd=try_divide(sum([ii for i in pairwise_dist(np.array(term_u),np.array(twitter_ug[topic]),dist="jaccard_coef") for ii in i]),np.array(term_u).shape[0]*np.array(twitter_ug[topic]).shape[0])
  query_u_inter_pjd=try_divide(sum([ii for i in pairwise_dist(np.array(term_u),np.array(inter_ug[topic]),dist="jaccard_coef") for ii in i]),np.array(term_u).shape[0]*np.array(inter_ug[topic]).shape[0])

  query_u_bing_pdd=try_divide(sum([ii for i in pairwise_dist(np.array(term_u),np.array(bing_ug[topic]),dist="dice_dist") for ii in i]),np.array(term_u).shape[0]*np.array(bing_ug[topic]).shape[0])
  query_u_twitter_pdd=try_divide(sum([ii for i in pairwise_dist(np.array(term_u),np.array(twitter_ug[topic]),dist="dice_dist") for ii in i]),np.array(term_u).shape[0]*np.array(twitter_ug[topic]).shape[0])
  query_u_inter_pdd=try_divide(sum([ii for i in pairwise_dist(np.array(term_u),np.array(inter_ug[topic]),dist="dice_dist") for ii in i]),np.array(term_u).shape[0]*np.array(inter_ug[topic]).shape[0])






  ###################################################################
  query_b_bing_jd=compute_dist(term_b,bing_bg[topic],dist="jaccard_coef")
  query_b_twitter_jd=compute_dist(term_b,twitter_bg[topic],dist="jaccard_coef")
  query_b_inter_jd=compute_dist(term_b,inter_bg[topic],dist="jaccard_coef")

  query_b_bing_dd=compute_dist(term_b,bing_bg[topic],dist="dice_dist")
  query_b_twitter_dd=compute_dist(term_b,twitter_bg[topic],dist="dice_dist")
  query_b_inter_dd=compute_dist(term_b,inter_bg[topic],dist="dice_dist")




  # query_b_bing_pjd=try_divide(sum([ii for i in pairwise_dist(np.array(term_b),np.array(bing_bg[topic]),dist="jaccard_coef") for ii in i]),np.array(term_b).shape[0]*np.array(bing_bg[topic]).shape[0])
  # query_b_twitter_pjd=try_divide(sum([ii for i in pairwise_dist(np.array(term_b),np.array(twitter_bg[topic]),dist="jaccard_coef") for ii in i]),np.array(term_b).shape[0]*np.array(twitter_bg[topic]).shape[0])
  # query_b_inter_pjd=try_divide(sum([ii for i in pairwise_dist(np.array(term_b),np.array(inter_bg[topic]),dist="jaccard_coef") for ii in i]),np.array(term_b).shape[0]*np.array(inter_bg[topic]).shape[0])

  # query_b_bing_pdd=try_divide(sum([ii for i in pairwise_dist(np.array(term_b),np.array(bing_bg[topic]),dist="dice_dist") for ii in i]),np.array(term_b).shape[0]*np.array(bing_bg[topic]).shape[0])
  # query_b_twitter_pdd=try_divide(sum([ii for i in pairwise_dist(np.array(term_b),np.array(twitter_bg[topic]),dist="dice_dist") for ii in i]),np.array(term_b).shape[0]*np.array(twitter_bg[topic]).shape[0])
  # query_b_inter_pdd=try_divide(sum([ii for i in pairwise_dist(np.array(term_b),np.array(inter_bg[topic]),dist="dice_dist") for ii in i]),np.array(term_b).shape[0]*np.array(inter_bg[topic]).shape[0])





  ###################################################################
  # query_t_bing_jd=compute_dist(term_t,bing_tg[topic],dist="jaccard_coef")
  # query_t_twitter_jd=compute_dist(term_t,twitter_tg[topic],dist="jaccard_coef")
  # query_t_inter_jd=compute_dist(term_t,inter_tg[topic],dist="jaccard_coef")

  # query_t_bing_dd=compute_dist(term_t,bing_tg[topic],dist="dice_dist")
  # query_t_twitter_dd=compute_dist(term_t,twitter_tg[topic],dist="dice_dist")
  # query_t_inter_dd=compute_dist(term_t,inter_tg[topic],dist="dice_dist")

  

  # query_t_bing_pjd=try_divide(sum([ii for i in pairwise_dist(np.array(term_t),np.array(bing_tg[topic]),dist="jaccard_coef") for ii in i]),np.array(term_t).shape[0]*np.array(bing_tg[topic]).shape[0])
  # query_t_twitter_pjd=try_divide(sum([ii for i in pairwise_dist(np.array(term_t),np.array(twitter_tg[topic]),dist="jaccard_coef") for ii in i]),np.array(term_t).shape[0]*np.array(twitter_tg[topic]).shape[0])
  # query_t_inter_pjd=try_divide(sum([ii for i in pairwise_dist(np.array(term_t),np.array(inter_tg[topic]),dist="jaccard_coef") for ii in i]),np.array(term_t).shape[0]*np.array(inter_tg[topic]).shape[0])

  # query_t_bing_pdd=try_divide(sum([ii for i in pairwise_dist(np.array(term_t),np.array(bing_tg[topic]),dist="dice_dist") for ii in i]),np.array(term_t).shape[0]*np.array(bing_tg[topic]).shape[0])
  # query_t_twitter_pdd=try_divide(sum([ii for i in pairwise_dist(np.array(term_t),np.array(twitter_tg[topic]),dist="dice_dist") for ii in i]),np.array(term_t).shape[0]*np.array(twitter_tg[topic]).shape[0])
  # query_t_inter_pdd=try_divide(sum([ii for i in pairwise_dist(np.array(term_t),np.array(inter_tg[topic]),dist="dice_dist") for ii in i]),np.array(term_t).shape[0]*np.array(inter_tg[topic]).shape[0])



  yield [query_u_bing_jd,query_u_twitter_jd,query_u_inter_jd,query_u_bing_dd,query_u_twitter_dd,query_u_inter_dd,\
          query_u_bing_pjd,query_u_twitter_pjd,query_u_inter_pjd,query_u_bing_pdd,query_u_twitter_pdd,query_u_inter_pdd,\
          query_b_bing_jd,query_b_twitter_jd,query_b_inter_jd,query_b_bing_dd,query_b_twitter_dd,query_b_inter_dd]