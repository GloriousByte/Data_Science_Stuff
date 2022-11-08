import csv
lister = [1,2,3,4]
with open("contacts.txt","r") as a:
    object_csv = csv.reader(a)
    print(type(object_csv))
    print(object_csv)
    print(lister)
    for line in object_csv:
        print(line)

    """with open("newcontacts.txt","w") as new_a:
        csv_writer = csv.writer(new_a,delimiter='-')
        for line in object_csv:
            csv_writer.writerow(line)
    """
with open("contacts.txt","r") as b:
    dict_csv = list(csv.DictReader(b))
    print(type(dict_csv))
    print(dict_csv)