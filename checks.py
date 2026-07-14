
def tag_sizes(log_file):
    size_tags = map(lambda row: ("NORMAL" if int(row[5]) <= 5000 else "LARGE", row), log_file)
    return list(size_tags)


def analyze_logs_to_dict(log_data):
    dict_log = {}

    sensitiv = ["23", "22", "3389"]

    for row in log_data:
        ip = row[1]
        port = row[3]
        size = int(row[5])
        time = int(row[0][12:13])


        list_tags = []

        if row[1][:7] != "192.168" and  row[1][:3] != "10.":
            list_tags.append("EXTERNAL_IP")


        if port in sensitiv:
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
    return dict_log


def safe_port(log_data):
    sensitiv = ["23", "22", "3389"]

    not_safe_ports =[row for row in log_data if row[3] in sensitiv]
    return not_safe_ports

def lists_tag(dict_log):
    dict_rows = {}
    for ip,tags in dict_log.items():
        for tag in tags:
            if tag in dict_rows:
                dict_rows[tag] += 1
            else:
                dict_rows[tag] = 1

    return dict_rows