import glob, os

for file in glob.glob(f"battery/*.txt"):
    nome_arquivo = file.split(os.sep)[-1]
    print(f'Arquivo: {file} aberto')
    arquivo = f'batterys/obj_train_data/{nome_arquivo.replace("txt","jpg")}'
    os.rename(arquivo, f'battery_renovado/{nome_arquivo.replace("txt","jpg")}')
