#Class of input deck

class Input:
    def __init__(self,
                 gmail_login='',
                 gmail_passkey='',
                 list_of_emails='',
                 test_flag = False,
                 reveal_names = False,
                 send_emails = False,
                 budget_lower = 0.0,
                 budget_upper = 0.0,
                 dist_date=''
                 ):
        
        self.gmail_login = gmail_login
        self.gmail_passkey = gmail_passkey
        self.list_of_emails = list_of_emails
        self.test_flag = test_flag
        self.reveal_names = reveal_names
        self.send_emails = send_emails
        self.budget_lower = budget_lower
        self.budget_upper = budget_upper
        self.dist_date = dist_date
       