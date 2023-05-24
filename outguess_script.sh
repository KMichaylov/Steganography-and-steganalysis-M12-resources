for FILE in *
do
    filename="${FILE%%.*}"
    outguess -d secret.txt $filename.jpg $filename-stego.jpg
done