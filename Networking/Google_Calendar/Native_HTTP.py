
#clientID 329717365176-aqe4dnhufklio4fcbhlg2j498g7gspn4.apps.googleusercontent.com
#secretoCliente kywvUbk_Si_F0mTdv21RzoA8

import requests
response = requests.get(
    url='https://www.googleapis.com/calendar/v3/users/me/calendarList',
    headers={
        'Authorization': 'Bearer ya29.a0Ae4lvC0ErURXkPteWqgwJUp5OPqPXmTvLtJtHSIcw2Z29UmMND7_BYz21ZuT0rOfdad5l51V1Qb_TuOtvoPqdgNFE7UWzCbVX8Li0gCA1AY7YPzJjwERP-rhwRpbmzOI5twuqv63H_ei93JfAz0vqlKZeyROKzkY5QE',
    },
)

response.raise_for_status()
print(response.json())

# import requests
# response = requests.post(
#     url='https://www.googleapis.com/oauth2/v4/token',
#     data={
#         'client_id': '329717365176-aqe4dnhufklio4fcbhlg2j498g7gspn4.apps.googleusercontent.com',
#         'client_secret': '-1OsrUOu_P2Bwa1e-CAX6C_-',
#         'refresh_token': '1//04t3Sd3pr_NKCCgYIARAAGAQSNwF-L9IrqK2EfHExN1debApfXQKz_Q4OccKzPtskMtprCnv7NQZoGmfcDy7HugWxC5_HrbLybC0',
#         'grant_type': 'refresh_token',
#     },
#     headers={
#         'Content-Type': 'application/x-www-form-urlencoded',
#     },
# )
# response.raise_for_status()
# print(response.json().get('access_token'))