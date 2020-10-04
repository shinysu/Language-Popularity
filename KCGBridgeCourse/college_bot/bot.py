from webutils import get_content_from_url, get_links_from_page, get_content_by_class, get_content_by_tags
url = "https://kcgcollege.ac.in"

def get_related_links(url, term):
    html = get_content_from_url(url)
    link = list(set(get_links_from_page(html, term)))
    return link

def get_club_info():
    link = get_related_links(url, 'club')[0]
    club_data = get_content_from_url(link)
    content = get_content_by_class(club_data, 'vc_tta-panel-title')
    return content[1:]


def get_department_info():
    link = get_related_links(url, 'department')[0]
    department_data = get_content_from_url(link)
    department_name = get_content_by_tags(department_data,'h2')
    return department_name[:len(department_name)-1]


def get_hostel_info():
    link = get_related_links(url, 'hostel')[0]
    hostel_data = get_content_from_url(link)
    hostel_details = get_content_by_tags(hostel_data,'p')
    return hostel_details

def get_facilities_info():
    facilities = []
    links = get_related_links(url, 'facilities')
    for link in links:
        facility_data = get_content_from_url(link)
        names = get_content_by_tags(facility_data, 'h2')
        facilities.extend(names)
    return facilities

def bot_reply(content):
    for data in content:
        if data:
            print(data)

bot_dict = {'departments':get_department_info, 'hostel':get_hostel_info, 'facilities':get_facilities_info,
            'clubs': get_club_info}

if __name__ == '__main__':
    print("Hello, I am the chabot for KCG College of Technology")
    while True:
        search_word = input("What would you like to know about?\ndepartments\nhostel\nfacilities\nclubs\nexit\n")
        if search_word == 'exit':
            break
        elif search_word in bot_dict:
            content = bot_dict[search_word]()
            bot_reply(content)
        else:
            print("Please enter a valid item")