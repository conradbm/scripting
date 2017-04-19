# Given a sloppy file, how to cut it up

cat 50_best.txt | grep 'span' | sed -n 's:.*<span>\(.*\)</span>.*:\1:p' | awk '{print substr($0,3,length($0))}' >> 50_best_cut.txt

