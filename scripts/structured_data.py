"""Connected entities for the public, bilingual academic profile.

Only describe visible, sourced content. This is not an indexing submission or
a request for a knowledge panel. Publication author lists may be abbreviated.
"""

def graph(base, lang, page, route, title, description, text, profiles, papers, lab, nto):
    person_id = base + '/#nikita-dubitskiy'
    website_id = base + '/#website'
    portrait_id = base + '/#portrait'
    institute_id = 'http://www.cplire.ru/#organization'
    lab_id = lab + '#organization'
    person = {
        '@type': 'Person', '@id': person_id,
        'name': text[lang]['name'],
        'alternateName': ['Nikita V. Dubitskiy', 'Nikita Dubitskiy',
                          'Nikita Vladimirovich Dubitskiy', 'Никита Дубицкий',
                          'Никита Владимирович Дубицкий'],
        'url': base + '/', 'identifier': 'https://orcid.org/0009-0003-1723-8103',
        'description': text[lang]['description'],
        'jobTitle': 'Инженер' if lang == 'ru' else 'Research engineer',
        'sameAs': list(profiles.values()), 'image': {'@id': portrait_id},
        'worksFor': {'@id': institute_id}, 'affiliation': {'@id': lab_id},
        'alumniOf': [
            {'@type': 'CollegeOrUniversity', 'name': 'HSE University', 'url': 'https://www.hse.ru/'},
            {'@type': 'CollegeOrUniversity', 'name': 'MIREA — Russian Technological University', 'url': 'https://www.mirea.ru/'}],
        'knowsAbout': ['Condensed matter physics', 'Epitaxial thin films',
                      'SrIrO3', 'Sr2IrO4', 'Electronic transport', 'Spintronics']
    }
    web = {
        '@type': 'ProfilePage' if page in ('home', 'cv') else 'WebPage',
        '@id': base + route + '#webpage', 'url': base + route,
        'name': title, 'description': description, 'inLanguage': lang,
        'isPartOf': {'@id': website_id}, 'about': {'@id': person_id},
        'primaryImageOfPage': {'@id': portrait_id}
    }
    if page in ('home', 'cv'):
        web['mainEntity'] = {'@id': person_id}
        person['subjectOf'] = {'@type': 'Article', 'url': nto,
                               'headline': 'Никита Дубицкий (Москва)',
                               'inLanguage': 'ru', 'about': {'@id': person_id}}
    result = [person, web, {
        '@type': 'WebSite', '@id': website_id, 'url': base + '/',
        'name': 'Nikita Dubitskiy', 'alternateName': 'Никита Дубицкий',
        'inLanguage': ['en', 'ru'], 'publisher': {'@id': person_id},
        'about': {'@id': person_id}
    }, {
        '@type': 'ResearchOrganization', '@id': institute_id,
        'name': text[lang]['institute'], 'url': 'http://www.cplire.ru/',
        'department': {'@id': lab_id}
    }, {
        '@type': 'ResearchOrganization', '@id': lab_id,
        'name': 'Лаборатория № 233 ИРЭ РАН' if lang == 'ru' else 'Laboratory No. 233, IRE RAS',
        'url': lab, 'parentOrganization': {'@id': institute_id}
    }, {
        '@type': 'ImageObject', '@id': portrait_id,
        'contentUrl': base + '/assets/nikita-dubitskiy.jpg',
        'url': base + '/assets/nikita-dubitskiy.jpg',
        'width': 1254, 'height': 1254, 'caption': text[lang]['name'],
        'about': {'@id': person_id}
    }]
    selected = papers if page == 'publications' else [papers[i] for i in (0, 8, 2)] if page == 'home' else []
    article_refs = []
    for paper in selected:
        article_id = 'https://doi.org/' + paper['doi']
        authors = []
        for name in paper['authors'].replace(' et al.', '').split(', '):
            authors.append({'@id': person_id} if 'Dubitskiy' in name else {'@type': 'Person', 'name': name})
        result.append({
            '@type': 'ScholarlyArticle', '@id': article_id,
            'headline': paper['title'], 'url': paper['url'],
            'identifier': {'@type': 'PropertyValue', 'propertyID': 'DOI', 'value': paper['doi']},
            'author': authors, 'isPartOf': {'@type': 'Periodical', 'name': paper['journal']}
        })
        article_refs.append({'@id': article_id})
    if page == 'publications':
        list_id = base + route + '#publications'
        web['mainEntity'] = {'@id': list_id}
        result.append({'@type': 'ItemList', '@id': list_id,
                       'numberOfItems': len(article_refs),
                       'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'item': ref}
                                           for i, ref in enumerate(article_refs)]})
    elif article_refs:
        web['hasPart'] = article_refs
    return result
