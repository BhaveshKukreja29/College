echo Student Roll no. 2303080
echo Enter number to check if even or odd
read n
rem=$((n%2))
if [ $rem -eq 0 ]
then echo is even
else
echo $n is odd
fi
