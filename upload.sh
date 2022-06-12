cp ~/.mume/parser.js js/
cp ~/.mume/mathjax_config.js js/

for i in {1..9}; do
    mpe2html slides/0$i.md 1
done
mpe2html slides/10.md 1
mpe2html index.md 1

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
