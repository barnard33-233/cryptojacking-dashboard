import pandas as pd
import tsfresh
import numpy as np
from scapy.all import *
from tsfresh.utilities.dataframe_functions import impute
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
import joblib

warnings.filterwarnings("ignore")

#################################################################
#                                                               #
#                         导入恶意数据集                           #
#                                                               #
#################################################################

df1 = pd.read_csv('test.csv')
# test.csv数据集提前填充了100条数据，最后加入3组数据来自3个mac地址的，分别是无害、恶意和无害，因此预期结果为0、1、0

#################################################################
#                                                               #
#                   给数据集添加标签                               #
#                                                               #
#################################################################
df1.insert(7, "Is_malicious", 1)

# 加载模型
model = joblib.load('model.pkl')


def classifier(a):
    df = a.copy()

    # 对数据以10个为一组进行分组
    df.reset_index(drop=True, inplace=True)  # reset index
    df['id'] = np.floor(df.index.array / 10)

    # 提取所有数据的特征
    tf = tsfresh.extract_features(df, impute_function=impute, column_kind='Is_malicious',
                                  column_id='id', column_sort="Time", column_value="Length")

    # 给class赋值占个位，在预测的时候需要去掉class
    tf['class'] = 1
    # 读取best_features.txt中的重要特征
    get_bestFeature = pd.DataFrame()
    best_features = []
    with open("best_features.txt", "r") as f:  # 打开文件
        for line in f.readlines():
            feature, typ, p_value, relevant = map(str, line.strip().split('\t'))
            best_features.append(feature)

    # 根据读取到的重要特征，从提取的所有特征中抽取
    for feature in best_features:
        get_bestFeature[feature] = tf[feature]

    # 去掉class
    X = get_bestFeature.drop('class', axis=1).to_numpy()
    y = get_bestFeature['class'].to_numpy()

    # 编码
    Le = LabelEncoder()
    for i in range(len(X[0])):
        X[:, i] = Le.fit_transform(X[:, i])

    # 进行分类，得到Y。Y中的数据为0或1，其中1说明该组数据被认为是恶意的
    Y = model.predict(X)

    # 输出最后3组的分类结果，分别来自3个mac
    i = len(Y)
    print('18:56:80:17:d0:ef', '192.168.0.19', Y[i-3])
    print('a4:bb:6d:ac:e1:fd', '192.168.1.139', Y[i-2])
    print('dc:a6:32:67:66:4b', '192.168.1.120', Y[i-1])


if __name__ == '__main__':
    df_all = pd.concat([df1])
    # print("All: {}".format(len(df_all)))
    # #去除无效数据
    # print("{} NAN in All".format(len(df_all[df_all.isna().any(axis=1)])))
    df_all = df_all.dropna()

    # print("After droppping NAN rows: ")
    # print("ALL: {}".format(len(df_malicious)))
    # classification1 = classify(df_all)
