# Written by: Blake Conrad
# Content: Iterative Numeric Loop to create 16 Word document files
# Resource: https://www.cyberciti.biz/faq/bash-for-loop/

for i in {1..16}
do
    touch "week_$i.docx"
done
