def inspect_empty_author(article):
    if len(article['author']) == 0:
        article['errors'].append('No_Author')
        return article
    else:
        return article
