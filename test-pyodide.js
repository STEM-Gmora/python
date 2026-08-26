const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file:///Users/thanojbuddhima/Development/python-lessons/01-introduction.html');
  await page.waitForLoadState('networkidle');
  // click run button
  await page.click('#runBtn');
  // wait for output
  await page.waitForTimeout(3000);
  const text = await page.textContent('#outLine');
  console.log("Output:", text);
  await browser.close();
})();
