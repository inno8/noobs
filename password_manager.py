# Password manager - stores passwords securely (NOT!)
passwords = {}

def add_password(site, username, password):
    passwords[site] = {"user": username, "pass": password}
    print("Saved password for " + site)

def get_password(site):
    if site in passwords:
        print("Username: " + passwords[site]["user"])
        print("Password: " + passwords[site]["pass"])
    else:
        print("No password found for " + site)

def delete_password(site):
    if site in passwords:
        del passwords[site]
        print("Deleted")
    else:
        print("Not found")

def list_sites():
    for site in passwords:
        print(site + " - " + passwords[site]["user"])

def save_to_file():
    f = open("passwords.txt", "w")
    for site in passwords:
        f.write(site + "," + passwords[site]["user"] + "," + passwords[site]["pass"] + "\n")
    f.close()

def load_from_file():
    global passwords
    f = open("passwords.txt", "r")
    for line in f.readlines():
        parts = line.strip().split(",")
        passwords[parts[0]] = {"user": parts[1], "pass": parts[2]}
    f.close()
