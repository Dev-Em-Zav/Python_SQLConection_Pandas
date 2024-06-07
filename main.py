from conexion import conectSql
from CSV_import_DataPython import importDataPython 
from pandasDataFrame import (framePandasList,framePandasTupla)



if __name__ == "__main__":

   arrData = importDataPython( "data.csv")
   resultado = conectSql(arrData)

   dataFrame = framePandasList(resultado,True,True)
   print('\n\n')
   print(resultado)
