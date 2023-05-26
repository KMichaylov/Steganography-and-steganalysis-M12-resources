# Only embedd in the following images:
#     • Building
    # • City
    # • Food
    # • Party
    # • Nature
    # • Stadium
    # • River
    # • Sea

# passphrase - secret$#497
for FILE in *
do
    if [[ "$FILE" == "secret.txt" ]] ; then
        continue
    fi
    filename="${FILE%%.*}"
    steghide embed -cf $filename.jpg -ef secret.txt -sf $filename-s.jpg
    rm $FILE
done
