class Accounts:
    def_init_(self,first_name,last_name, user_name, password)
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
    user_accounts = []
    
    def save_accounts(self):
        '''
        this is a save function that appends the account to the user_accounts
        '''
        Accounts.user_accounts.append(self)
        
    def save_contact(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

    Contact.contact_list.append(self)
    
    def delete_contact(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Accounts.user_accounts.remove(self)
        
        
        