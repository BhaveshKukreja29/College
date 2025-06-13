
read -p "Enter a 3-digit number: " num
temp=$num
sum=0

while [ $temp -gt 0 ]; do
    digit=$(( temp % 10 ))          # Extract last digit
    cube=$(( digit * digit * digit ))
    sum=$(( sum + cube ))
    temp=$(( temp / 10 ))           # Remove last digit
done

if [ $sum -eq $num ]; then
    echo "$num is an Armstrong number"
else
    echo "$num is not an Armstrong number"
fi
