def inspect_empty_author(article, context):
    if len(article['author']) == 0:
        article['errors'].append('No_Author')
        return article
    else:
        return article


def content_length(article, context):
    return len(article['content'].split(' '))