


from reader import reader_log
from checks import safe_port
from checks import tag_sizes



def main():
    log_file = "network_traffic.log"
    log_data = reader_log(log_file)
    print(f"מספר השורות{len(log_file)}")

    print(f"מספר השורות עם פורטים חשודים{len(safe_port(log_data))}")

    tag_row = tag_sizes(log_data)

    tag_name = [(tag, row) for tag , row in tag_row]
    print(tag_name[:5])


if __name__ == "__main__":
    main()