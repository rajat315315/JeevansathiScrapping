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
    "cookie":"ak_bmsc=688D2F920BE1E68AE1B80CDA6279494217417C2A4D3F0000F52FD05C2723D310~plf2xBDOPI1ne08x06KGfS2+pFViNReeVvCFKyckurZTybRMtj2C+f9NAy3Pm8DCpi7r0b4jmeZxVacyO3f4etCXVGS8Gt2Vz3Am3Ff8ZYYYTf2FOtwMB5ymcG4RetN3LqV20RDTLdPRD2hIyjoDrHf1wRxCNsaQgQf3FtcjkSf2Pj3kM06XxE6SRpYN9QibNS1WACKPovAHgs4I9q37hLX+gmD0RnB6ZKh1Amhrmrnj0=; JS_MOBILE=N; JS_TABLET_MOBILE=N; JSSearchId=1291861690",
    "accept-encoding":"gzip, deflate"
    }


def scrap_from_to(Directory, url, _from, _to):

    for i in range(_from, _to):
        response = requests.request("GET", url + str(i), data=payload, headers=headers)
        with open(os.path.join(Directory, str(i)), "w") as f:
            f.writelines(response.text)


scrap_from_to(Directory, url, 1, 6000)