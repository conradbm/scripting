date_transformed=$(date | cut -d ' ' -f 2,3,4 | tr ' ' ',');
echo $date_transformed
