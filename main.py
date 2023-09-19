import requests
from datetime import datetime

Pixela_Endpoint = "https://pixe.la/v1/users"
username = "********"
Pixela_Token = "************"

user_parameters = {

    "token": Pixela_Token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# Account created
# response = requests.post(url=Pixela_Endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{Pixela_Endpoint}/{username}/graphs"

graph_parameters = {
    "id": "habit-graph",
    "name": "x-enlargment",
    "unit": "minutes",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": Pixela_Token,

}
# graph created
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

add_value_endpoint = f"{Pixela_Endpoint}/{username}/graphs/habit-graph"
# amele yolu benim yaptığım
# raw_date = str(datetime.today())
# raw_date_list =raw_date.split(" ")
# raw_date_list_0 = raw_date_list[0]
# today_list= raw_date_list_0.split("-")
# today= str(today_list[0]+today_list[1]+today_list[2])

# daha iyisi
# manipüle etme yöntemi(date içine veri girme )
today = datetime(year=2023, month=9, day=14 )
#üstteki ile birlikte (içine veri girmeden)alttakini de kullanırsam varolan zamanın içine veri girer. (.now eklemem lazım)
# print(today.strftime("%Y%m%d"))

value_params = {
   "date": today.strftime("%Y%m%d"),
   "quantity":"15",
}
response = requests.post(url=add_value_endpoint, json=value_params, headers=headers )
print(response.text)
