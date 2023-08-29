from datetime import datetime


def get_new_email_with_time_stamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "anil" + time_stamp + "@gmail.com"
