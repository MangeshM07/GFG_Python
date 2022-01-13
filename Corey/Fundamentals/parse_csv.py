import csv

with open("usdata.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile)

    with open("new_usdata.csv", "w") as new_file:
        csv_writer = csv.writer(new_file, delimiter="\t")

        for line in csv_reader:
            csv_writer.writerow(line)

# More better way to read csv data using DictReader
with open("usdata.csv","r") as csv_file:
    csv_dictReader = csv.DictReader(csv_file)

    with open("new_file.csv","w") as new_file:
        fieldNames = ["first_name","last_name","company_name","address","city","county","state","zip","age","phone1","phone2","email","web"]
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldNames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_dictReader:
            csv_writer.writerow(line)