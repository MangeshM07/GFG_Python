import csv

html_output=''
names=[]

with open("usdata.csv", "r") as file:
    data = csv.reader(file)

    # This will skip the header line
    next(data)

    for line in data:
        if line[0]=='' or line[1]=='':
            continue
        names.append(f"{line[0]} {line[1]}")

html_output += f'<p>There are currently {len(names)} entries</p>'
html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

with open('outfile.html','w') as out:
    data = csv.writer(out)

    for line in html_output:
        data.writerow(line)

# print(html_output)

