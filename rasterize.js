var system = require('system');
var webpage = require('webpage');
var writedPdf = 0;
var writedPng = 0;

function render(target){
    var page = webpage.create(),
        address, output, size;

    address = "http://localhost:8000/" + target;
    output = target.substr(0, target.length-5);
    page.viewportSize = { width: 456, height: 600 };

    page.open(address, function (status) {
        if (status !== 'success') {
            console.log('Unable to load the address!' + address);
        } else {
            window.setTimeout(function () {
                page.paperSize = { format: "A5", orientation: 'portrait', margin: '3mm'};

                page.render(output+".pdf");
                console.log("Writing: "+output+".pdf");
                writedPdf ++;

                pageWidth = 456;
                pageHeight = parseInt(pageWidth * 3/4, 10);
                page.viewportSize = { width: pageWidth, height: pageHeight };

                var clipRect = page.evaluate(function(){
                    return document.querySelector("#article-content").getBoundingClientRect();
                });
                page.clipRect = {
                    top:    clipRect.top,
                    left:   clipRect.left,
                    width:  clipRect.width,
                    height: clipRect.height
                };

                page.render(output+".png");
                console.log("Writing: " + output+".png");
                writedPng ++;
            }, 500);
        }
    });
};

for(var i = 1; i< system.args.length; ++i){
    console.log("Rendering: "+ system.args[i]);
    render(system.args[i]);
}
console.log("Total "+ (system.args.length - 1) + " pages" );
window.setTimeout(function () {
    console.log("Write "+ writedPdf + " pdf" );
    console.log("Write "+ writedPng + " png" );
    phantom.exit();
}, system.args.length*1000);
