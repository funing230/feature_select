from math import log
import pandas as pd

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    print("样本总数：" + str(numEntries))

    labelCounts = {}  # 记录每一类标签的数量

    # 定义特征向量featVec
    for featVec in dataSet:

        currentLabel = featVec[-1]  # 最后一列是类别标签

        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0;

        labelCounts[currentLabel] += 1  # 标签currentLabel出现的次数
        print("当前labelCounts状态：" + str(labelCounts))

    shannonEnt = 0.0

    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries  # 每一个类别标签出现的概率

        print(str(key) + "类别的概率：" + str(prob))
        print(prob * log(prob, 2))
        shannonEnt -= prob * log(prob, 2)
        print("熵值：" + str(shannonEnt))

    return shannonEnt


def createDataSet():
    dataSet = [
        [1, 1, 'yes'],
        [1, 0, 'yes'],
        [1, 1, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no'],
        # #以下随意添加，用于测试熵的变化，越混乱越冲突，熵越大
        [1, 1, 'no'],
        [1, 1, 'no'],
        [1, 1, 'no'],
        [1, 1, 'no'],
        [1, 1, 'maybe'],
        [1, 1, 'maybe1']
        # 用下面的8个比较极端的例子看得会更清楚。如果按照这个规则继续增加下去，熵会继续增大。
        # [1,1,'1'],
        # [1,1,'2'],
        # [1,1,'3'],
        # [1,1,'4'],
        # [1,1,'5'],
        # [1,1,'6'],
        # [1,1,'7'],
        # [1,1,'8'],

        # 这是另一个极端的例子，所有样本的类别是一样的，有序，不混乱，此时熵为0
        # [1, 1, '1'],
        # [1, 1, '1'],
        # [1, 1, '1'],
        # [1, 1, '1'],
        # [1, 1, '1'],
        # [1, 1, '1'],
        # [1, 1, '1'],
        # [1, 1, '1'],
    ]

    labels = ['no surfacing', 'flippers']

    return dataSet, labels


def testCalcShannonEnt():
    metrics = pd.read_csv('dataset/' + 'commit_metrics_5_s' + '.csv')
    metrics_fillnan=metrics.fillna(0)

    metrics_drop=metrics_fillnan.drop(labels=['file','class','type'],axis=1)

    # dataSet=metrics_fillnan.drop(labels=0)
    dataSet = metrics_drop.values.tolist()
    features=metrics_drop.columns.tolist()

    # myDat, labels = createDataSet()

    print(calcShannonEnt(dataSet))


if __name__ == '__main__':
    testCalcShannonEnt()
    # print(log(0.000002, 2))