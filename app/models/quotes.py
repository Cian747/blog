class Quotes:
    '''
    Generate the news in from a a country
    '''

    def __init__(self,author,quote):
        '''
        Initiate the news source class blueprint

        args: 
            author = person that wrote the article
            quote = the quote fetched from the link
        '''     
        self.author = author
        self.quote = quote
