#!/bin/bash -x
cp rasterize.js output
cd output
python2 -m SimpleHTTPServer &
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
| sed "s#\.\/##g" | xargs phantomjs rasterize.js http://localhost:8000/
kill $SERVPID