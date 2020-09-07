from user_credential import User,Credentials

def create_user(username,password):
    new_user = User(username,password)
    return new_user


def sign_in(username,password):
    user_exists = Credentials.user_exist(username,password)
    return user_exists

def save_user(user):
    user.save_user()
    
     
def display_user():
    return User.display_user()


def create_credentials(account_name,username,password):
    new_credentials = Credentials(account_name,username,password)
    return new_credentials

def save_credentials(credentials):
    credentials.save_credentials()
    
def display_credentials():
    return credentials.display_credentials()

def delete_credentials(credentials):
    credentials.delete_credentials
    
def check_credentials(account_name):
    return Credentials.credentials_exist()

def find_credentials():
    return Credentials.find_account_name()

def generate_password():
    gen_pwrd = Credentials.generate_password()
    return gen_pwrd

def main():
    print('Welcome to Password Locker. Use the these commands to proceed: CA = create account, SI = sign in')
    short_code = input().lower()   
    if short_code == 'ca':
        print('Enter new account details')
        print('*' * 100)
        username = input('Enter Username: ')
        while True:
            print('use : GP = to auto generate password... or MP = to manually enter your own password')
            password_choice = input().lower()
            if password_choice == 'mp':
                password = input('Enter Password: ')
                break
            elif password_choice == 'gp':
                password = generate_password()
                break
            else:
                print('Invalid short code. Please try again')
                
            save_user(create_user(username, password))
                
        print('*' * 100)
        print(f'Welcome {username} to your new account your password is <--- {password} --->')
        print('*' * 100)
    
    elif short_code == 'si':
        print('Enter Account Username and Password to Login')
        username = input('Username: ')
        password = input('Password: ')
        check_user = sign_in(username,password)
        if sign_in == check_user:            
            print('\n')
            print(f'Welcome back {username}')
            print('\n')
            
    while True:
        print('Use these short codes to manage credentials: \n NC = new credential, \n VC = view credentials, \n FC find credential, \n GP = generate random password, \n Dc = delete credential, \n EX = exit application')
        short_code = input().lower()
        if short_code == 'nc':
            print('Enter New Credential Details')
            print('*' * 100)
            account_name = input('Account Name : ')
            username = input('Username : ')
            while True:
                print('Would you like to... GP = auto generate password, or MP = manually enter password?')
                password_choice = input().lower()
                if password_choice == 'mp':
                    password = input('Enter password : ')
                    break
                elif password_choice == 'gp':
                    password = generate_password()
                    break
                else:
                    print('Invalid short code. Please try again')
                print('*' * 100)
            save_credentials(create_credentials(account_name, username, password))
            print('\n')
            print(f'Your {account_name} account has been saved')
            print('\n')
            print('*' * 100)
            
        elif short_code == 'vc':
            if view_credentials():
                print('Your saved credentials are:')
                for account_name in view_credentials():
                    print(f' Name: {account_name} \n Username: {username} \n Password: {password}')
                    print('*' * 100)
            else:
                print('You have No Credentials. Please Create One')
                
        elif short_code == 'dc':
            print('Enter Account name to delete...')
            name = input('Acount Name : ').lower()
            if find_credentials(name):
                name_result = find_credentials(name)
                name_result.delete_credentials()
                print(f'Account {name} has been successfully deleted ')   
                

if __name__ == '__main__':
    main()
    
    
