from reader import reader_log

def safe_port(log_file):
    sensitiv_ips = ["23","22","3389"]

    safe_row = filter(lambda row: row[3] not in sensitiv_ips, log_file)

    return list(safe_row)

def tag_sizes(log_file):
    size_tags = map(lambda row: ("NORMAL" if int(row[5]) <= 5000 else "LARGE", row), log_file)
    return list(size_tags)
