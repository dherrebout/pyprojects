from datetime import datetime as dt
import time

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
# List of websites to be blocked within working hours
website_list = ['www.facebook.com', 'facebook.com']

while True:
    if (dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() <
            dt(dt.now().year, dt.now().month, dt.now().day, 17)):
        # If time is between 9AM and 17PM
        print('Working hours')

    else:
        # If time is before 9AM or after 17PM
        print('Fun hours')

    # End of while loop: sleep for 60 seconds
    time.sleep(60)
