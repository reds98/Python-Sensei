import requests
response = requests.get(
    url='https://www.googleapis.com/calendar/v3/users/me/calendarList',
    headers={
        'Authorization': 'Bearer ya29.a0Ae4lvC3v9xMvwYn06Hx0H9pbvkZP2tQU2lc_frNlpnNOfao7KbrA6hkOCas3pOF7Rd2zcNcHEUIF9guge_NWaI5pIM9Cl3_3uFbG2GVwCF52c8Tk4Po-vxZHf19fHZ79dAkUKu8KJJTRJpgXY2MEbgoltP_IVcaESJWk',
    },
)

response.raise_for_status()
print(response.json())
