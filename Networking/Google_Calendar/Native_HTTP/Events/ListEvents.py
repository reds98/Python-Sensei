import requests
payload = {'calendarId':'sahid.rojas64@gmail.com'}
headers = {'content-type': 'application/json',
 'Authorization': 'Bearer ya29.a0AfH6SMBrH3GOvtMu7vflNnRFeDhbml3DxT4EdjSilsYJ9-vycA_fbZ-C46Xx1TlSi7dFiP5xjYA1398AsoudQc0VAPUMk33vIYCV6vxua1VIa_aEwn3DwdtHyb3FUqOO-C-Dh0pOvfP3IKh3Zp5v6W3q993NG4Qlq2Q2'
 }
url='https://www.googleapis.com/calendar/v3/calendars/calendarId/events'
response = requests.get(url,params=payload,headers=headers)

response.raise_for_status()
print(response.json())
