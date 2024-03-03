import wikipedia


def get_info(given_page):
    try:
        page = wikipedia.page(given_page)
        summary = page.summary
        url = page.url
        return summary, url
    except wikipedia.exceptions.PageError:
        return "Page no found"


def ui():
    page = input('Enter name of the page: ')
    summary, url = get_info(page)
    print('Summary:', summary)
    print('URL:', url)


ui()
