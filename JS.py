import requests
import os

Directory = "/home/rajat/Scrapping/JS/Data/"
url = "https://www.jeevansathi.com/search/advanceSearch/1291861690/"
payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "2bbd9d2d-2cfa-4674-ba62-57e7a9675fa5",
    "cache-control":"no-cache",
    "Postman-Token":"d0f7b55d-1db8-4b85-a4fd-0bf479e971c5",
    "User-Agent":"PostmanRuntime/7.6.0",
    "Accept":"*/*",
    "Host":"www.jeevansathi.com",
    "cookie":"ak_bmsc=7D8BC855A90FD1672132E9C959F13B60170BD71C6D1200004E00D05C5D822751~pl2ppAusK9wH5IbtuK2F+X7sl3i33Pj5vhER6Xs1TV79fUZjA78biGaDElstWOgLENImM+sB8R8tNkfeUWzIjjlAUntNb9uz/hJjLznHO4mR+1jkWiKYMVzCloyHZQY2CIAuYLViyxiVnblTFvbIRRoM41BTz2bTsbTJfeBbt1jH1prfJBaJPP1sex75Fd7PP/kHu/A0d8IzWOjb/UtmVm2LCdsMbLW2/HznjBh6RaQoo=; JS_MOBILE=N; JS_TABLET_MOBILE=N; JSSearchId=1291861690",
    "accept-encoding":"gzip, deflate"
    }


def scrap_from_to(Directory, url, _from, _to):

    for i in range(_from, _to):
        response = requests.request("GET", url + str(i), data=payload, headers=headers)
        with open(os.path.join(Directory, str(i)), "w") as f:
            f.writelines(response.text)


scrap_from_to(Directory, url, 1, 6000)