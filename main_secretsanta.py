import drawing_names
import readin
import emailing_people
import constants
from input_class import Input
import json 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-j', '--json',  help='path of json')
args = parser.parse_args()

def main(input:Input):
    gmail_user = input.gmail_login
    gmail_password = input.gmail_passkey

    
    send_emails = input.send_emails
    test_flag = input.test_flag
    reveal_names = input.reveal_names

    print(constants.block)
    nameinput,emailinput = readin.readin_from_excel(input.list_of_emails)
    print(constants.block)
    assigned_names = drawing_names.draw_until_noone_has_themselves(nameinput)
    print(constants.block)
    if reveal_names:
        drawing_names.reveal_names(nameinput,assigned_names)

    emailing_people.distribute_names(
                                     names=nameinput,
                                     assignednames=assigned_names,
                                     emails=emailinput,
                                     input=input
                                     )
    print(constants.block)
    print('Stopping normally.')
    print(constants.block)


if not args.json:
    input_default = Input()
    default = json.dumps(input_default.__dict__,indent=1)
    print(default) 

else: 
    with open(args.json, 'r') as j:
        contents = json.loads(j.read())

    input = Input(**contents)
    main(input)