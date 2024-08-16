import requests as r
from zlib import crc32

from bs4 import BeautifulSoup

from program_info_manager import mission_guide_url, old_file_hash, competition_website, set_new_file_hash


def get_mission_guide_page():
    """
    parses the pages and checks if the mission guide has been changed

    Returns:
        Bool: True if file has changed, False if the file is the same,
    """

    # get request to get the page info in html
    response = r.get(mission_guide_url)

    # load the page html data into a html parser
    html_page = BeautifulSoup(response.text, 'html.parser')

    # find all hyperlink tags in the page
    hyperlinks_in_html_page = html_page.find_all('a')

    # loop through all <a> tags to find the document link
    for tag in hyperlinks_in_html_page:
        if "Competition Mission Guide" in tag.text:

            # concatenating the hyperlink to the main website url
            mission_guide_pdf_url = competition_website + tag['href']
            break

    # get request the mission guide document as a response string
    file_data = r.get(mission_guide_pdf_url).text

    # hash the response to be used for comparison with previous versions
    new_file_hash = crc32(file_data.encode())

    if new_file_hash == old_file_hash:
        return {"has_file_changed": False, "mission_guide_pdf_url": mission_guide_pdf_url}
    else:
        set_new_file_hash(new_file_hash)
        return {"has_file_changed": True, "mission_guide_pdf_url": mission_guide_pdf_url}
