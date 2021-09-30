iptables -L -n | grep ^DROP | cut -d" " -f 12| sort | grep -v "0/0" | cut -d"/" -f 1
