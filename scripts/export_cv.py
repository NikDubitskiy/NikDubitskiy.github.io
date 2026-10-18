"""Build static bilingual CV PDFs. Requires Playwright and a local Chromium."""
from pathlib import Path
import functools,http.server,threading
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
def export():
 server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(ROOT)))
 threading.Thread(target=server.serve_forever,daemon=True).start()
 try:
  with sync_playwright() as p:
   browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
   page=browser.new_page(color_scheme='light')
   for lang,route in [('en','/cv/'),('ru','/ru/cv/')]:
    page.goto(f'http://127.0.0.1:{server.server_port}'+route,wait_until='networkidle')
    page.evaluate("document.documentElement.dataset.theme='light'")
    page.evaluate('document.fonts.ready')
    name='Никита Дубицкий' if lang=='ru' else 'Nikita Dubitskiy'
    page.evaluate("name=>{document.querySelector('h1').textContent=name;document.querySelector('.page-heading .eyebrow').textContent='Curriculum vitae';const p=document.createElement('p');p.className='pdf-contact';p.textContent='nikita.dubitskiy@gmail.com · nikdubitskiy.github.io · ORCID: 0009-0003-1723-8103';document.querySelector('.page-heading').appendChild(p);}",name)
    page.add_style_tag(content='.pdf-contact{font-size:10px;margin-top:14px;color:#333}.page-heading .eyebrow{font-size:10px}.article-section{margin-top:18px}.article-section>h2{margin-bottom:12px}.research-row{padding:0}')
    page.pdf(path=str(ROOT/'assets'/f'nikita-dubitskiy-cv-{lang}.pdf'),format='A4',print_background=True,margin={'top':'13mm','bottom':'13mm','left':'14mm','right':'14mm'})
    print('Exported CV:',lang)
   browser.close()
 finally:server.shutdown()
if __name__=='__main__':export()
