import pandas as pd

def gera_ds(arg1, arg2):
    dataset_original = pd.read_csv(arg1)
    dataset_original = dataset_original.drop_duplicates()
    sub_dataset = dataset_original.sample(n=arg2)
    resto_dataset = dataset_original.drop(sub_dataset.index)
    sub_dataset = sub_dataset.sort_values(by='1')
    sub_dataset.to_csv('random_ransomwares'+str(sub_dataset.shape[0])+'X'+str(sub_dataset.shape[1])+'.csv', index=False)
    resto_dataset = resto_dataset.sort_values(by='1')
    resto_dataset.to_csv('random_ransomwares' + str(resto_dataset.shape[0]) + 'X' + str(resto_dataset.shape[1]) + '.csv', index=False)
    #print(f'Datset1:\n{sub_dataset}')
    #print(f'Datset2:\n{resto_dataset}')

if __name__ == '__main__':
    gera_ds('/home/rui/Área de Trabalho/projeto/dataset/vt_99_RF_0.0025_ransomwares.csv', 208)