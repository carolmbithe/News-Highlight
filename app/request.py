from app import app
import urllib.request,json
from .models import newssource

Newssource = newssource.Newssource

api_key = app.config['NEWSHIGHLIGHT_API_KEY']

base_url = app.config["NEWSHIGHLIGHT_API_BASE_URL"]

def get_newssource():

    """
    Function that gets the json response to our url request
    """

    get_newssource_url = base_url.format(api_key)

    with urllib.request.urlopen(get_newssource_url) as url:
        get_newssource_data = url.read()
        get_newssource_response = json.loads(get_newssource_data)

        newssource_results = None

        if get_newssource_response['sources']:
            newssource_results_list = get_newssource_response['sources']
            newssource_results = process_results(newssource_results_list)

    return newssource_results

def process_results(newssource_list):

    """
    Function that proceeses that the sources result and transform them to a list of Objects

    Args:
    newssource_list:A list of dictionaries that contain newssource details

    Returns:
        newssource_results:A list of newssource Objects
    """

    newssource_results=[]

    for newssource_item in newssource_list:
        name = newssource_item.get('name')
        description = newssource_item.get('description')
        url = newssource_item.get('url')
        category = newssource_item.get('category')
        language = newssource_item.get('language')


        newssource_object = Newssource(name,description,url,category,language)
        newssource_results.append(newssource_object)

        # print(newssource_list)

    return newssource_results

def get_source():
    """
    Function that gets the json response to our url request
    """

    get_source_details_url = base_url.format(name,api_key)

    with urllib.request.urlopen(get_source_details_url) as url:
        source_details_data = url.read()
        source_details_response = json.loads(source_details_data)

        newssource_object = None

        if source_details_response:
            name = source_details_response.get('name')
            description = source_details_response.get('description')
            url = source_details_response.get('url')
            category = source_details_response.get('category')
            language = source_details_response.get('language')

            newssource_object = Newssource(name,description,url,category,language)

        return newssource_object
