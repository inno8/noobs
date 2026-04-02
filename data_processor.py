# Data processing utilities
import csv

def load_csv(filename):
    f = open(filename, "r")
    reader = csv.reader(f)
    data = []
    for row in reader:
        data.append(row)
    f.close()
    return data

def filter_data(data, column, value):
    results = []
    for row in data:
        if row[column] == value:
            results.append(row)
    return results

def sort_data(data, column):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[j][column] < data[i][column]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    return data

def calculate_stats(data, column):
    values = []
    for row in data:
        try:
            values.append(float(row[column]))
        except:
            pass
    
    if len(values) == 0:
        return None
    
    total = 0
    for v in values:
        total += v
    avg = total / len(values)
    
    max_val = values[0]
    min_val = values[0]
    for v in values:
        if v > max_val: max_val = v
        if v < min_val: min_val = v
    
    return {"average": avg, "max": max_val, "min": min_val, "count": len(values)}

def export_csv(data, filename):
    f = open(filename, "w")
    for row in data:
        line = ""
        for i in range(len(row)):
            line += str(row[i])
            if i < len(row) - 1:
                line += ","
        line += "\n"
        f.write(line)
    f.close()
