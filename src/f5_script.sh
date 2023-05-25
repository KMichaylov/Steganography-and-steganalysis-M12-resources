# Only embedd in the following images:
#     • Building
    # • City
    # • Food
    # • Party
    # • Nature
    # • Stadium
    # • River
    # • Sea
for FILE in *
do
    if [[ "$FILE" == "secret.txt" ]] ; then
        continue
    fi
    filename="${FILE%%.*}"
    outguess -d secret.txt $filename.jpg $filename-stego.jpg
    f5 e -e secret.txt -p "secret$#497" $filename.jpg $filename-stego.jpg
    rm $FILE
done

/home/kristiyan/m12-tools/f5-steganography/tests
