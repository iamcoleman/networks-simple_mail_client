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


def get_recipient():
    """
    Returns the recipient name and address from user input

    :return recName, recAddress:
    """

    yes = {'yes', 'ye', 'y'}
    while True:
        print("Please type the recipient's name:")
        rec_name = input()
        print("Please type the recipient's email address:")
        rec_address = input()
        print("Is this correct (Y/n)? {} at {}".format(rec_name, rec_address))
        choice = input().lower()
        if choice in yes:
            if validate_email(rec_address):
                return rec_name, rec_address
            else:
                print("Email ({}) is invalid\n".format(rec_address))


def get_message(filename):
    """
    Returns a Template object for the message

    :param filename:
    :return Template:
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_contents = template_file.read()
    return Template(template_file_contents)


def main():
    # get the name and address of recipient
    rec_name, rec_address = get_recipient()

    # get the message to email
    # ${RECIPIENT_NAME} in template will get replaced
    message_template = get_message('email_message.txt')
    message = message_template.substitute(RECIPIENT_NAME=rec_name)
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
    email['From'] = MY_ADDRESS
    email['To'] = rec_address
    email['Subject'] = "Coleman's Mail Client"
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
