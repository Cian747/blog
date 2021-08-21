from app.models.quotes import Quotes
import urllib.request,json


quote_url = None


def configure_request(app):
    global quote_url
    quote_url = app.config['QUOTE_BASE_URL']



def get_quote():
    '''
    Function that gets the json response to our url request
    '''
    # get_news_url = quote_url

    # with urllib.request.urlopen(get_news_url) as url:
    #     get_quote_data = url.read()
    #     get_quote_response = json.loads(get_quote_data)

    #     quote_results = None

    #     quote_results = process_results(get_quote_response)


    # return quote_results


def process_results(quote_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    quote_results = []
    for quote_item in quote_list:
        author = quote_item.get('author')
        quote = quote_item.get('quote')

        quote_object = Quotes(author,quote)
        quote_results.append(quote_object)

    return quote_results

