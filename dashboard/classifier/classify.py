import pandas as pd
import tsfresh
import numpy as np
from scapy.all import *
from tsfresh.utilities.dataframe_functions import impute
from sklearn.preprocessing import LabelEncoder
import joblib
import os

warnings.filterwarnings("ignore")
basedir = os.path.dirname(__file__) + '/'

# load model
model = joblib.load(basedir + 'model.pkl')


# """
#    提前定义字典，用于存储每个设备对应的mac、ip和分类结果，最开始分类结果都为0
#    便于初始化后端数据库，并且在实际抓包过程中可以使用其他扫描软件提前获取这部分设备数据
# """
# result = [
#     # TODO: abort this
#     {'mac': '18:56:80:17:d0:ef', 'data': {'ip': '192.168.0.19', 'safety': 0}},
#     {'mac': 'a4:bb:6d:ac:e1:fd', 'data': {'ip': '192.168.1.139', 'safety': 0}},
#     {'mac': 'dc:a6:32:67:66:4b', 'data': {'ip': '192.168.1.120', 'safety': 0}}
# ]

# def init():
#     # TODO: abort this
#     global model
#     # 导入测试数据集
#     df_test = pd.read_csv(basedir + 'test.csv')
#     # 加载模型
#     return df_test

#将test.csv中的网络流量按照mac地址进行分类
# def classify_by_mac(df):
#     device_data = {
#         '18:56:80:17:d0:ef': pd.DataFrame(),
#         'a4:bb:6d:ac:e1:fd': pd.DataFrame(),
#         'dc:a6:32:67:66:4b': pd.DataFrame()
#     }
#     #
#     for index, row in df.iterrows():
#         src_mac = row['Hw_src']
#         dst_mac = row['HW_dst']
#         if src_mac in device_data:
#             device_data[src_mac] = device_data[src_mac].append(row)
#         elif dst_mac in device_data:
#             device_data[dst_mac] = device_data[dst_mac].append(row)
#     # 测试mac分类结果
#     # for mac, data in device_data.items():
#     #     print("MAC Address:", mac)
#     #     print("Traffic Data:")
#     #     print(data)
#     #     print("-----------------------------------")

def classifier(device_data):
    # global result
    results = {}

    for mac, data in device_data.items():
        # take the place
        data.insert(7, "Is_malicious", 1)

        # 对数据以10个为一组进行分组
        data.reset_index(drop=True, inplace=True)  # reset index
        data['id'] = np.floor(data.index.array / 10) # TODO

        # 提取所有数据的特征
        tf = tsfresh.extract_features(data, impute_function=impute, column_kind='Is_malicious',
                                      column_id='id', column_sort="Time", column_value="Length")

        # 给safety赋值占个位，在预测的时候需要去掉safety
        tf['class'] = 1

        # 读取best_features.txt中的重要特征
        best_features = []
        with open(basedir + "best_features.txt", "r") as f:  # 打开文件
            for line in f.readlines():
                feature, typ, p_value, relevant = map(str, line.strip().split('\t'))
                best_features.append(feature)

        # 根据读取到的重要特征，从提取的所有特征中抽取
        get_bestFeature = tf[best_features].copy()

        # 去掉class
        X = get_bestFeature.drop('class', axis=1).to_numpy()

        # 编码
        Le = LabelEncoder()
        for i in range(len(X[0])):
            X[:, i] = Le.fit_transform(X[:, i])

        # 进行分类，得到predictions，predictions中的数据为0或1，其中1说明该组数据被认为是恶意的
        predictions = model.predict(X)

        prediction = sum(predictions)/len(predictions)
        safety = 1 if prediction > 0.5 else 0 # TODO: read thresh from config

        # 更新result中对应设备的安全性值
        # for item in result:
        #     if item['mac'] == mac:
        #         # 使用最后一个预测值作为分类结果
        #         item['data']['safety'] = predictions[-1]
        #         break

        # XXX: assume that mac and ip correspond one-to-one
        results[mac] = { 'ip':device_data[mac]['Source'][0], 'safety': safety}

    print(results)

    return results

if __name__ == '__main__':
    pass