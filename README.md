# SecretSanta

Input deck is in JSON format. 

Running 
```
python3 main_secretsanta.py 
```
will print out an empty input. This can be piped into a file to be filled in with 
```
python3 main_secretsanta.py > {your_input_name}.json 
```
Having filled in the input, run using:
```
python3 main_secretsanta.py --json {your_input_name}.json 
```
The input fields are as follows:
```
gmail_login 
gmail_passkey
```
are the login and password for your burner gmail (strings). Refer to gmail's guidelines on setting this up for use of their automated service; 
```
list_of_emails
```
should be a three columned excel table in the form
```
index name email
```
for inputting the people playing (path to it, string); 
```
send_emails
```
determines whether emails are actually sent by the program (boolean);
```
test_flag
```
sends a test email (boolean,i.e not the corresponding recipient) if and only if send_emails is also on. The flag
```
reveal_names
```
will print out who has who and should only be used for tests (boolean). Finally the fields,
```
dist_date
budget_lower
budget_lower
```
are the details for the giving of gifts. Namely the date where gifts are exchanged (string) and the lower and upper limits of the budget (float)