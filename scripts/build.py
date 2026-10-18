"""Generate the academic website with Python 3; no dependencies."""
from pathlib import Path
from html import escape as esc
import json
import re
import structured_data
import details
import citations
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
BASE='https://nikdubitskiy.github.io'
THESIS='https://doi.org/10.6084/m9.figshare.34003488'
PDF='https://ndownloader.figshare.com/files/69376527'
PROFILES={'ORCID':'https://orcid.org/0009-0003-1723-8103','Google Scholar':'https://scholar.google.com/citations?user=HyAEbn0AAAAJ','ResearchGate':'https://www.researchgate.net/profile/Nikita-Dubitskiy','CoLab':'https://colab.ws/researchers/R-3F94E-0DAFF-KP01K'}
CONFIG=json.loads((ROOT/'site-config.json').read_text())
PORTRAIT=BASE+'/assets/nikita-dubitskiy.jpg'

# Issue years follow the bibliography. The JPCS article has issue year 2027;
# its 2025 arXiv precursor is an additional link, not a second publication.
PAPERS=[
 {'year':2027,'title':'Substrate-dependent structure and magnetotransport of epitaxial SrIrO₃ thin films and SrIrO₃/La₀.₇Sr₀.₃MnO₃ heterostructures','authors':'G. A. Ovsyannikov, N. V. Dubitskiy, G. D. Ulev, K. I. Constantinian, I. E. Moskal, V. A. Baydikova, A. M. Petrzhik, A. V. Shadrin, A. V. Mashirov','journal':'Journal of Physics and Chemistry of Solids','details':'220, 114155','doi':'10.1016/j.jpcs.2026.114155','preprint':'https://arxiv.org/abs/2511.02998'},
 {'year':2026,'title':'Topological strontium iridate as an interlayer in superconducting heterostructures','authors':'N. V. Dubitskiy, Y. V. Kislinskii, G. A. Ovsyannikov, K. I. Constantinian, G. D. Ulev, I. E. Moskal, A. M. Petrzhik','journal':'RENSIT','details':'18(4), 443–452','doi':'10.17725/j.rensit.2026.18.443'},
 {'year':2026,'title':'Josephson Transport through Spin–Orbit-Coupled SrIrO₃ and Sr₂IrO₄ Interlayers','authors':'N. Dubitskiy, G. Ovsyannikov, Y. Kislinskii, G. Ulev, A. Petrzhik','journal':'Mesoscience & Nanotechnology','details':'1(3), 01-03005','doi':'10.64214/jmsn.01.03005','conference':True},
 {'year':2025,'title':'Epitaxial Growth, Structure and Electronic Transport of SrIrO₃ Thin Films','authors':'N. V. Dubitskiy, V. A. Baydikova, G. A. Ovsyannikov et al.','journal':'RENSIT','details':'17(4), 439–448','doi':'10.17725/j.rensit.2025.17.439'},
 {'year':2025,'title':'Structure and Electronic Transport in SrIrO₃ Thin Films Under Epitaxial Strain Induced by Substrate Lattice Mismatch','authors':'N. V. Dubitskiy, V. A. Baydikova, A. M. Petrzhik, I. E. Moskal, A. V. Shadrin, V. A. Shmakov, G. A. Ovsyannikov','journal':'Physics of the Solid State','details':'67(6), 1073–1081','doi':'10.61011/PSS.2025.06.61710.4HH-25'},
 {'year':2025,'title':'Effect of epitaxial stresses on the structure and electron transport in strontium iridate thin films','authors':'V. A. Baydikova, N. V. Dubitskiy, A. M. Petrzhik et al.','journal':'Physics of Metals and Metallography','details':'126(13), 1652–1658','doi':'10.1134/S0031918X25602069'},
 {'year':2025,'title':'Electron Transport in Strontium Iridate Thin Films and Superconducting Heterostructures','authors':'Y. V. Kislinskii, I. E. Moskal, V. A. Baydikova, K. Y. Constantinian, N. V. Dubitskiy, A. M. Petrzhik, G. D. Ulev, A. V. Shadrin, V. A. Shmakov, G. A. Ovsyannikov','journal':'Physics of the Solid State','details':'67(7), 1311–1315','doi':'10.61011/PSS.2025.07.61895.24HH-25'},
 {'year':2024,'title':'Structural Features, Electronic and Spin Transport in Epitaxial Thin Films of Iridates','authors':'V. A. Baydikova, N. V. Dubitskiy, I. E. Moskal et al.','journal':'RENSIT','details':'16(4), 509–518','doi':'10.17725/j.rensit.2024.16.509'},
 {'year':2024,'title':'Growth of epitaxial thin films of Sr₂IrO₄ antiferromagnet for spintronics heterostructures','authors':'I. E. Moskal, Y. V. Kislinskii, A. M. Petrzhik, G. A. Ovsyannikov, N. V. Dubitskiy','journal':'Physics of the Solid State','details':'66(7), 1063–1067','doi':'10.61011/PSS.2024.07.58977.58HH'},
 {'year':2024,'title':'Production of and Electronic Transport in Thin Films of Strontium Iridate','authors':'I. E. Moskal, A. M. Petrzhik, Y. V. Kislinskii, A. V. Shadrin, G. A. Ovsyannikov, N. V. Dubitskiy','journal':'Bulletin of the Russian Academy of Sciences: Physics','details':'88(4), 582–585','doi':'10.1134/S1062873823706360'},
 {'year':2023,'title':'Strontium Iridates as Barrier Materials for Josephson Heterostructures','authors':'Y. V. Kislinskii, K. Y. Constantinian, I. E. Moskal, N. V. Dubitskiy, A. M. Petrzhik, A. V. Shadrin, G. A. Ovsyannikov','journal':'Russian Microelectronics','details':'52(Suppl. 1), S53–S58','doi':'10.1134/S1063739723600802'}
]

TEXT={
 'en':{
 'name':'Nikita Dubitskiy','other':'Никита Владимирович Дубицкий','role':'Experimental condensed matter physics',
 'nav':['Home','Research','Publications','CV','Contact'],
 'intro':'Thin films. Strong spin–orbit coupling. Electronic transport.',
 'bio':'I am a physicist and research engineer at the Kotelnikov Institute of Radioengineering and Electronics, Russian Academy of Sciences, in Moscow. I study epitaxial strontium iridate films and oxide heterostructures, connecting their crystal structure and local chemistry to electronic transport.',
 'description':'Nikita V. Dubitskiy — physicist at Kotelnikov IRE RAS. SrIrO₃ and Sr₂IrO₄ thin films, spintronics, electronic transport and superconducting heterostructures.',
 'explore':'Explore research','selected':'Selected publications','allpapers':'All publications','latest':'Latest journal article',
 'thesis':'Master’s thesis','thesistitle':'Substrate-Driven Epitaxial Strain Effects on Structure and Electronic Transport in Spin–Orbit-Coupled SrIrO₃ Thin Films',
 'edition':'Revised English edition · HSE University · 2026','read':'Read the thesis','download':'Download PDF · 18.8 MB',
 'afm':'SrIrO₃ on NdGaO₃ · AFM, 5 × 5 μm²','figure':'From the master’s thesis, Fig. 9(c).',
 'question':'How do a substrate and the local defect environment shape transport in a spin–orbit-coupled oxide?',
 'researchbody':'My recent research follows the relationship between structure, local chemistry and transport in epitaxial SrIrO₃. The master’s thesis compares films grown by RF magnetron sputtering on five substrates: SrTiO₃, NdGaO₃, LSAT, LaAlO₃ and PMN–PT.',
 'topics':[
 ('Epitaxial growth & structure','A series of approximately 35 nm films spans compressive and tensile lattice mismatch. X-ray diffraction identifies the oriented orthorhombic perovskite phase; AFM reveals how surface morphology changes between substrates.'),
 ('Local chemistry & spin–orbit coupling','XPS probes the Ir chemical state, the Ir 4f spin–orbit splitting and the near-surface oxygen environment. Structural and spectroscopic observations help interpret substrate-dependent transport.'),
 ('Charge transport & Hall effect','Resistance measurements from 4.2 to 300 K are combined with Hall measurements at 2 and 10 K in fields up to ±7 T. The Hall sign differs between substrates, consistent with changing electron and hole contributions in a multiband semimetal.'),
 ('Electrical strain control','In SrIrO₃/PMN–PT, an applied voltage up to 300 V produces a room-temperature resistance change of approximately 0.022%. The response is consistent with a contribution from piezoelectric strain transfer.')],
 'methods':'Experimental methods','methodlist':[('Growth','RF magnetron sputtering'),('Structure & morphology','XRD, reciprocal-space mapping, AFM'),('Chemical state','X-ray photoelectron spectroscopy'),('Transport','Low-temperature resistance, Hall effect, magnetotransport'),('Analysis','Python, Origin, MAUD; fitting and uncertainty estimation')],
 'interpretation':'The thesis treats the Kondo-like contribution as a phenomenological description: it does not by itself establish magnetic scattering centers. Hall signs in a multiband material do not uniquely determine individual carrier densities.',
 'series':'AFM comparison of SrIrO₃ films on (a) LSAT, (b) STO, (c) NGO, (d) LAO and (e) PMN–PT; (f) bare PMN–PT. Each panel has its own height scale. Original figure from the revised English thesis, Fig. 9, p. 24 (PDF p. 29).',
 'pubintro':'Journal articles and a conference extended abstract. DOI links lead to published versions; the earlier arXiv manuscript is linked alongside its corresponding journal article.',
 'search':'Search titles, authors or journals','year':'Filter by year','all':'All years','empty':'No publications match your search.','count':'publications',
 'article':'Journal article','conference':'Conference extended abstract','preprint':'Earlier arXiv manuscript (2025)',
 'cvintro':'Education, research experience and experimental skills.','experience':'Research experience','engineer':'Research engineer','institute':'Kotelnikov Institute of Radioengineering and Electronics, RAS','lab':'Laboratory No. 233 · Moscow, Russia','present':'present',
 'work':'Epitaxial oxide thin-film growth, structural and spectroscopic characterization, and electrical transport measurements.',
 'education':'Education','master':'Master’s degree in Physics','bachelor':'Bachelor’s degree','hse':'HSE University · Faculty of Physics','mirea':'MIREA — Russian Technological University',
 'awards':'Selected academic distinctions','awardlist':['Prize winner, VI Student Conference “From Galactic Nuclei to Atomic Scales”, HSE University (2024).','Second-degree prize diploma, 66th All-Russian Scientific Conference, MIPT (2024).'],
 'print':'Print / save as PDF','languages':'Languages','languageval':'Russian · English','contactintro':'For research correspondence and scientific collaboration.','email':'Email','profiles':'Academic profiles','location':'Moscow, Russia',
 'footer':'Physicist · Oxide thin films & electronic transport','skip':'Skip to content',
 'focus':['SrIrO₃ & Sr₂IrO₄','Epitaxial strain','Oxide spintronics'],
 },
 'ru':{
 'name':'Никита Дубицкий','other':'Nikita V. Dubitskiy','role':'Экспериментальная физика конденсированного состояния',
 'nav':['Главная','Исследования','Публикации','CV','Контакты'],
 'intro':'Тонкие плёнки. Спин-орбитальное взаимодействие. Электронный транспорт.',
 'bio':'Я физик и инженер Института радиотехники и электроники им. В. А. Котельникова РАН в Москве. Исследую эпитаксиальные плёнки иридатов стронция и оксидные гетероструктуры: как кристаллическая структура и локальное химическое окружение связаны с электронным транспортом.',
 'description':'Никита Владимирович Дубицкий — физик, инженер ИРЭ РАН. Плёнки SrIrO₃ и Sr₂IrO₄, спинтроника, электронный транспорт и сверхпроводящие гетероструктуры.',
 'explore':'Об исследованиях','selected':'Избранные публикации','allpapers':'Все публикации','latest':'Новая журнальная статья',
 'thesis':'Магистерская диссертация','thesistitle':'Влияние эпитаксиальных деформаций на структуру и электронный транспорт в тонких плёнках SrIrO₃ с сильным спин-орбитальным взаимодействием',
 'edition':'Переработанная английская версия · НИУ ВШЭ · 2026','read':'Открыть диссертацию','download':'Скачать PDF · 18,8 МБ',
 'afm':'SrIrO₃ на NdGaO₃ · АСМ, 5 × 5 мкм²','figure':'Из магистерской диссертации, рис. 9(c).',
 'question':'Как подложка и локальные дефекты влияют на транспорт в оксиде с сильным спин-орбитальным взаимодействием?',
 'researchbody':'Мои исследования последних лет посвящены связи структуры, локального химического окружения и транспорта в эпитаксиальных плёнках SrIrO₃. В магистерской диссертации сравниваются плёнки, выращенные методом ВЧ-магнетронного распыления на пяти подложках: SrTiO₃, NdGaO₃, LSAT, LaAlO₃ и PMN–PT.',
 'topics':[
 ('Эпитаксиальный рост и структура','Серия плёнок толщиной около 35 нм охватывает сжимающее и растягивающее рассогласование решёток. Рентгеновская дифракция подтверждает ориентированную орторомбическую перовскитную фазу; АСМ показывает различия морфологии поверхности на разных подложках.'),
 ('Химическое окружение и спин-орбитальное взаимодействие','РФЭС позволяет исследовать химическое состояние иридия, спин-орбитальное расщепление уровней Ir 4f и приповерхностное кислородное окружение. Структурные и спектроскопические данные помогают интерпретировать зависимость транспорта от подложки.'),
 ('Электронный транспорт и эффект Холла','Измерения сопротивления в диапазоне 4,2–300 К дополняются холловскими измерениями при 2 и 10 К в полях до ±7 Тл. Знак холловского отклика зависит от подложки, что согласуется с изменением вкладов электронов и дырок в многозонном полуметалле.'),
 ('Электрическое управление деформацией','В структуре SrIrO₃/PMN–PT напряжение до 300 В вызывает изменение сопротивления при комнатной температуре примерно на 0,022 %. Отклик согласуется с вкладом передачи пьезоэлектрической деформации от подложки.')],
 'methods':'Экспериментальные методы','methodlist':[('Рост плёнок','ВЧ-магнетронное распыление'),('Структура и морфология','XRD, карты обратного пространства, АСМ'),('Химическое состояние','Рентгеновская фотоэлектронная спектроскопия'),('Транспорт','Низкотемпературное сопротивление, эффект Холла, магнитотранспорт'),('Анализ','Python, Origin, MAUD; аппроксимация и оценка неопределённостей')],
 'interpretation':'Кондо-подобный вклад в диссертации рассматривается как феноменологическое описание и сам по себе не доказывает наличие магнитных центров рассеяния. Знак эффекта Холла в многозонном материале не определяет отдельно концентрации электронов и дырок.',
 'series':'АСМ плёнок SrIrO₃ на (a) LSAT, (b) STO, (c) NGO, (d) LAO и (e) PMN–PT; (f) подложка PMN–PT без плёнки. У каждой панели своя шкала высоты. Оригинальный рисунок из английской версии диссертации, рис. 9, с. 24 (с. 29 PDF).',
 'pubintro':'Журнальные статьи и расширенные тезисы конференции. DOI ведут на опубликованные версии; рукопись arXiv приведена дополнительной ссылкой к соответствующей статье.',
 'search':'Поиск по названию, авторам или журналу','year':'Фильтр по году','all':'Все годы','empty':'По вашему запросу публикаций нет.','count':'публикаций',
 'article':'Журнальная статья','conference':'Расширенные тезисы конференции','preprint':'Ранняя рукопись в arXiv (2025)',
 'cvintro':'Образование, исследовательский опыт и экспериментальные навыки.','experience':'Исследовательский опыт','engineer':'Инженер','institute':'Институт радиотехники и электроники им. В. А. Котельникова РАН','lab':'Лаборатория № 233 · Москва','present':'настоящее время',
 'work':'Рост эпитаксиальных оксидных плёнок, структурные и спектроскопические исследования, измерения электронного транспорта.',
 'education':'Образование','master':'Магистратура по физике','bachelor':'Бакалавриат','hse':'НИУ ВШЭ · Факультет физики','mirea':'РТУ МИРЭА',
 'awards':'Научные конференции и награды','awardlist':['Призёр VI Студенческой конференции «От ядер галактик до атомных масштабов», НИУ ВШЭ (2024).','Диплом призёра II степени 66-й Всероссийской научной конференции МФТИ (2024).'],
 'print':'Печать / сохранить в PDF','languages':'Языки','languageval':'Русский · Английский','contactintro':'Для обсуждения исследований и научного сотрудничества.','email':'Электронная почта','profiles':'Научные профили','location':'Москва, Россия',
 'footer':'Физик · Оксидные плёнки и электронный транспорт','skip':'Перейти к содержимому',
 'focus':['SrIrO₃ и Sr₂IrO₄','Эпитаксиальные деформации','Оксидная спинтроника'],
 }}

PAGES=['home','research','publications','cv','contact','conferences']
def path(lang,page):
 return ('/ru/' if lang=='ru' else '/')+('' if page=='home' else page+'/')
def a(url,label,cls=''):
 label=label.replace('↗','<svg class="external-icon" aria-hidden="true" viewBox="0 0 16 16"><path d="M4 12 12 4M4 4h8v8"/></svg>')
 return f'<a href="{esc(url,quote=True)}"'+(f' class="{cls}"' if cls else '')+f'>{label}</a>'
import content as editorial
editorial.enrich(TEXT,PAPERS)
def body(lang,page):
 return editorial.body(lang,page,TEXT,PAPERS,a,path,PROFILES)

def render(lang,page,content=None,slug=None):
 t=TEXT[lang];idx=PAGES.index(page);route=path(lang,page)
 labels={'en':{'home':'Physicist · IRE RAS','research':'Oxide thin-film research','publications':'Scientific publications','cv':'Education & research experience','contact':'Contact & academic profiles'},'ru':{'home':'физик · ИРЭ РАН','research':'Исследования оксидных тонких плёнок','publications':'Научные публикации','cv':'Образование и научный опыт','contact':'Контакты и научные профили'}}
 labels['ru']['conferences']='Конференции и научные доклады';labels['en']['conferences']='Conferences and scientific contributions'
 title=t['name']+' — '+labels[lang][page]
 desc={'conferences':('Конференции и доклады Никиты Дубицкого: МИРЭА, МФТИ, НИУ ВШЭ, МИФИ. Темы исследований, тезисы и награды.' if lang=='ru' else 'Conferences and contributions by Nikita Dubitskiy: MIREA, MIPT, HSE and MEPhI. Research topics, proceedings and awards.'),'home':t['description'],'research':('SrIrO₃ and Sr₂IrO₄ thin films, electronic transport and Josephson heterostructures. Research by Nikita Dubitskiy at Kotelnikov IRE RAS.' if lang=='en' else 'Исследования Никиты Дубицкого: плёнки SrIrO₃ и Sr₂IrO₄, электронный транспорт, спинтроника и джозефсоновские гетероструктуры. ИРЭ РАН.'),'publications':('Scientific publications by Nikita V. Dubitskiy: oxide thin films, spin–orbit coupling and electronic transport. Journal articles with DOI and thesis.' if lang=='en' else 'Научные публикации Никиты Владимировича Дубицкого: оксидные плёнки, спин-орбитальное взаимодействие и электронный транспорт. Статьи с DOI и диссертация.'),'cv':('Nikita Dubitskiy: research engineer at Kotelnikov IRE RAS, master’s degree in Physics from HSE University. Education, experience and experimental methods.' if lang=='en' else 'Никита Дубицкий: инженер ИРЭ РАН, магистр физики НИУ ВШЭ. Образование, научный опыт, экспериментальные методы и награды.'),'contact':('Contact physicist Nikita Dubitskiy at Kotelnikov IRE RAS, Moscow. Email, ORCID, Google Scholar, ResearchGate and CoLab.' if lang=='en' else 'Контакты физика Никиты Владимировича Дубицкого, ИРЭ РАН, Москва. Электронная почта, ORCID, Google Scholar, ResearchGate и CoLab.')}[page]
 if slug:
  note=details.NOTES[slug][lang];route=details.route(lang,slug,path);title=note['short']+' — '+t['name'];desc=note['description']
 graph=structured_data.graph(BASE,lang,'detail' if slug else page,route,title,desc,TEXT,PROFILES,PAPERS,editorial.LAB,editorial.NTO)
 if slug:
  item=details.entity(lang,slug,PAPERS,TEXT,BASE);graph.append(item)
  graph[1]['mainEntity']={'@id':item['@id']};graph[1]['about']=[{'@id':BASE+'/#nikita-dubitskiy'},{'@id':item['@id']}]
 if page!='home':graph.append({'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':t['nav'][0],'item':BASE+path(lang,'home')},{'@type':'ListItem','position':2,'name':t['nav'][idx],'item':BASE+route}]})
 if slug:graph[-1]['itemListElement'].insert(1,{'@type':'ListItem','position':2,'name':t['nav'][idx],'item':BASE+path(lang,page)});graph[-1]['itemListElement'][-1].update(position=3,name=note['short'])
 nav=''.join(f'<a href="{path(lang,p)}"'+(' class="active" aria-current="page"' if p==page else '')+f'>{t["nav"][i]}</a>' for i,p in enumerate(PAGES))
 verification=''.join(f'<meta name="{name}" content="{esc(str(CONFIG.get(key,"")),quote=True)}">' for name,key in [('yandex-verification','yandex_verification'),('google-site-verification','google_site_verification')] if CONFIG.get(key))
 crumb='' if page=='home' else '<div class="breadcrumbs">'+a(path(lang,'home'),t['nav'][0])+f'<span aria-hidden="true">/</span><span>{t["nav"][idx]}</span></div>'
 if slug:crumb='<div class="breadcrumbs">'+a(path(lang,'home'),t['nav'][0])+'<span aria-hidden="true">/</span>'+a(path(lang,page),t['nav'][idx])+'<span aria-hidden="true">/</span><span>'+esc(note['short'])+'</span></div>'
 language_route=lambda language:details.route(language,slug,path) if slug else path(language,page)
 extra=details.metadata(lang,slug,PAPERS,TEXT,BASE) if slug else ''
 return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{esc(title)}</title><meta name="description" content="{esc(desc,quote=True)}"><meta name="author" content="Nikita V. Dubitskiy"><meta name="theme-color" content="#eef2f6"><meta name="color-scheme" content="light dark"><script src="/assets/theme.js"></script>{verification}{extra}<meta name="robots" content="max-image-preview:large">
<link rel="canonical" href="{BASE+route}"><link rel="alternate" hreflang="en" href="{BASE+language_route('en')}"><link rel="alternate" hreflang="ru" href="{BASE+language_route('ru')}"><link rel="alternate" hreflang="x-default" href="{BASE+language_route('en')}">
<meta property="og:type" content="website"><meta property="og:title" content="{esc(title,quote=True)}"><meta property="og:description" content="{esc(desc,quote=True)}"><meta property="og:url" content="{BASE+route}"><meta property="og:site_name" content="Nikita Dubitskiy"><meta property="og:locale" content="{'ru_RU' if lang=='ru' else 'en_US'}"><meta property="og:locale:alternate" content="{'en_US' if lang=='ru' else 'ru_RU'}"><meta property="og:image" content="{BASE}/assets/social.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Nikita Dubitskiy — experimental condensed matter physics"><meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="/assets/fonts/GolosText.woff" as="font" type="font/woff" crossorigin><link rel="icon" type="image/svg+xml" href="/assets/favicon.svg"><link rel="stylesheet" href="/assets/site.css"><link rel="stylesheet" href="/assets/design.css"><script defer src="/assets/site.js"></script><script type="application/ld+json">{json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False)}</script></head>
<body class="page-{page}"><a class="skip-link" href="#main">{t['skip']}</a><div class="site-shell"><header class="site-header"><a class="brand" href="{path(lang,'home')}" aria-label="{t['name']}"><span class="monogram" aria-hidden="true">ND<span>.</span></span><span class="brand-name">{t['name']}<span>{'Physicist · IRE RAS' if lang=='en' else 'Физик · ИРЭ РАН'}</span></span></a><div class="header-tools"><button class="theme-toggle" type="button" hidden aria-label="{'Сменить тему' if lang=='ru' else 'Toggle theme'}"><span aria-hidden="true">◐</span><span class="theme-label">{'Тема' if lang=='ru' else 'Theme'}</span></button><div class="language-switch" aria-label="{'Language' if lang=='en' else 'Язык'}">{a(language_route('en'),'EN','current' if lang=='en' else '')}<span aria-hidden="true">/</span>{a(language_route('ru'),'RU','current' if lang=='ru' else '')}</div></div></header><nav class="main-nav" aria-label="{'Main navigation' if lang=='en' else 'Основное меню'}">{nav}<span class="nav-signature" aria-hidden="true">5d / SrIrO₃</span></nav><main id="main">{crumb}{content if content is not None else body(lang,page)}</main><footer class="site-footer"><div><strong>{t['name']}</strong><p>{t['footer']}</p></div><div>{a('mailto:nikita.dubitskiy@gmail.com','nikita.dubitskiy@gmail.com')}<p>{t['location']}</p></div></footer></div><dialog class="image-dialog"><button class="close-image" type="button" aria-label="{'Закрыть изображение' if lang=='ru' else 'Close image'}">×</button><img alt=""><p></p></dialog></body></html>'''

def build():
 for lang in TEXT:
  for page in PAGES:
   target=ROOT/path(lang,page).lstrip('/')/'index.html';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(render(lang,page),encoding='utf-8')
 for lang in TEXT:
  for slug,note in details.NOTES.items():
   target=ROOT/details.route(lang,slug,path).lstrip('/')/'index.html';target.parent.mkdir(parents=True,exist_ok=True)
   target.write_text(render(lang,note['parent'],details.content(lang,slug,PAPERS,TEXT,a,path),slug),encoding='utf-8')
 citations.build(ROOT,PAPERS,details.NOTES)
 notfound=render('en','home','<header class="page-heading"><p class="eyebrow">404</p><h1>Page not found</h1><p>The page may have moved.</p><a class="button" href="/">Back to home →</a></header>').replace('<link rel="canonical" href="'+BASE+'/">','<meta name="robots" content="noindex">')
 notfound=re.sub(r'<script type="application/ld\+json">.*?</script>', '', notfound)
 notfound=re.sub(r'<link rel="alternate"[^>]*>', '', notfound)
 (ROOT/'404.html').write_text(notfound,encoding='utf-8')
 ns='http://www.sitemaps.org/schemas/sitemap/0.9';xn='http://www.w3.org/1999/xhtml';im='http://www.google.com/schemas/sitemap-image/1.1'
 for prefix,uri in [('',ns),('xhtml',xn),('image',im)]:ET.register_namespace(prefix,uri)
 root=ET.Element('{'+ns+'}urlset')
 routes=[(lang,page,None) for lang in TEXT for page in PAGES]+[(lang,n['parent'],slug) for lang in TEXT for slug,n in details.NOTES.items()]
 for lang,page,slug in routes:
  current=lambda language:details.route(language,slug,path) if slug else path(language,page)
  u=ET.SubElement(root,'{'+ns+'}url');ET.SubElement(u,'{'+ns+'}loc').text=BASE+current(lang)
  for language in ['en','ru','x-default']:
   ET.SubElement(u,'{'+xn+'}link',{'rel':'alternate','hreflang':language,'href':BASE+current('en' if language=='x-default' else language)})
  if page=='home' and not slug:
   img=ET.SubElement(u,'{'+im+'}image');ET.SubElement(img,'{'+im+'}loc').text=PORTRAIT
   ET.SubElement(img,'{'+im+'}title').text=TEXT[lang]['name']+' — '+('physicist' if lang=='en' else 'физик')
 ET.indent(root,space='  ')
 ET.ElementTree(root).write(ROOT/'sitemap.xml',encoding='utf-8',xml_declaration=True)
 (ROOT/'sitemap.txt').write_text(''.join(u.find('{'+ns+'}loc').text+'\n' for u in root),encoding='utf-8')
 (ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+BASE+'/sitemap.xml\nSitemap: '+BASE+'/sitemap.txt\n')
 (ROOT/'.nojekyll').touch()
 print('Built',len(routes),'bilingual pages, bibliography downloads, 404 and sitemaps')
if __name__=='__main__':build()
