for FILE in *
do
    if [[ "$FILE" == "secret.txt" ]] ; then
        continue
    fi
    filename="${FILE%%.*}"
    outguess -d secret.txt $filename.jpg $filename-s.jpg
    rm $FILE
done