#!/usr/bin/env python
#
# Very simple Python script to dump all emails in an IMAP folder to files.
# This code is released into the public domain.
#
# RKI Nov 2013
#
import sys
import imaplib
import getpass

IMAP_SERVER = 'server'
EMAIL_ACCOUNT = "email@email.com"
EMAIL_FOLDER = "Inbox"
OUTPUT_DIRECTORY = '/DKIMMessages/'

#PASSWORD = getpass.getpass()
PASSWORD = 'PASSWORD'


def process_mailbox(M):
    """
    Dump all emails in the folder to files in output directory.
    """

    rv, data = M.search(None, "ALL")
    if rv != 'OK':
        print("No messages found!")
        return

    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print("ERROR getting message")
            return
        print("Writing message ")
        f = open('%s/%s.eml' %(OUTPUT_DIRECTORY, num), 'wb')
        f.write(data[0][1])
        f.close()
# Mark the message as deleted
        M.store(num, '+FLAGS', '\\Deleted')

def main():
    M = imaplib.IMAP4_SSL(IMAP_SERVER)
    M.login(EMAIL_ACCOUNT, PASSWORD)
    rv, data = M.select(EMAIL_FOLDER)
    if rv == 'OK':
        print("Processing mailbox: ")
        process_mailbox(M)
        M.close()
    else:
        print("ERROR: Unable to open mailbox ")
    M.logout()

if __name__ == "__main__":
    main()
