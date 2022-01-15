import requests

img_url = 'https://m.media-amazon.com/images/I/71xtuRugCvL._SL1500_.jpg'


def download(url):
    try:
        response = requests.get(url=url)
        with open('req_img.jpg', 'wb') as file:
            file.write(response.content)
        return 'dl is done'
    except Exception as ex:
        return 'dn is not done'


def main():
    print(download(url=img_url))


if __name__ == '__main__':
    main()
