echo -e "bhavesh\n ok\n notok" > file1.txt
echo -e "bh\n huh" > file2.txt

cat file1.txt file2.txt > file3.txt
sort file3.txt > sortedFile3.txt
sort -r file3.txt > sortedRevFile3.txt

> file1.txt
> file2.txt

echo combined 2 files, sorted both ways and cleared original 2 files