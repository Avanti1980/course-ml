cp -r /home/avanti/Slides/Courses/.crossnote/* ./crossnote/
cp -r /home/avanti/Notes/ML/Logistic-Regression/  ./notes/

git add *
git commit -m $1

case $2 in
"ee")
    git push gitee master
    ;;
"hub")
    git push github master
    ;;
"both")
    git push gitee master
    git push github master
    ;;
*)
    echo "error: 2nd par must be [ee|hub|both]!"
    ;;
esac
