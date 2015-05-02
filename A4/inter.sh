for j in $(seq 2 824) ### Inner for loop ###
 do
#   i=j
   a=`grep -Fx -f 1.txt $j.txt | wc -w`
   echo $a
   #b=`grep -Fxv -f 1.txt $j.txt | wc -w`
   #echo $b
   #c=`grep -Fxv -f $j.txt 1.txt | wc -w`
   #echo $c
   #u=`expr $a + $b + $c`
   #echo $u
   #k=`expr $a / $u`
   #echo $k
   #l=1
   #f=`expr $l - $k`
   #echo $f
   #`echo $f >> final.txt`
done
