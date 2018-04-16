import urllib.request
data_from_user = input()
urllib.request.urlretrieve(data_from_user,"local.html")