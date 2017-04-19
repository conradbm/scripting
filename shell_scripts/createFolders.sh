# Written by: Blake Conrad
# Content: Iterative Numeric Loop to create 16 Folders
# Resource: https://www.cyberciti.biz/faq/bash-for-loop/

for i in {1..16}
do
    mkdir "week_$i"
done
