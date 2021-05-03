def make_soup(url):
    '''
    This helper function takes in a url and requests and parses HTML
    returning a soup object.
    '''
    headers = {'User-Agent': 'Codeup Data Science'} 
    response = requests.get(url, headers=headers)    
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    return soup

def get_blog_articles(urls, cached=False):
    '''
    This function takes in a list of blog urls from Codeup and a parameter
    with default cached == False. This function scrapes the title and texts for each  of the urls, 
    and then creates a list of dictionaries with the title and text for each blog.

    '''
   

    # Create an empty list to hold dictionaries
    articles = []

        # Loop through each url in our list of urls
    for url in urls:

            # Make request and soup object using helper
            soup = make_soup(url)

            # Save the title of each blog in variable title
            title = soup.find('h1').text

            # Save the text in each blog to variable text
            content = soup.find('div', class_="jupiterx-post-content").text

            # Create a dictionary holding the title and content for each blog
            article = {'title': title, 'content': content}

            # Add each dictionary to the articles list of dictionaries
            articles.append(article)
            
       

       
    
    return articles