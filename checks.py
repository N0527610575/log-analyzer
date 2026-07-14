from reader import reader_log


def analyze_logs_to_dict(log_data):
    dict_log = {}

    sensitiv = ["23", "22", "3389"]

    for row in log_data:
        ip = row[1]
        port = row[3]
        size = int(row[5])
        time = int(row[0][13:14])


        list_tags = []

        if row[1][:7] != "192.168" and  row[1][:3] != "10.":
            list_tags.append("EXTERNAL_IP")


        if ip in sensitiv:
            list_tags.append("SENSITIVE ")

        if size > 5000:
            list_tags.append("LARGE_PACKET")

        if 0 < time < 6:
            list_tags.append("NIGHT_ACTIVITY")



        if ip not  in dict_log:
            dict_log[ip] = list_tags

        else:
            for tag in list_tags:
                if tag not in dict_log[ip]:
                    dict_log[ip].append(tag)
