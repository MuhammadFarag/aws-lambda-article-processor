def inspect_empty_author(article, context):
    if len(article['author']) == 0:
        article['errors'].append('No_Author')
        return article
    else:
        return article


def content_length(article, context):
    article['length'] = len(article['content'].split(' '))
    return article


def pump_rating(article, context):
    article['rating'] = article['rating'] + 5
    return article


def capitalize_author_name(article, context):
    article['author'] = article['author'].title()
    return article
