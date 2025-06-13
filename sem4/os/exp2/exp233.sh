echo Student Roll no. 2303080
a=1
echo Enter the number to find summation
read n
s=0
while [ $a -le $n ]
do
s=$((s+a))
a=$((a+1))
done
echo The summation is $s
