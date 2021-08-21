from app.models.quotes import Quote
import urllib.request,json


quote_url = None


def configure_request(app):
    global quote_url
    quote_url = app.config['QUOTE_BASE_URL']


def get_quote():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = quote_url

    with urllib.request.urlopen(get_news_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

    if get_quote_response:
        author  = get_quote_response.get('author')
        quote  = get_quote_response.get('quote')

        quote = Quote(author, quote)
        return quote
    else:
        author = 'Eric(TheHipHopPreacher)'
        quote = 'Be phenomenal or be forgotten'
        
        quote = Quote(author, quote)
        return quote




