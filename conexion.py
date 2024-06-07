import pyodbc

def conectSql(arrData, listData=True):

        data = arrData.copy()
        recors_total=[]


        connectionString = "DRIVER={ODBC Driver 18 for SQL Server};SERVER=(LocalDB)\MSSQLLocalDB;DATABASE=Northwind;"
        conn = pyodbc.connect(connectionString) 

        SQL_QUERY = """

        SELECT 
                [Country], 
                CompanyName, 
                ContactName
        FROM  Customers
        WHERE [Country] =  ?


        """ 

        for valor_parametro in data:
                # Ejecuta la consulta con el parámetro
                cursor = conn.cursor()
                cursor.execute(SQL_QUERY, valor_parametro)
                records = cursor.fetchall()                     # Te lo devuelve como una tupla
                recors_total = recors_total + records           # Concatena cada consulta

        conn.close()

        # AJUSTE DE TUPLAS A LISTA DE CADA ELEMENTO EXTRAIDO
        
        if listData:
                new_recors_total=[]
                
                for r in recors_total:
                        new_recors_total.append(list(r))
                        
                # for r in recors_total:
                #         print(f"{r.Country}\t\t{r.CompanyName}\t\t{r.ContactName}")
                return new_recors_total
        else:
                return recors_total

