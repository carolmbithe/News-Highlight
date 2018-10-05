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

        newssource_object = Newssource(name)
        newssource_results.append(newssource_object)

        print(newssource_list)

    return newssource_results
