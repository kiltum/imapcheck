# imapcheck
```
Checking login/password on IMAP server

optional arguments:
  -h, --help            show this help message and exit
  -l LOGIN, --login LOGIN
                        Login
  -p PASSWORD, --password PASSWORD
                        Password. use stdin for loading from STDIN
  -s SERVER, --server SERVER
                        Server hostname
  --no-ssl              Do not try to use SSL to connect
  -v, --verbose         Show every step with results
  -q, --quiet           Return result only in exit code
```

## Return values

Return OK or FAILED to stdout. Also exit code 0 or 1.

If -q is present, only exit code will return and no any output. 
