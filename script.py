import pandas as pd
import os

diretorio = "Dia 3 - 30 10\\"

arquivos_csv = []
nomes = []

todosArquivos = os.listdir(diretorio)
for arq_csv in todosArquivos:
    if arq_csv.endswith(".csv"):
        arquivos_csv.append(os.path.join(diretorio,arq_csv))
        nomes.append(arq_csv)
i=0

for arquivo in arquivos_csv:
            
    df = pd.read_csv(arquivos_csv[0],sep=",",skiprows=1)


    titles = ["Times","SoundPressure1","OffsetPressure1","SoundPressure2","OffsetPressure2"]

    df[titles[0]] = df.iloc[:,0].astype(int).astype(str) + "." + df.iloc[:,1].astype(int).astype(str).str.zfill(4)
    df[titles[1]] = df.iloc[:,2].astype(int).astype(str) + "." + df.iloc[:,3].astype(int).astype(str).str.zfill(3)
    df[titles[2]] = df.iloc[:,4].astype(int).astype(str) + "." + df.iloc[:,5].astype(int).astype(str).str.zfill(3)
    df[titles[3]] = df.iloc[:,6].astype(int).astype(str) + "." + df.iloc[:,7].astype(int).astype(str).str.zfill(3)
    df[titles[4]] = df.iloc[:,8].astype(int).astype(str) + "." + df.iloc[:,9].astype(int).astype(str).str.zfill(3)

    newDf = df[titles]
    newDf_path = f"Modificados\\Dia 3\\"
    newDf.to_csv(f"{newDf_path}Modified_{nomes[i]}",index=False) #, header=False)
    i+=1
            


