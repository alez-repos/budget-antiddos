echo ==========================================
echo Listening access.log for $1 seconds ...
echo ==========================================

timeout $1 tail -f /var/log/nginx/access.log > m0
cat m0 | grep -vi google | grep -vi bing | cut -d " " -f 1 | sort -u > m0.filtered

echo output at: $PWD/m0.filtered


