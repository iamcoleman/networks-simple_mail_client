# Computer Networks - Simple Mail Client

A simple mail client made for my Computer Networks class.

### mailClient.py
The main mail client file. Connects to SMTP, gets user input for recipient, formats email based off the `email_message.txt` file, and sends the email.

### yourMailLogin.py
File that contains the login credentials and the mail server host and port number for the email account that will be sending the email. Need to update these if you clone the repo.

### email_message.txt
The file that will be the body of your email. You can edit the file however you would like. Use the template `${RECIPIENT_NAME}` somewhere in the file if you would like to include the recipient name acquired from the user input.
