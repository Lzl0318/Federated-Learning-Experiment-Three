import pickle as pkl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

index = ['00', '02', '05', '10', '20']
path = r"C:\Users\lzl_z\Desktop\联邦实验\联邦实验论文版\新建 Microsoft Excel 工作表1.xlsx"
writer = pd.ExcelWriter(path)
for c, i in enumerate(index):
    with open(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_three\results\validation\_' + i + '_1.pkl', 'rb') as f1:
        dict1 = pkl.load(f1)
        df1 = pd.DataFrame({'accuracy': dict1.get('fed_val_acc')})
    f1.close()
    with open(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_three\results\validation\_' + i + '_2.pkl', 'rb') as f2:
        dict2 = pkl.load(f2)
        df2 = pd.DataFrame({'accuracy': dict2.get('fed_val_acc')})
    f2.close()
    with open(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_three\results\validation\_' + i + '_3.pkl', 'rb') as f3:
        dict3 = pkl.load(f3)
        df3 = pd.DataFrame({'accuracy': dict3.get('fed_val_acc')})
    f3.close()
    with open(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_three\results\validation\_' + i + '_4.pkl', 'rb') as f4:
        dict4 = pkl.load(f4)
        df4 = pd.DataFrame({'accuracy': dict4.get('fed_val_acc')})
    f4.close()
    with open(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_three\results\validation\_' + i + '_5.pkl', 'rb') as f5:
        dict5 = pkl.load(f5)
        df5 = pd.DataFrame({'accuracy': dict5.get('fed_val_acc')})
    f5.close()

    df = (df1 + df2 + df3 + df4 + df5) / 5
    df.to_excel(excel_writer=writer, sheet_name=str(c))

writer.save()



