import pickle as pkl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

index = ['00', '02', '05', '10', '20']
path = r"C:\Users\lzl_z\Desktop\联邦实验\联邦实验论文版\实验三测试集.xlsx"
writer = pd.ExcelWriter(path)
for i in index:
    with open(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_three\citeseer-results\testing\_' + i + '_1.pkl', 'rb') as f1:
        df1 = pkl.load(f1)
    f1.close()
    with open(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_three\citeseer-results\testing\_' + i + '_2.pkl', 'rb') as f2:
        df2 = pkl.load(f2)
    f2.close()
    with open(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_three\citeseer-results\testing\_' + i + '_3.pkl', 'rb') as f3:
        df3 = pkl.load(f3)
    f3.close()
    with open(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_three\citeseer-results\testing\_' + i + '_4.pkl', 'rb') as f4:
        df4 = pkl.load(f4)
    f4.close()
    with open(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_three\citeseer-results\testing\_' + i + '_5.pkl', 'rb') as f5:
        df5 = pkl.load(f5)
    f5.close()

    df = (df1 + df2 + df3 + df4 + df5) / 5
    df.to_excel(excel_writer=writer, sheet_name=i+'%loss')

writer.save()



