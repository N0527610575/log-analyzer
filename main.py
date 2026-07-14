


from reader import reader_log

from checks import analyze_logs_to_dict,safe_port,tag_sizes
from reporter import reporter






def main():
    log_file = "network_traffic.log"
    log_data = reader_log(log_file)
    print(f"מספר השורות{len(log_file)}")

    print(f"מספר השורות עם פורטים חשודים{len(safe_port(log_data))}")

    tag_row = tag_sizes(log_data)

    tag_name = [(tag, row) for tag , row in tag_row]
    print(tag_name[:3])

    # for k , v in analyze_logs_to_dict(log_data).items():
    #     if len(v) >= 2:
    #         print(k,v)
    print(len(analyze_logs_to_dict(log_data)))
    reporter(log_data,"report.txt",analyze_logs_to_dict(log_data))



if __name__ == "__main__":
    main()