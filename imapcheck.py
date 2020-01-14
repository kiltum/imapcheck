#!/usr/bin/env python3

import argparse
import imaplib
import sys



def main():
    parser = argparse.ArgumentParser(description='Checking login/password on IMAP server')
    parser.add_argument("-l", "--login", help="Login", required=True)
    parser.add_argument("-p", "--password", help="Password. use stdin for loading from STDIN", required=True)
    parser.add_argument("-s", "--server", help="Server hostname", required=True)
    parser.add_argument("--no-ssl", action="store_true", help="Do not try to use SSL to connect")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show every step with results")
    parser.add_argument("-q", "--quiet", action="store_true", help="Return result only in exit code")
    args = parser.parse_args()

    imap = None
    verbose = args.verbose
    password = None
    result = None

    if args.quiet:
        verbose = False

    if args.no_ssl:
        imap = imaplib.IMAP4(args.server)
    else:
        imap = imaplib.IMAP4_SSL(args.server)

    if args.password.lower() == 'stdin':
        password = sys.stdin.read().rstrip()
    else:
        password = args.password

    if verbose:
        print("Try to check " + args.login + "/" + password + " on " + args.server)

    try:
        result = imap.login(args.login, password)
        imap.logout()
    except Exception as e:
        if verbose:
            print("FAILED Error code: " + str(e))
        else:
            if not args.quiet:
                print("FAILED")
        quit(1)
    if verbose:
        print("OK " + str(result[1]))
    else:
        if not args.quiet:
            print("OK")
    quit(0)

if __name__ == "__main__":
    main()