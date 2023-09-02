import csv

# Create an empty list to store HTML file names
html_files = []

# Open the CSV file
with open('biostats.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Loop through each row in the CSV file
    for row in csv_reader:
        # Create a new HTML file for each row
        html_filename = f'{row["Name"]}.html'
        html_files.append(html_filename)

        with open(html_filename, mode='w') as html_file:
            # Write the HTML template with data from the current row
            html_file.write(f'''<!DOCTYPE html>
<html>
<head>
    <title>Employee Details</title>
</head>
<body>
    <h1>Employee Details</h1>
    <ul>
        <li><strong>Name:</strong> {row["Name"]}</li>
        <li><strong>Age:</strong> {row["Age"]}</li>
        <li><strong>Gender:</strong> {row["Gender"]}</li>
    </ul>
</body>
</html>''')

# Create the master HTML directory file
with open('directory.html', mode='w') as directory_file:
    directory_file.write('<!DOCTYPE html>\n<html>\n<head>\n    <title>Employee Directory</title>\n</head>\n<body>\n    <h1>Employee Directory</h1>\n    <ul>\n')

    # Add links to individual HTML files in the directory
    for html_file in html_files:
        directory_file.write(f'        <li><a href="{html_file}">{html_file}</a></li>\n')

    directory_file.write('    </ul>\n</body>\n</html>')
