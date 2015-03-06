i=0

while read line
do
i=`expr $i + 1`
wget $line --warc-file=$i --no-warc-compression

done < a3.txt
