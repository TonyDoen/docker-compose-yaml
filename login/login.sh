code=`/usr/bin/python ga.py`
passwd='my password'
user='my user name'
host='my user host'

echo 'Google Authenticator App: '$code
lg.exp $code $passwd $user $host

