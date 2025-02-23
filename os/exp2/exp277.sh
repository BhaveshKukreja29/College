#!/bin/sh
echo "Student Roll no. 2303080"
entry () {
echo "Enter Username"
read username
echo "Enter Password"
read password
}
entry
if [ "$username" = "Admin" ] && [ "$password" = "Secret" ]; then
echo "Login Successful"
else
echo "Invalid Username or Password"
fi
