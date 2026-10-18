"""Sourced research notes, not duplicate full-text publisher copies."""
from html import escape as esc

NOTES = {
 'substrate-magnetotransport': {
  'parent':'publications','paper':0,
  'ru': {'short':'Подложка и магнитотранспорт SrIrO₃','description':'Работа Никиты Дубицкого и соавторов о структуре и магнитотранспорте SrIrO₃ на разных подложках и гетероструктурах с манганитом.',
   'summary':'В этой работе мы сопоставляем структуру плёнок SrIrO₃ с их электронным и магнитным транспортом. Изменяя подложку, можно менять условия эпитаксиального роста и деформации решётки. Второй объект исследования — гетероструктуры SrIrO₃/La₀.₇Sr₀.₃MnO₃, где иридат соседствует с магнитным оксидом.',
   'question':'Как выбор подложки связан со структурой плёнки и её откликом на магнитное поле?',
   'methods':'Рентгеновская дифракция, фотоэлектронная спектроскопия, измерения сопротивления, эффекта Холла и магнитосопротивления.',
   'context':'Работа связывает исследования отдельных плёнок с задачей создания оксидных структур для спинтроники.',
   'version':'Журнальная версия опубликована онлайн в 2026 году; библиографический год выпуска — 2027. Рукопись arXiv 2025 года имеет другое название и приведена отдельно.'},
  'en': {'short':'Substrate effects and SrIrO₃ magnetotransport','description':'Research by Nikita Dubitskiy and colleagues on substrate-dependent SrIrO₃ structure, magnetotransport and iridate/manganite heterostructures.',
   'summary':'We compare the structure of SrIrO₃ films with their electronic and magnetic transport. Changing the substrate changes the conditions for epitaxial growth and lattice strain. A second part concerns SrIrO₃/La₀.₇Sr₀.₃MnO₃ heterostructures, which combine the iridate with a magnetic oxide.',
   'question':'How does substrate choice relate to film structure and its response to a magnetic field?',
   'methods':'X-ray diffraction, photoelectron spectroscopy, resistance, Hall-effect and magnetoresistance measurements.',
   'context':'The work connects individual oxide films with heterostructures relevant to spintronics.',
   'version':'Published online in 2026; the journal issue year is 2027. The 2025 arXiv manuscript has a different title and is linked separately.'}},
 'josephson-iridates': {
  'parent':'publications','paper':2,
  'ru': {'short':'Джозефсоновские структуры с иридатами','description':'Никита Дубицкий и соавторы: джозефсоновский транспорт через проводящие SrIrO₃ и изолирующие Sr₂IrO₄ прослойки. Работа 2026 года.',
   'summary':'Мы исследовали сверхпроводящие структуры Nb/иридат/YBa₂Cu₃O₇₋δ с двумя типами прослоек. Через проводящий SrIrO₃ и изолирующий Sr₂IrO₄ наблюдался джозефсоновский ток. Различие материалов проявилось в нормальном сопротивлении и характеристическом напряжении переходов.',
   'question':'Как меняются свойства сверхпроводящего перехода при замене проводящей прослойки на изолирующую?',
   'methods':'При 4,2 К измерены вольт-амперные характеристики и зависимость критического тока от магнитного поля.',
   'context':'При толщине SrIrO₃ 15 нм произведение IсRₙ составило 0,1–0,3 мкВ; для Sr₂IrO₄ толщиной 5 нм — 41–79 мкВ. Полные результаты и условия сравнения приведены в публикации.',
   'version':'Расширенные тезисы конференции, опубликованы 9 сентября 2026 года.'},
  'en': {'short':'Josephson structures with strontium iridates','description':'Nikita Dubitskiy and colleagues: Josephson transport through conducting SrIrO₃ and insulating Sr₂IrO₄ interlayers. Conference publication, 2026.',
   'summary':'We studied Nb/iridate/YBa₂Cu₃O₇₋δ superconducting structures with two interlayer materials. Both conducting SrIrO₃ and insulating Sr₂IrO₄ carried a Josephson current. Their different transport regimes were reflected in normal resistance and characteristic voltage.',
   'question':'How does replacing a conducting interlayer with an insulating one change a superconducting junction?',
   'methods':'Current–voltage characteristics and magnetic-field-dependent critical current were measured at 4.2 K.',
   'context':'IсRₙ was 0.1–0.3 μV for 15-nm SrIrO₃ and 41–79 μV for 5-nm Sr₂IrO₄. The publication gives the full results and comparison conditions.',
   'version':'Conference extended abstract, published 9 September 2026.'}},
 'thesis': {
  'parent':'research','paper':None,
  'ru': {'short':'Подложка, структура и транспорт SrIrO₃','description':'Магистерская диссертация Никиты Дубицкого: сравнение плёнок SrIrO₃ на пяти подложках, структура, химическое состояние и электронный транспорт.',
   'summary':'В магистерской работе я исследовал плёнки SrIrO₃ на пяти подложках: SrTiO₃, NdGaO₃, LSAT, LaAlO₃ и PMN–PT. Образцы получены ВЧ-магнетронным распылением. Сравнение одной серии позволяет проследить связь между выбором подложки, структурой, химическим окружением и электрическими свойствами.',
   'question':'Что определяет транспорт в эпитаксиальной плёнке: деформация решётки, локальная химия и морфология поверхности?',
   'methods':'Рентгеновская дифракция и АСМ использованы для исследования структуры и поверхности, РФЭС — для анализа химического состояния. Сопротивление измерено в диапазоне 4,2–300 К, эффект Холла — при 2 и 10 К в полях до ±7 Тл.',
   'context':'Отдельный эксперимент посвящён SrIrO₃ на пьезоэлектрической подложке PMN–PT: приложенное напряжение меняет деформацию подложки, а электрический отклик измеряется на плёнке. Эта работа входит в более широкое исследование SrIrO₃, Sr₂IrO₄ и гетероструктур на их основе.',
   'version':'Магистратура по физике, НИУ ВШЭ, 2026. Научный руководитель — Г. А. Овсянников. На Figshare размещена переработанная английская версия; DOI относится к этой версии диссертации, а не к журнальной статье.'},
  'en': {'short':'Substrate, structure and transport in SrIrO₃','description':'Nikita Dubitskiy’s master’s thesis: SrIrO₃ on five substrates, linking structure, chemical state and electronic transport. HSE University, 2026.',
   'summary':'My master’s thesis examines SrIrO₃ films grown by RF magnetron sputtering on five substrates: SrTiO₃, NdGaO₃, LSAT, LaAlO₃ and PMN–PT. Comparing one film series connects substrate choice with structure, local chemical environment and electrical properties.',
   'question':'How do lattice strain, local chemistry and surface morphology relate to transport in an epitaxial film?',
   'methods':'X-ray diffraction and AFM probe structure and surface morphology; XPS examines chemical state. Resistance was measured from 4.2 to 300 K, with Hall measurements at 2 and 10 K in fields up to ±7 T.',
   'context':'A separate experiment uses a piezoelectric PMN–PT substrate: an applied voltage changes substrate strain while the electrical response is measured in the SrIrO₃ film. The thesis is one part of my broader work on SrIrO₃, Sr₂IrO₄ and oxide heterostructures.',
   'version':'Master’s degree in Physics, HSE University, 2026. Supervisor: G. A. Ovsyannikov. Figshare hosts the revised English edition; its DOI identifies the thesis edition, not a journal article.'}}
}

def route(lang, slug, path):
 return path(lang,NOTES[slug]['parent'])+slug+'/'

def content(lang,slug,papers,text,a,path):
 n=NOTES[slug];t=n[lang];ru=lang=='ru'
 tr=lambda r,e:r if ru else e
 p=papers[n['paper']] if n['paper'] is not None else None
 title=p['ru_title'] if p and ru else p['title'] if p else text[lang]['thesistitle']
 authors=p['authors'] if p else 'Nikita Dubitskiy'
 publication=(p['journal']+' · '+str(p['year'])+' · '+p['details']) if p else tr('Магистерская диссертация · НИУ ВШЭ · 2026','Master’s thesis · HSE University · 2026')
 url=p['url'] if p else 'https://doi.org/10.6084/m9.figshare.34003488.v1'
 doi=p['doi'] if p else '10.6084/m9.figshare.34003488.v1'
 sections=[('summary',tr('О работе','About this work'),t['summary']),('question',tr('Исследовательский вопрос','Research question'),t['question']),('methods',tr('Что измеряли','Measurements'),t['methods']),('context',tr('Результат и контекст','Results and context'),t['context'])]
 body=f'<header class="page-heading"><p class="eyebrow">{tr("Никита Дубицкий и соавторы" if p else "Никита Дубицкий","Nikita Dubitskiy and colleagues" if p else "Nikita Dubitskiy")}</p><h1>{esc(title)}</h1><p class="authors" lang="en">{esc(authors)}</p><p class="journal">{esc(publication)}</p></header>'
 body+=''.join(f'<section class="article-section" id="{id}"><h2>{heading}</h2><p>{esc(value)}</p></section>' for id,heading,value in sections)
 body+=f'<section class="article-section" id="sources"><h2>{tr("Публикация и материалы","Publication and materials")}</h2><p>{esc(t["version"])}</p><p>DOI: {esc(doi)}</p><div class="actions">{a(url,tr("Открыть публикацию ↗","Read publication ↗"),"button")}'
 if p and p.get('preprint'):body+=a(p['preprint'],tr('Рукопись arXiv · 2025 ↗','arXiv manuscript · 2025 ↗'))
 if not p:body+=a('https://ndownloader.figshare.com/files/69376527',tr('Полный текст · PDF ↗','Full text · PDF ↗'))
 if p:body+=f'<a href="/assets/citations/{slug}.bib" download>BibTeX</a><a href="/assets/citations/{slug}.ris" download>RIS</a>'
 body+='</div></section><section class="article-section"><h2>'+tr('Связанные работы','Related work')+'</h2><ul>'
 for other,note in NOTES.items():
  if other!=slug:body+='<li>'+a(route(lang,other,path),esc(note[lang]['short']))+'</li>'
 body+='</ul><p>'+a(path(lang,'publications'),tr('Все публикации →','All publications →'))+'</p></section>'
 toc=sections+[('sources',tr('Источники','Sources'),'')]
 return '<div class="reading-layout"><aside class="contents"><nav aria-label="'+tr('Содержание страницы','On this page')+'"><p>'+tr('Содержание','Contents')+'</p>'+''.join(a('#'+id,h) for id,h,_ in toc)+'</nav></aside><div class="article-body research-note">'+body+'</div></div>'

def metadata(lang,slug,papers,text,base):
 n=NOTES[slug];p=papers[n['paper']] if n['paper'] is not None else None
 title=p['title'] if p else text['en']['thesistitle']
 authors=p['authors'].replace(' et al.','').split(', ') if p else ['Nikita Dubitskiy']
 values=[('citation_title',title),('citation_publication_date',str(p['year']) if p else '2026'),('citation_doi',p['doi'] if p else '10.6084/m9.figshare.34003488.v1')]
 values.extend(('citation_author',author) for author in authors)
 if p:values.append(('citation_journal_title',p['journal']))
 else:values.extend([('citation_dissertation_institution','HSE University'),('citation_pdf_url','https://ndownloader.figshare.com/files/69376527')])
 return ''.join(f'<meta name="{key}" content="{esc(value,quote=True)}">' for key,value in values)

def entity(lang,slug,papers,text,base):
 n=NOTES[slug];p=papers[n['paper']] if n['paper'] is not None else None
 item={'@type':'ScholarlyArticle' if p else 'Thesis','@id':'https://doi.org/'+(p['doi'] if p else '10.6084/m9.figshare.34003488.v1'),'headline':p['title'] if p else text['en']['thesistitle'],'description':n[lang]['summary'],'author':[],'url':p['url'] if p else 'https://doi.org/10.6084/m9.figshare.34003488.v1'}
 for author in p['authors'].split(', ') if p else ['Nikita Dubitskiy']:
  item['author'].append({'@id':base+'/#nikita-dubitskiy'} if 'Dubitskiy' in author else {'@type':'Person','name':author})
 if p:item['isPartOf']={'@type':'Periodical','name':p['journal']}
 else:item.update(educationalLevel='Master’s degree',inLanguage='en',license='https://creativecommons.org/licenses/by/4.0/')
 return item
