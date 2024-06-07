
import pandas as pd

def framePandasList(dataSQL, printData=False, export=False, _index=False):
  
    df = pd.DataFrame(dataSQL,columns=[
                'Country', 
                'CompanyName', 
                'ContactName'
                ])
    if printData:
        print('\n\n')
        print(df)
        print('\n\n')
    
    if export :
        try:
            nombre_file= 'export.csv'
            df.to_csv(nombre_file, index=_index,encoding='utf-8-sig')
            print(f"DataFrame exportado a {nombre_file}")

        except:
            nombre_file= 'export_temp.csv'
            df.to_csv(nombre_file, index=_index,encoding='utf-8-sig')
            print(f"DataFrame exportado a {nombre_file}")
    
        return df 
    


def framePandasTupla(dataSQL, printData=False, export=False, _index=False):
  
    df = pd.DataFrame(dataSQL)
    if printData:
        print('\n\n')
        print(df)
        print('\n\n')

    if export :
        try:
            nombre_file= 'export.csv'
            df.to_csv(nombre_file, index=_index,encoding='utf-8-sig')
            print(f"DataFrame exportado a {nombre_file}")

        except:
            nombre_file= 'export_temp.csv'
            df.to_csv(nombre_file, index=_index,encoding='utf-8-sig')
            print(f"DataFrame exportado a {nombre_file}")
    
        return df 