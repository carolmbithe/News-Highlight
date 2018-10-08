import urllib.request,json
from .models import Source

# Source = source.Source
api_key = None
base_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWSHIGHLIGHT_API_KEY']
    base_url = app.config["NEWSHIGHLIGHT_API_BASE_URL"]


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
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')


        source_object = Source(name,description,url,category,language)
        source_results.append(source_object)

        # print(source_list)

    return source_results

def get_source():
    """
    Function that gets the json response to our url request
    """

    get_source_details_url = base_url.format(api_key)

    with urllib.request.urlopen(get_source_details_url) as url:
        source_details_data = url.read()
        source_details_response = json.loads(source_details_data)

        source_object = None

        if source_details_response:
            name = source_details_response.get('name')
            description = source_details_response.get('description')
            url = source_details_response.get('url')
            category = source_details_response.get('category')
            language = source_details_response.get('language')

            source_object = Source(name,description,url,category,language)

        return source_object
# def get_article(id):
       
