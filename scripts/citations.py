"""Export bibliographic records without counting a preprint twice."""
import re

def journal_fields(paper):
 match=re.fullmatch(r'([^,(]+)(?:\(([^)]+)\))?, (.+)',paper['details'])
 if not match:return {}
 volume,issue,pages=match.groups()
 return {'volume':volume,**({'number':issue} if issue else {}),'pages':pages.replace('–','--')}

def tex(value):
 return value.replace('&',r'\&').replace('%',r'\%').replace('#',r'\#').replace('_',r'\_')

def author_names(paper):
 partial='et al.' in paper['authors']
 names=paper['authors'].replace(' et al.','').split(', ')
 return names,partial

def bib(paper,key):
 names,partial=author_names(paper)
 authors=[]
 for name in names:
  given,family=name.rsplit(' ',1);authors.append(family+', '+given)
 if partial:authors.append('others')
 fields={'title':'{'+tex(paper['title'])+'}','author':tex(' and '.join(authors)),'journal':tex(paper['journal']),'year':str(paper['year']),**journal_fields(paper),'doi':paper['doi'],'url':paper['url']}
 return '@article{'+key+',\n'+''.join('  '+k+' = {'+v+'},\n' for k,v in fields.items())+'}\n'

def ris(paper):
 names,partial=author_names(paper)
 rows=['TY  - JOUR','TI  - '+paper['title']]
 for name in names:
  given,family=name.rsplit(' ',1);rows.append('AU  - '+family+', '+given)
 rows+=['JO  - '+paper['journal'],'PY  - '+str(paper['year']),'DO  - '+paper['doi'],'UR  - '+paper['url']]
 fields=journal_fields(paper)
 if fields.get('volume'):rows.append('VL  - '+fields['volume'])
 if fields.get('number'):rows.append('IS  - '+fields['number'])
 if fields.get('pages'):
  pages=fields['pages'].split('--');rows.append('SP  - '+pages[0])
  if len(pages)>1:rows.append('EP  - '+pages[-1])
 if partial:rows.append('N1  - Author list abbreviated in source bibliography.')
 if paper.get('conference'):rows.append('N1  - Conference extended abstract.')
 if paper['year']==2027:rows.append('N1  - Published online in 2026; journal issue January 2027.')
 return '\n'.join(rows+['ER  - ',''])+'\n'

def build(root,papers,notes):
 target=root/'assets/citations';target.mkdir(exist_ok=True)
 (root/'assets/publications.bib').write_text('\n'.join(bib(p,'dubitskiy'+str(i+1)) for i,p in enumerate(papers)),encoding='utf-8')
 (root/'assets/publications.ris').write_text('\n'.join(ris(p) for p in papers),encoding='utf-8')
 for slug,note in notes.items():
  if note['paper'] is not None:
   p=papers[note['paper']]
   (target/(slug+'.bib')).write_text(bib(p,slug),encoding='utf-8')
   (target/(slug+'.ris')).write_text(ris(p),encoding='utf-8')
