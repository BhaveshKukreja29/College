echo Student Roll no. 2303080
echo Enter the number to find factorial
read n
f=1
i=1
while [ $i -le $n ]
do
f=$((f*i))
i=$(($i+1))
done
echo The factorial of $n is $f
