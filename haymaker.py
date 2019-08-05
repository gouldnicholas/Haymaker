

import asyncio
from pyppeteer import launch

async def main():
    
    ctr=1
    #replace ... with path of file
    #reads from url list and outputs to text called haystack index
    with open ("/Users/.../urllist.txt", "r") as myfile,open("/Users/.../haystackindex.txt","a+") as out:
        for line in myfile:
            #gets rid of \n
            line=line.strip()
            print(line)
            #HTTPS
            try:
                browser = await launch(headless=True,ignoreHTTPSerrors=True )
                page = await browser.newPage()
                await page.goto(f'https://{line}')
                #replace ... with path of file where screenshots will be stored
                await page.screenshot(path='/Users/.../'+str(ctr)+'.png', fullpage=True)
                print('Screenshot(https)1\n')
                out.write(str(ctr)+'='+"https://"+line+'\n')
                out.flush()
                ctr =ctr+1
                await browser.close()
            except:
                print('except1\n')
                await browser.close()
                pass
            #HTTP
            try:
                browser = await launch(headless=True,ignoreHTTPSerrors=True )
                page = await browser.newPage()
                await page.goto(f'http://{line}')
                #replace ... with path of file where screenshots will be stored
                await page.screenshot(path='/Users/.../'+str(ctr)+'.png', fullpage=True)
                print('Screenshot(http)2\n')
                out.write(str(ctr)+'='+"http://"+line+'\n')
                out.flush()
                ctr =ctr+1
                await browser.close()
            except:
                print('except2\n')
                await browser.close()
                pass
    myfile.close
    out.close


asyncio.get_event_loop().run_until_complete(main())