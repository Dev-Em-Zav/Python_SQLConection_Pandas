import csv

def importDataPython(filename):

    with open( filename, "r", newline='') as f: 
        reader = csv.reader(f, delimiter=",")
        next(reader) # Eliminar cabecera
        res = []
        for line in reader:
            res.append((line))
    
    return res


