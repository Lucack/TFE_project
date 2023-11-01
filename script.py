import pandas as pd
import os

diretorio = "C:\\Users\\Lucas\\Desktop\\Script_Balao\\"

arquivos_csv = []
nomes = []

todosArquivos = os.listdir(diretorio)
for arq in todosArquivos:
    if arq.endswith(".csv"):
        arquivos_csv.append(os.path.join(diretorio,arq))
        nomes.append(arq)
i=0

for arquivo in arquivos_csv:
            
    df = pd.read_csv(arquivos_csv[0],sep=",",skiprows=1)


    titles = ["Times","SoundPressure1","OffsetPressure1","SoundPressure2","OffsetPressure2"]

    df[titles[0]] = df.iloc[:,0].astype(str) + "." + df.iloc[:,1].astype(str)
    df[titles[1]] = df.iloc[:,2].astype(str) + "." + df.iloc[:,3].astype(str)
    df[titles[2]] = df.iloc[:,4].astype(str) + "." + df.iloc[:,5].astype(str)
    df[titles[3]] = df.iloc[:,6].astype(str) + "." + df.iloc[:,7].astype(str)
    df[titles[4]] = df.iloc[:,8].astype(str) + "." + df.iloc[:,9].astype(str)

    newDf = df[titles]
    newDf_path = f"C:\\Users\\Lucas\\Desktop\\Script_Balao\\Modificados\\Dia 3\\"
    newDf.to_csv(f"{newDf_path}{nomes[i]}aaaaaaaaa.csv",index=False)
    i+=1
            


