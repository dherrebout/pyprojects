from datetime import datetime as dt
import time

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
# List of websites to be blocked within working hours
website_list = ['www.facebook.com', 'facebook.com']

# Infinite loop
while True:
    # If time is between 9AM and 17PM
    if (dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() <
            dt(dt.now().year, dt.now().month, dt.now().day, 17)):
        print('Working hours')

        # Read hosts file
        with open(hosts_path, 'r') as file:
            content = file.read()
            print(content)

            # Check if to be blocked websites are already in hosts
            for website in website_list:
                # If already there, do nothing
                if website in content:
                    pass
                # If not there, write blocking lines in hosts file
                else:
                    file.write(redirect + '\t' + website + '\n')

    # If time is before 9AM or after 17PM
    else:
        print('Fun hours')

        # Read hosts file
        with open(hosts_path, 'r') as file:
            content = file.readlines()

        # Read all lines in hosts
        for line in content:
            # If item is not in hosts, append it
            if not any(website in line for website in website_list):
                file.write(line)

    # End of while loop: sleep for 60 seconds
    time.sleep(60)
