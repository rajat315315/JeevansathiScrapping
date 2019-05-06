

#Sample Profile ----------------------------------

# "profilechecksum": "e1ddc7d92934629c776c47c11112e60ci22898135",
# "userloginstatus": "Last Online today",
# "subscription_text": "eAdvantage",
# "subscription_icon": "eAdvantage",
# "age": "26 Years",
# "username": "YVYV0863",
# "height": "5' 4\" ",
# "occupation": "Analyst",
# "caste": "Sunni",
# "income": "Rs. 15 - 20lac",
# "mtongue": "Urdu",
# "edu_level_new": "M.A, B.A",
# "location": "New Delhi",
# "photo": {
#     "label": "Login to view photo",
#     "url": "https://static.jeevansathi.com/images/picture/450x450_f.png?noPhoto",
#     "action": "Login"
# },
# "album_count": "0",
# "timetext": null,
# "seen": "Y",
# "religion": "Muslim",
# "gender": "F",
# "featured": null,
# "filter_score": "",
# "filter_reason": "",
# "highlighted": 0,
# "verification_seal": null,
# "verification_status": null,
# "mstatus": "Never Married",
# "college": "Lady Shri Ram College for Women",
# "pg_college": "Delhi School Of Economics",
# "company_name": null,
# "gunascore": null,
# "name_of_user": null,
# "profileid": "22898135",
# "thumbnail_pic": null,
# "availforchat": false,
# "complete_verification_status": null,
# "last_active_before": 894240,
# "online": false,

import re
import os
import json
import pandas as pd
import pickle

Columns = ['userloginstatus', 'subscription_text', 'age', 'height', 'occupation', 'caste', 'income', 'mtongue', 'edu_level_new', 'album_count', 'religion', 'gender',
           'mstatus', 'college', 'pg_college', 'company_name', 'last_active_before']
Directory = "/home/rajat/Scrapping/JS/Data/"

def convert_to_single_pickle(Data_Directory, _from, _to):


    main_json = []
    for i in range(_from, _to):
        if i in [2960, 1984, 1985]:
            continue
        with open(os.path.join(Data_Directory, str(i)), "r") as f:
            read = f.read()
            matched = re.findall(r'var response = (.*);', read)
            loaded = json.loads(matched[0])['profiles']

            if i == 1:
                main_json = loaded
            else:
                main_json = main_json + loaded

    df = pd.DataFrame(main_json)
    df.to_pickle(os.path.join(Data_Directory, "data_pickled"))


convert_to_single_pickle(Directory, 1, 6000)