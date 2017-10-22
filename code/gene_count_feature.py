from load_model import bing_bg,bing_ug,bing_tg,twitter_ug,twitter_bg,twitter_tg,inter_ug,inter_bg,inter_tg
from update import getBigram,getTrigram




def count_feat(term_u,term_b,term_t,topic):
  query_count=len(term_u)
  # b_count=len(term_b)
  # t_count=len(term_t)
  
  query_u_in_bing_count=sum([1 for x in term_u if x in bing_ug[topic]])
  query_u_in_twitter_count=sum([1 for x in term_u if x in twitter_ug[topic]])
  query_u_in_inter_count=sum([1 for x in term_u if x in inter_ug[topic]])

  query_b_in_bing_count=sum([1 for x in term_b if x in bing_bg[topic]])
  query_b_in_twitter_count=sum([1 for x in term_b if x in twitter_bg[topic]])
  query_b_in_inter_count=sum([1 for x in term_b if x in inter_bg[topic]])

  query_t_in_bing_count=sum([1 for x in term_t if x in bing_tg[topic]])
  query_t_in_twitter_count=sum([1 for x in term_t if x in twitter_tg[topic]])
  query_t_in_inter_count=sum([1 for x in term_t if x in inter_tg[topic]])

  yield [query_count,query_u_in_bing_count,query_u_in_twitter_count,query_u_in_inter_count,query_b_in_bing_count,\
         query_b_in_twitter_count,query_b_in_inter_count,query_t_in_bing_count,query_t_in_twitter_count,query_t_in_inter_count]








         