from sklearn.externals import joblib
import sys
sys.path.append('../')

bing_bg=joblib.load('../data/model/bing_bg.model')
bing_ug=joblib.load('../data/model/bing_ug.model')
bing_tg=joblib.load('../data/model/bing_tg.model')
##################################################
twitter_bg=joblib.load('../data/model/twitter_bg.model')
twitter_ug=joblib.load('../data/model/twitter_ug.model')
twitter_tg=joblib.load('../data/model/twitter_tg.model')
##################################################
inter_bg=joblib.load('../data/model/inter_bg.model')
inter_ug=joblib.load('../data/model/inter_ug.model')
inter_tg=joblib.load('../data/model/inter_tg.model')
##################################################
bingtop=joblib.load('../data/model/bingtop.model')
twittertop=joblib.load('../data/model/twittertop.model')
intertop=joblib.load('../data/model/intertop.model')
#####################################################
"""this is all dict"""
count_vect=joblib.load('../data/model/count_vect.model')
tfidf_transform=joblib.load('../data/model/tfidf_transform.model')
svd_transform=joblib.load('../data/model/svd_transform.model')
#############
bing_all_tfidf=joblib.load('../data/model/bing_all_tfidf.model')
bing_all_svd=joblib.load('../data/model/bing_all_svd.model')
twitter_all_tfidf=joblib.load('../data/model/twitter_all_tfidf.model')
twitter_all_svd=joblib.load('../data/model/twitter_all_svd.model')
inter_all_tfidf=joblib.load('../data/model/inter_all_tfidf.model')
inter_all_svd=joblib.load('../data/model/inter_all_svd.model')
######################################################
"""this is solo bing"""

count_vect_solo_bing=joblib.load('../data/model/count_vect_solo_bing.model')
tfidf_transform_solo_bing=joblib.load('../data/model/tfidf_transform_solo_bing.model')
svd_transform_solo_bing=joblib.load('../data/model/svd_transform_solo_bing.model')
bing_solo_tfidf=joblib.load('../data/model/bing_solo_tfidf.model')
bing_solo_svd=joblib.load('../data/model/bing_solo_svd.model')
#######################################################
"""this is solo twitter"""

count_vect_solo_twitter=joblib.load('../data/model/count_vect_solo_twitter.model')
tfidf_transform_solo_twitter=joblib.load('../data/model/tfidf_transform_solo_twitter.model')
svd_transform_solo_twitter=joblib.load('../data/model/svd_transform_solo_twitter.model')
twitter_solo_tfidf=joblib.load('../data/model/twitter_solo_tfidf.model')
twitter_solo_svd=joblib.load('../data/model/twitter_solo_svd.model')
#######################################################
"""this is solo inter"""

count_vect_solo_inter=joblib.load('../data/model/count_vect_solo_inter.model')
tfidf_transform_solo_inter=joblib.load('../data/model/tfidf_transform_solo_inter.model')
svd_transform_solo_inter=joblib.load('../data/model/svd_transform_solo_inter.model')
inter_solo_tfidf=joblib.load('../data/model/inter_solo_tfidf.model')
inter_solo_svd=joblib.load('../data/model/inter_solo_svd.model')

allwords=joblib.load('../data/model/allwords.model')
###########################################################
firstmodel=joblib.load('../data/online/first.model')
minmax=joblib.load('../data/online/minmax.model')
secondmodel=joblib.load('../data/online/second.model')

###########################################################
twitter_bg_hash=joblib.load('../data/model/twitter_bg_hash.model')
bing_bg_hash=joblib.load('../data/model/bing_bg_hash.model')
inter_bg_hash=joblib.load('../data/model/inter_bg_hash.model')
#####################################################
porn=joblib.load('../data/model/porn.model')











