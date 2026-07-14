import csv

def reader_log(csv_file):
    with open(csv_file, "r", encoding="utf-8") as read_log:
        reader = csv.reader(read_log)

        next(reader)

        list_log = [row for row in reader]
        return list_log


# print(reader_log("network_traffic.log"))








