# main.py
from reader import reader_log
from checks import  check_ip
def main():
    log_data = reader_log("network_traffic.log")

    for row in log_data[:9]:
        print(row)

if __name__ == "__main__":
    main()