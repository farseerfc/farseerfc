const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();

  for(var i = 2; i< process.argv.length; ++i){
    var target = process.argv[i];
    var output = target.substr(0, target.length-5);
    console.log("Rendering: "+ target);

    const page = await browser.newPage();
    await page.goto('http://localhost:8000/'+target);
    await page.screenshot({path: output+'.png', fullPage: true});
    await page.pdf({path: output+'.pdf', format: 'a4'});
    await page.close();
  }

  console.log("Total "+ (process.argv.length - 1) + " pages" );

  await browser.close();
})();
