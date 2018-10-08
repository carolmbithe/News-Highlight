import urllib.request,json
from .models import Source,Article

# Source = source.Source
api_key = None
base_url = None
base_url_articles=None

def configure_request(app):
    global api_key,base_url,base_url_articles
    api_key = app.config['NEWSHIGHLIGHT_API_KEY']
    base_url = app.config["NEWSHIGHLIGHT_API_BASE_URL"]
    base_url_articles=app.config["NEWSHIGHLIGHT_API_ARTICLE_URL"]


def get_sources():

    """
    Function that gets the json response to our url request
    """

    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results

def process_results(source_list):

    """
    Function that proceeses that the sources result and transform them to a list of Objects

    Args:
    source_list:A list of dictionaries that contain source details

    Returns:
    source_results:A list of source Objects
    """

    source_results=[]

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')



        source_object = Source(id,name,description)
        source_results.append(source_object)

        # print(source_list)

    return source_results

def get_articles(id):
    """
    Function that gets the json response to our url request
    """

    get_articles_url = base_url_articles.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_result_list=get_articles_response['articles']
            articles_results=process_article_results(articles_result_list)
    return articles_results
def process_article_results(articles_list):
    articles_results=[]
    for article_item in articles_list:
        source=article_item.get('source')
        author=article_item.get('author')
        title=article_item.get('title')
        description=article_item.get('description')
        url=article_item.get('url')
        urlToImage=article_item.get('urlToImage')
        publishedAt=article_item.get('publishedAt')
        articles_object = Article(source,author,title,description,publishedAt,url,urlToImage)
        articles_results.append(articles_object)

    return articles_results
