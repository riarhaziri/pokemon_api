import csv 
# from app import Pokemon

def csv_to_list(path, Pokemon):
    with open(path) as pokemon_csv:
        next(pokemon_csv)
        data = csv.reader(pokemon_csv, delimiter=',')
        result = []
        row_values = []
        for row in data:
            for i in range(len(row)):
                row_values.append(row[i])
            if row_values[12] == "True":
                row_values[12] = True
            elif row_values[12] == "False":
                row_values[12] = False
            pokemon = Pokemon(row_values[1],row_values[2],row_values[3],row_values[4],row_values[5],
                    row_values[6],row_values[7],row_values[8],row_values[9],row_values[10],
                    row_values[11],row_values[12])
            result.append(pokemon)
            row_values = []
        return result



# print(csv_to_list('pokemon.csv',Pokemon))