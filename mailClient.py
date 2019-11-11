# yourMailLogin.py
import yourMailLogin

# Template
from string import Template

# SMTP
import smtplib

# MIMEMultipart Message Object
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email Validation
from validate_email import validate_email


def getRecipient():
    """
    Returns the recipient name and address from user input

    :return:
    """

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
                print("Email ({}) is invalid\n".format(recAddress))


def getMessage(filename):
    """
    Returns a Template object for the message

    :param filename:
    :return:
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_contents = template_file.read()
    return Template(template_file_contents)


def main():
    # get the name and address of recipient
    recName, recAddress = getRecipient()

    # get the message to email
    messageTemplate = getMessage('email_message.txt')
    message = messageTemplate.substitute(RECIPIENT_NAME=recName)
    print("\nCreated the message:\n\n{}\n".format(message))

    # setup the SMTP server
    MY_ADDRESS, MY_PASSWORD = yourMailLogin.yourMailLogin()
    SERVER_ADDRESS, SERVER_PORT = yourMailLogin.yourMailSMTP()
    try:
        print("Connecting to mail server...")
        server = smtplib.SMTP(host=SERVER_ADDRESS, port=SERVER_PORT)
        server.starttls()
    except:
        print("Could not connect to mail server!")
        return

    try:
        print("Logging into email account...")
        server.login(MY_ADDRESS, MY_PASSWORD)
    except:
        print("Could not login to email account!")
        return

    # create the email
    email = MIMEMultipart()
    email['From']=MY_ADDRESS
    email['To']=recAddress
    email['Subject']="Coleman's Mail Client"
    email.attach(MIMEText(message, 'plain'))

    # send email with SMTP server
    try:
        print("Sending the email...")
        server.send_message(email)
    except:
        print("Could not send email!")
        return

    # terminate the SMTP session and close connection
    print("Success!")
    server.quit()


if __name__ == '__main__':
    main()
