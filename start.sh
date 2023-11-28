python3 ./cevio_spider.py

year=`date +%Y `
month=`date +%m `
day=`date +%d `
now=$year-$month-$day


git config --global user.email ""
git config --global user.name "Crawler"

git add .
statusResult=$(git status -u --porcelain)
if [ -z statusResult ]
then
    echo 'no changes found'
else
    echo 'The workspace is modified:'
    echo "$statusResult"
    git commit -m "update $now"
fi
