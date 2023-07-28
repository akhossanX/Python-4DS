
from datetime import datetime


def format_seconds(seconds):
    return f"{seconds:,.4f} or {seconds:.2e} in scientific notation"


def main():
    current_time = datetime.now()
    seconds_since_epoch = current_time.timestamp()
    formatted_time = current_time.strftime("%b %d %Y")

    print(f"Seconds since January 1, 1970: "
          f"{format_seconds(seconds_since_epoch)}")
    print(formatted_time)


if __name__ == "__main__":
    main()
