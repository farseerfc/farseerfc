#!/bin/bash -x
cp rasterize.js output
cd output
python -m http.server &
SERVPID=$!
echo server pid $SERVPID
sleep 1
find . -iname "*.html" \
	! -iname "*.rst.html" \
	! -iwholename "*/tag/*" \
	! -iwholename "*/author/*" \
	! -iwholename "*/category/*" \
	! -iwholename "*/pages/*" \
	! -iname "tags*" \
	! -iname "authors*" \
	! -iname "categor*" \
	! -iname "pages*" \
	! -iname "archives*" \
	! -iname "search.html" \
	! -iname "index*.html" \
| sed "s#\.\/##g" | xargs -n 16 phantomjs rasterize.js
sleep 30
kill $SERVPID
# find . -iname "*.png" | parallel optipng || true

