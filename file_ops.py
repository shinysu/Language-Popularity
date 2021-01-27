import csv


def write_csv_from_dict(filename, fieldnames, data):
    with open(filename, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for project in data:
            writer.writerow(project)


def read_csv_from_dict(filename):
    urls = []
    with open(filename, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            urls.append(dict(row)['url'])
    return urls
