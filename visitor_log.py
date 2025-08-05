import datetime

def log_visitor(user, action):
    with open("visitor_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {user}: {action}\n")
