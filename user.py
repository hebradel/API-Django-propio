import requests

if __name__=='__main__':
    url='http://127.0.0.1:5000'
    response=requests.get(url)

    print(response.text)