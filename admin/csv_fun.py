import csv
def write_to_csv(filename,data):
    with open(filename,'a') as csv_out:
        writer = csv.writer(csv_out)
        writer.writerow(data)
    
def print_from_csv(filename):
   courses = []
   with open(filename,'r') as csv_in:
        reader = csv.reader(csv_in)
        for row in reader:
            courses.append(row)
   return courses
