import smtplib
from email.mime.text import MIMEText
from input_class import Input


def distribute_names(names,
                     emails,
                     assignednames,
                     input:Input,
                     ):
        
    print('Entering emailing routine.')


    num_names = len(names) 
    num_emails = len(emails)
    num_assignednames = len(emails)
    assert(num_names==num_emails),"exit: num names neq num emails"
    assert(num_names==num_assignednames),"exit: num names neq num assigned names"
    if input.send_emails:
        print('    Send emails is on - recipients will RECEIVE EMAILS')
    else:
        print('    Send emails is off - recipients will NOT RECEIVE EMAILS')
    if input.test_flag:
        print('    Test emails is on - recipients will not recieve names only a test email (only if send_emails is on).')


    for i in range(num_names):

        out_string = '    Emailing {:16} at {:25} their assigned gift recipient.'.format(names[i],emails[i])
        print(out_string)
        if input.send_emails:
            send_email(assignednames[i],
                       emails[i],
                       i,
                       input
                )
        else:
            print('    TEST RUN - NO EMAIL SENT: message contains gift recipient ',assignednames[i])
    
    return 0 


def send_email(name,address,index,input:Input):
    real_body = 'You have been assigned {:20} The budget is {:5} to {:5} pounds and the distribution of gifts will be {:10}.'
    sent_from = input.gmail_login
    to = [address]
    if input.test_flag == False:
        subject = 'Santa has assigned you a recipient!'
        body = real_body.format(name,input.budget_lower,input.budget_upper,input.dist_date)
    else:
        print('-----TEST EMAIL-----',index)
        subject = 'santa test'
        body = str(index) 

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(input.gmail_login, input.gmail_passkey)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("    Email to " + address + "  sent successfully!")
    except Exception as ex:
        print ("    Something went wrong….",ex)