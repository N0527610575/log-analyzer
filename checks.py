from reader import reader_log

def check_ip(file_ips,):
    sensitiv_ips = ["23","22","3389"]

    safe_row = filter(lambda row: row[3] not in sensitiv_ips, file_ips)
    sensitiv_row =  [row for row in file_ips if row[3] not in sensitiv_ips]

    return list(safe_row)