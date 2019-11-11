# SMTP
import smtplib

# MIMEMultipart Message Object
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email Validation
from validate_email import validate_email


def getRecipient():
    yes = {'yes', 'ye', 'y'}
    while True:
        print("Please type the recipient's name:")
        recName = input()
        print("Please type the recipient's email address:")
        recAddress = input()
        print("Is this correct (Y/n)? {} at {}".format(recName, recAddress))
        choice = input().lower()
        if choice in yes:
            if validate_email(recAddress):
                return recName, recAddress
            else:
                print("Email is invalid\n")


def main():
    # get the name and address of recipient
    recName, recAddress = getRecipient()

    # setup the SMTP server
    server = smtplib.SMTP()
    return

if __name__ == '__main__':
    main()
