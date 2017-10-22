from sklearn.externals import joblib
from sklearn import svm
from sklearn.linear_model import SGDClassifier
import sys
sys.path.append("../")
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import f1_score,accuracy_score,roc_auc_score


count_ff=joblib.load('../data/train/count_ff.model')
distance_ff=joblib.load('../data/train/distance_ff.model')
tfidf_ff=joblib.load('../data/train/tfidf_ff.model')
rel=joblib.load('../data/train/rel.model')

count_ff_test=joblib.load('../data/train/count_ff_test.model')
distance_ff_test=joblib.load('../data/train/distance_ff_test.model')
tfidf_ff_test=joblib.load('../data/train/tfidf_ff_test.model')
rel_test=joblib.load('../data/train/rel_test.model')

y=np.array(rel)
X=np.array([i+ii+iii for i,ii,iii in zip(count_ff,distance_ff,tfidf_ff)])
#y=[0 if i ==0 else 1 for i in y]

y_new=np.array(rel_test)
X_new=np.array([i+ii+iii for i,ii,iii in zip(count_ff_test,distance_ff_test,tfidf_ff_test)])

minmax=MinMaxScaler()
X=minmax.fit_transform(X)

X_new=minmax.transform(X_new)
joblib.dump(minmax,'../data/online/minmax.model')







wclf = svm.SVC(kernel='linear',class_weight={0:.3,1:2.7,2:5})
wclf.fit(X,y)
joblib.dump(wclf,'../data/online/second.model')
pre=wclf.predict(X_new)
print f1_score(y_new, pre, average=None)








