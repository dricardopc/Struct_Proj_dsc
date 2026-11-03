import pandas as pd
import numpy as np

def validar_numerico(df,list_cols):
    df_final = pd.DataFrame()
    for col in list_cols:
        if df[col].dtype == 'int64' or df[col].dtype == 'float64':
            #print(col)
            #Calculo de columnas
            n = df.shape[0]
            missing = df[col].isnull().sum()
            missing_percent = df[col].isnull().sum()/n
            negativo = df[df[col]<0][col].count()
            negativo_percent =negativo/n
            unico = df[col].nunique()
            media = df[col].mean()
            std = df[col].std()
            minimo = df[col].min()
            maximo = df[col].max()
            LI = df[col].mean() - 1.96(np.std(df[col])/np.sqrt(df.shape[0]))
            LS = df[col].mean() + 1.96(np.std(df[col])/np.sqrt(df.shape[0]))
            Q1 = df[col].quantile(.25)
            Q3 = df[col].quantile(.75)
            IQR = Q3 - Q1
            min_bp = Q1 - 1.5 * IQR
            max_bp = Q3 + 1.5 * IQR
            P1 = df[col].quantile(.01)
            P5 = df[col].quantile(.05)
            P10 = df[col].quantile(.1)
            P25 = df[col].quantile(.25)
            P50 = df[col].quantile(.5)
            P75 = df[col].quantile(.75)
            P90 = df[col].quantile(.9)
            P95 = df[col].quantile(.95)
            P99 = df[col].quantile(.99)
            OUT_IQR = np.where((df[col]< min_bp) | (df[col]> max_bp),1,0).sum()
            OUT_IQR_percent = OUT_IQR/n
            OUT_P1 = np.where((df[col]< P1),1,0).sum()
            OUT_P1_percent = OUT_P1/n
            OUT_P5 = np.where((df[col]< P5),1,0).sum()
            OUT_P5_percent = OUT_P5/n
            OUT_P90 = np.where((df[col]> P90),1,0).sum()
            OUT_P90_percent = OUT_P90/n
            OUT_P95 = np.where((df[col]> P95),1,0).sum()
            OUT_P95_percent = OUT_P95/n
            OUT_P99 = np.where((df[col]> P99),1,0).sum()
            OUT_P99_percent = OUT_P99/n
            valores = [[col,n,missing,missing_percent,negativo,negativo_percent,unico,
            media,minimo,maximo,LI,LS,P1,P5,P10,P25,P50,P75,P90,P95,P99,min_bp,max_bp,
            OUT_IQR,OUT_IQR_percent,OUT_P1,OUT_P1_percent,OUT_P5,OUT_P5_percent,
            OUT_P90,OUT_P90_percent,OUT_P95,OUT_P95_percent,OUT_P99,OUT_P99_percent]]
            nombres = ["Variable","n","Missing","%Missing","Negativo","%Negativo","Unico",
            "Media","Min","Max","LI","LS","P1","P5","P10","P25","P50","P75","P90","P95","P99","min_bp","max_bp",
            "Outlier IQR","%Outlier IQR","Outlier P1","%Outlier P1","Outlier P5","%Outlier P5",
            "Outlier P90","%Outlier P90","Outlier P95","%Outlier P95","Outlier P99","%Outlier P99"]
            tabla = pd.DataFrame(valores,columns=nombres)
            df_final = pd.concat([df_final,tabla], axis = 0)

    df_final = df_final.round(decimals = 6)
    return df_final

def print_limit_quart(dftab2_wt,varx):
    Q1=dftab2_wt[varx].quantile(0.25)
    Q3=dftab2_wt[varx].quantile(0.75)
    Q01=dftab2_wt[varx].quantile(0.01)
    Q99=dftab2_wt[varx].quantile(0.99)
    IQR=Q3-Q1
    LS=Q3+1.5*IQR
    LI=Q3-1.5*IQR
    print("Q1: ",Q1)
    print("Q3: ",Q3)
    print("LS: ",LS)
    print("LI: ",LI)
    print("Q01: ",Q01)
    print("Q99: ",Q99)