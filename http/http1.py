import requests
import datetime

r = requests.get(input("Enter URL (ctrl+shift+v): "))
h = r.headers


def print_headers(headers):
    for key, value in headers.items():
        print(f"--- {key} ---")
        if ";" in value:
            s_value = value.split("; ")
            for s in s_value:
                print(s)
            print()
        else:
            print(value, end="\n\n")


def log_headers(headers):
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")
    logfile = f"headers_log_{dt}.txt"
    with open(logfile, "w", encoding="utf-8") as f:
        for key, value in headers.items():
            print(f"--- {key} ---", file=f)
            if ";" in value:
                s_value = value.split("; ")
                for s in s_value:
                    print(s, file=f)
                print(file=f)
            else:
                print(value, end="\n\n", file=f)


print_headers(h)
log_headers(h)
