import requests
payload = {'eventId': 'fralu9obsuffge6il7dn14aels','calendarId':'sahid.rojas64@gmail.com'}
headers = {'content-type': 'application/json',
 'Authorization': 'Bearer ya29.a0Ae4lvC3YDxVvQBn57SlXft2vZ1bmFGJlHwlV8xDZaW7eCdrQwsr6C5wmzgBJ3KfmtAbNtDBnJBBcp9Q3Zk4H3bfr_VGreIFLYiMplsjhkOD5vK9qBmPvQ2LEhOCp0j7XUPlSR9xu6R_8Z197G1yAGi6QW0YFNEOE1Qsx'
 }
url='https://www.googleapis.com/calendar/v3/calendars/calendarId/events/eventId'
response = requests.get(url,params=payload,headers=headers)


response.raise_for_status()
print(response.json())
