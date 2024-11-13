import pandas as pd 

def readin_from_excel(path):
    print("Reading in email list.")
    names_and_emails = pd.read_excel(path)
    names = names_and_emails["Names"]
    emails = names_and_emails["Emails"]
    num_names = len(names)
    num_emails = len(emails)

    assert(num_names==num_emails),"readin error, numnames neq numemails"
    
    print("Found {:3} names and emails".format(len(names)))
    names_list = [] 
    emails_list = []
    print("Listing people found:")

    for j in range(0,num_emails):
        current_name = names[j]
        current_email = emails[j]
        names_list.append(current_name)
        emails_list.append(current_email)
        print("   Name: {:20}; email: {:20}".format(current_name,current_email))

    return names_list,emails_list 

