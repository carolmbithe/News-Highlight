class Source:
    """
    Source class to define Source Objects
    """
    def __init__(self,name,description,url,category,language):

        self.name =name
        self.description =description
        self.url =url
        self.category =category
        self.language =language


class Article:
    """
    Source class to define Article Objects
    """
    def __init__(self,source,author,title,description,published_At,content,url,url_to_image):

        self.source =source
        self.author = author
        self.title=title
        self.description =description
        self.published_At=published_At
        self.content=content
        self.url =url
        self.url_to_image=url_to_image
