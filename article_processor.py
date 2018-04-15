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


def naive_merge_capitalized_author_and_pumped_rating(articles, context):
    a1, a2 = articles
    if a1['rating'] > a2['rating']:
        return {"author": a2['author'], "content": a1['content'], "rating": a1['rating'], "errors": a1['errors']}
    else:
        return {"author": a1['author'], "content": a2['content'], "rating": a2['rating'], "errors": a2['errors']}
