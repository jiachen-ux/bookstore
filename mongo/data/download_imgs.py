import requests
import json

def download_img_url(image_url):
    img_data = requests.get(image_url).content
    img_name = image_url.split('/')[-1]
    with open('images/' + img_name, 'wb') as handler:
        handler.write(img_data)


def read_json_file(filename):
    with open(filename, 'r') as f:
        lst = json.load(f)

    inc = 1
    data = list()
    for obj in lst:

        if 'title' not in obj or 'thumbnailUrl' not in obj:
            continue

        if 'isbn' not in obj:
            obj['isbn'] = ""
        if 'pageCount' not in obj:
            obj['pageCount'] = 0
        if 'categories' not in obj:
            obj['categories'] = []
        if 'shortDescription' not in obj:
            obj['shortDescription'] = ""

        d = {
            '_id': inc,
            'title': obj['title'],
            'thumbnailUrl': obj['thumbnailUrl'],
            'isbn': obj['isbn'],
            'pageCount': obj['pageCount'],
            'shortDescription': obj['shortDescription'],
            'categories': obj['categories'],
            'authors': obj['authors']
        }

        data.append(d)

        inc += 1
    
    return data

def get_all_img_urls(data):
    urls = list(map(lambda t : t['thumbnailUrl'], data))

    saw = set()
    for url in urls:
        download_img_url(url)
        # img = url.split('/')[-1]
        # if img in saw:
        #     print("SAW THIS IMG " + img)
        # saw.add(img)


def write_to_json(data):
    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def correct_img_path(o):
    img_name = o['thumbnailUrl'].split('/')[-1]
    o['thumbnailUrl'] = 'images/' + img_name
    return o

data = read_json_file("amazon.books.json")
data_corrected = list(map(correct_img_path, data))
write_to_json(data_corrected)