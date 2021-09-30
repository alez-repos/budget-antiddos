# budget-antiddos

I made this script for my potato web server because I suddenly started to recieve thousands of requests per sec which had some weird pattern on the IP addresses of about 200-300 different /24 networks with more than two IP on the same /24. Clearly some kind of botnet pointing at my server.

It helped me to filter that requests so I believe someone who cant afford an expensive anti ddos mechanism can just try to run this script and block the connections.

## How to use

Just edit the files to point to your server access.log, and edit the run.sh script if you want to change the sample time which is 20 seconds.
After the script runs you will see the information retrieved and a set of iptables rules in case you want to apply just copy/paste in the console.