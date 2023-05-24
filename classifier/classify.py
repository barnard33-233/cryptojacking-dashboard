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

df1 = pd.read_csv('malicious/WebOS_binary.csv')  #
df2 = pd.read_csv('malicious/Server_Binary.csv')  #
df3 = pd.read_csv('malicious/Raspberry_Webmine_Robust.csv')
df4 = pd.read_csv('malicious/Raspberry_Binary.csv')  #
df5 = pd.read_csv('malicious/Raspberry_Webmine_Aggressive.csv')
df6 = pd.read_csv('malicious/Raspberry_WebminePool_Aggressive.csv')
df7 = pd.read_csv('malicious/Server_WebminePool_Aggressive.csv')  #

# df32 = pd.read_csv('malicious/Server_WebminePool_Robust.csv')  #
# df33 = pd.read_csv('malicious/Raspberry_WebminePool_Stealthy.csv')  #
# df34 = pd.read_csv('malicious/Raspberry_WebminePool_Robust.csv')  #
# df35 = pd.read_csv('malicious/Desktop_WebminePool_Aggressive.csv')  #

#################################################################
#                                                               #
#       过滤掉恶意数据集中的干扰数据，需要参照上面的恶意数据集            #
#                                                               #
#################################################################

# For WebOS = 18:56:80:17:d0:ef
index_names = df1[((df1['HW_dst'] != '18:56:80:17:d0:ef') & (df1['Hw_src'] != '18:56:80:17:d0:ef'))].index
df1.drop(index_names, inplace=True)

# Big_Server_Monero_mining_data = a4:bb:6d:ac:e1:fd
index_names = df2[((df2['HW_dst'] != 'a4:bb:6d:ac:e1:fd') & (df2['Hw_src'] != 'a4:bb:6d:ac:e1:fd'))].index
df2.drop(index_names, inplace=True)

# ege_data_rasberry = dc:a6:32:67:66:4b
index_names = df3[((df3['HW_dst'] != 'dc:a6:32:67:66:4b') & (df3['Hw_src'] != 'dc:a6:32:67:66:4b'))].index
df3.drop(index_names, inplace=True)

# Rasberry_binary_monero_mining = dc:a6:32:68:35:8a
index_names = df4[((df4['HW_dst'] != 'dc:a6:32:68:35:8a') & (df4['Hw_src'] != 'dc:a6:32:68:35:8a'))].index
df4.drop(index_names, inplace=True)

# Rasberry_network_data_2 = dc:a6:32:67:66:4b
index_names = df5[((df5['HW_dst'] != 'dc:a6:32:67:66:4b') & (df5['Hw_src'] != 'dc:a6:32:67:66:4b'))].index
df5.drop(index_names, inplace=True)

# Rasberry-Webmine = dc:a6:32:67:66:4b
index_names = df6[((df6['HW_dst'] != 'dc:a6:32:67:66:4b') & (df6['Hw_src'] != 'dc:a6:32:67:66:4b'))].index
df6.drop(index_names, inplace=True)

# Server_Webmine_Network_data = a4:bb:6d:ac:e1:fd
index_names = df7[((df7['HW_dst'] != 'a4:bb:6d:ac:e1:fd') & (df7['Hw_src'] != 'a4:bb:6d:ac:e1:fd'))].index
df7.drop(index_names, inplace=True)
"""
# Server_%50_Mining = a4:bb:6d:ac:e1:fd
index_names = df32[((df32['HW_dst'] != 'a4:bb:6d:ac:e1:fd') & (df32['Hw_src'] != 'a4:bb:6d:ac:e1:fd'))].index
df32.drop(index_names, inplace=True)

# Rasberry_webmine_%10 = dc:a6:32:67:66:4b
index_names = df33[((df33['HW_dst'] != 'dc:a6:32:67:66:4b') & (df33['Hw_src'] != 'dc:a6:32:67:66:4b'))].index
df33.drop(index_names, inplace=True)

# Rasberry_webmine_%50 = dc:a6:32:68:35:8a
index_names = df34[((df34['HW_dst'] != 'dc:a6:32:68:35:8a') & (df34['Hw_src'] != 'dc:a6:32:68:35:8a'))].index
df34.drop(index_names, inplace=True)

# Desktop_Webmine_%100 = dc:a6:32:68:35:8a
index_names = df35[((df35['HW_dst'] != 'd8:3b:bf:8f:ba:ba') & (df35['Hw_src'] != 'd8:3b:bf:8f:ba:ba'))].index
df35.drop(index_names, inplace=True)
"""
#################################################################
#                                                               #
#               导入非恶意数据集，不需要过滤                         #
#                                                               #
#################################################################

df8 = pd.read_csv('benign-1/interactive_01.csv')  #
df9 = pd.read_csv('benign-1/interactive_02.csv')  #
df10 = pd.read_csv('benign-1/interactive_03.csv')  #
df11 = pd.read_csv('benign-1/interactive_04.csv')  #
df12 = pd.read_csv('benign-1/interactive_05.csv')  #
df13 = pd.read_csv('benign-1/interactive_06.csv')  #

#################################################################
#                                                               #
#                   给数据集添加标签                               #
#                                                               #
#################################################################

df1.insert(7, "Is_malicious", 1)
df2.insert(7, "Is_malicious", 1)
df3.insert(7, "Is_malicious", 1)
df4.insert(7, "Is_malicious", 1)
df5.insert(7, "Is_malicious", 1)
df6.insert(7, "Is_malicious", 1)
df7.insert(7, "Is_malicious", 1)
"""
df32.insert(7, "Is_malicious", 1)
df33.insert(7, "Is_malicious", 1)
df34.insert(7, "Is_malicious", 1)
df35.insert(7, "Is_malicious", 1)
"""
df8.insert(7, "Is_malicious", 0)
df9.insert(7, "Is_malicious", 0)
df10.insert(7, "Is_malicious", 0)
df11.insert(7, "Is_malicious", 0)
df12.insert(7, "Is_malicious", 0)
df13.insert(7, "Is_malicious", 0)

# 加载模型
model = joblib.load('model.pkl')


def main(a):
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
    group_num = 1
    for i in Y:
        if i == 1:
            print(group_num, "malignant")
        else:
            print(group_num, "benign")
        group_num = group_num + 1

    # 对模型进行测试
    # target_names = ['benign', 'malignant']
    # print(classification_report(y, Y, target_names=target_names))
    print("accuracy:" + str(sum(Y)/len(Y)))

    return Y


if __name__ == '__main__':
    #df_all = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13])
    df_all = pd.concat([df6])
    print("All: {}".format(len(df_all)))
    #去除无效数据
    print("{} NAN in All".format(len(df_all[df_all.isna().any(axis=1)])))
    df_malicious = df_all.dropna()

    print("After droppping NAN rows: ")
    print("ALL: {}".format(len(df_malicious)))

    classification = main(df_malicious)