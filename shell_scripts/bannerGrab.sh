# Author: Blake Conrad
# The following script simply grabs all banners of open ports on a target system.

nmap -sV --script=banner <target ip address> | grep 'open'
