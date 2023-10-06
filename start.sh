python3 ./cevio_spider.py

year=`date +%Y `
month=`date +%m `
day=`date +%d `
now=$year-$month-$day


git config --global user.email ""
git config --global user.name "Crawler"

git add .
git commit -m "update $now"
