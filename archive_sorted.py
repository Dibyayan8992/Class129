import csv

data = []

with open('archive_dataset.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

headers = data[0]
planet_data = data[1:]

for row in planet_data:
    row[2] = row[2].lower()

planet_data.sort(key = lambda planet_data: planet_data[2])

with open('archive_dataset_sorted.csv', 'w', newline = "") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(planet_data)