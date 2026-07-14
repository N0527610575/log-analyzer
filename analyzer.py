def count_gets_for_ip(log_data):
    ip_gets = {}

    for row in log_data:
        ip = row[1]
        if ip in ip_gets:
            ip_gets[ip] += 1

        else:
            ip_gets[ip] = 1
    return ip_gets


def dict_port(log_data):
    port_protocol = {}
    for row in log_data:
        port_protocol[row[3]] = row[4]

    return port_protocol



