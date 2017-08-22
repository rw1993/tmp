# -*- coding: utf-8 -*-
import os

# 下载数据：https://www.kaggle.com/camnugent/sandp500
# 选择其中individual_stocks_5ye文件夹，设置为文件名
# 设定数据文件的文件名
# 我使用价格当天的变动情况作为时间序列
# 这样生成的文件每一行都对应一个时间序列
# 问题在于可能只有1000多，长度可能不够
# 个别文件会报错，运行后查看结果看结果文件是否有数据就可
# tushare那边华为这有权限问题，需要你自己研究了，之前我初步研究的结果是长度不够。

file_path = "/data/individual_stocks_5yr/{}"

names = os.listdir(file_path.format(""))

wf = open("/data1/FPN_TRAIN/tsresult", "w")

for name in names:
    with open(file_path.format(name), "r") as f:
        try:
            first_line = True
            timeseries = []
            print name
            for line in f.readlines():
                if first_line:
                    first_line = False
                    continue
                date, open_price, hight_price, low_price, close_price, v, n = line.strip().split(",")
                timeseries.append(float(close_price)-float(open_price))
            wf.write(",".join(map(str, timeseries))+"\n")
        except Exception, e:
            print e
wf.close()
