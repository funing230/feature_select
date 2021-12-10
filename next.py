
import numpy as np
import math
import pandas as pd

class IG():
    def __init__(self,X,y):

        X = np.array(X)
        n_feature = np.shape(X)[1]
        n_y = len(y)

        orig_H = 0
        for i in set(y):
            orig_H += -(y.count(i)/n_y)*math.log(y.count(i)/n_y)
            print("y is "+str(y.count(i)))

        condi_H_list = []
        for i in range(n_feature):
            feature = X[:,i]
            sourted_feature = sorted(feature)
            threshold = [(sourted_feature[inde-1]+sourted_feature[inde])/2 for inde in range(len(feature)) if inde != 0 ]

            if max(feature) in threshold:
                threshold.remove(max(feature))
            if min(feature) in threshold:
              threshold.remove(min(feature))

            pre_H = 0
            for thre in set(threshold):
                lower = [y[s] for s in range(len(feature)) if feature[s] < thre]
                highter = [y[s] for s in range(len(feature)) if feature[s] > thre]
                H_l = 0
                for l in set(lower):
                    H_l += -(lower.count(l) / len(lower))*math.log(lower.count(l) / len(lower))
                H_h = 0
                for h in set(highter):
                    H_h += -(highter.count(h) / len(highter))*math.log(highter.count(h) / len(highter))
                temp_condi_H = len(lower)/n_y *H_l+ len(highter)/n_y * H_h
                condi_H = orig_H - temp_condi_H
                pre_H = max(pre_H,condi_H)
            condi_H_list.append(pre_H)

        self.IG = condi_H_list


    def getIG(self):
        return self.IG
if __name__ == "__main__":

    metrics = pd.read_csv('dataset/' + 'commit_metrics' + '.csv')
    metrics_fillnan=metrics.fillna(0)

    metrics_drop=metrics_fillnan.drop(labels=['file','class','type'],axis=1)

    # dataSet=metrics_fillnan.drop(labels=0)
    dataSet = metrics_drop.values.tolist()
    features=metrics_drop.columns.tolist()



    # X =  [[1,0,0,1],
    #       [0,1,1,1],
    #       [0,0,1,0]]
    # y = [0,0,1]
    print(IG(dataSet,features).getIG())

    # print(IG(X,y).getIG())





