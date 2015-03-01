#!/bin/bash
outdir=output
filepath=$1
dirn=$(dirname $1)
basen=$(basename $1 .html)
echo phantomjs rasterize.js http://$SITEURL/$filepath $outdir/$dirn/$basen.png 456
phantomjs rasterize.js http://$SITEURL/$filepath $outdir/$dirn/$basen.png 456
echo phantomjs rasterize.js http://$SITEURL/$filepath $outdir/$dirn/$basen.pdf A5
phantomjs rasterize.js http://$SITEURL/$filepath $outdir/$dirn/$basen.pdf A5
