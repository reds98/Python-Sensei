# Let’s begin by installing the requests library. To do so, run the following command:
# pip install requests

import requests
#With this line you can make a request but the response its no saved in any place
print(requests.get('https://api.github.com'))

# Response is a powerful object for inspecting the results of the request.
response = requests.get('https://api.github.com')

# The first bit of information that you can gather 
# from Response is the status code.
#  A status code informs you of the status of the request.
response.status_code

# .status_code returned a 200, 
# which means your request was successful
#  and the server responded with the data you were requesting.

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

# but there is more that this 2 codes for example
#  204 mean that the response dont have any content or 
# 304 Not modified
 #The next example   you can raise an exception  if the  the request was unsuccessful

from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

#THE CONTENT
#The .content gives you accsess to the raw bytes of the response payload 
print(response.content)
#If you wnat to to convert them into a string using character encoding sucha as UTF-8
#You use access .text
response.text

#Because the decoding of bytes to a str requires an encoding scheme, requests will try to guess the encoding based
# on the response’s headers if you do not specify one.
#But you can provide  an explicit encoding by setting .encoding before accesing .text 

response.encoding = 'utf-8' # Optional: requests infers this internally
response.text

#Almost a lot of the content came in JSON format you can convert the content 
# into JSON like this
response.json()

#HEADERS
#If you want to access the header for getting information  you will use 
#.headers
response.headers

#The .headers return a dictionary object so you can access header values by keys
response.headers['Content-Type']
#Another cool feature is the the headers are not case-sensitive
response.headers['content-type']

#QUERY STRING PARAMETERS

# Search GitHub's repositories for requests
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

# Inspect some attributes of the `requests` repository
#By passing the dictionary {'q': 'requests+language:python'} to the params 
# parameter of .get(), you are able to modify the results 
# that come back from the Search API
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')

#You can pass the  params to get() in the form of a dictionary

requests.get(
    'https://api.github.com/search/repositories',
    params=[('q', 'requests+language:python')],
)

# Request Headers

# To customize headers, you pass a 
# dictionary of HTTP headers to get() using the headers parameter. 
# For example, you can change your previous search request to 
# highlight matching search terms in the results by specifying 
# the text-match media type in the Accept header:
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

# View the new `text-matches` array which provides information
# about your search term within the results
json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')

# The Accept header tells the server what content types your application can handle. 
# In this case, since you’re expecting the matching search terms to 
# be highlighted, you’re using the header
# value application/vnd.github.v3.text-match+json, 
# which is a proprietary GitHub Accept header where the content is a special JSON format.

#Other HTTP Methods
requests.post('https://httpbin.org/post', data={'key':'value'})
requests.put('https://httpbin.org/put', data={'key':'value'})
requests.delete('https://httpbin.org/delete')
requests.head('https://httpbin.org/get')
requests.patch('https://httpbin.org/patch', data={'key':'value'})
requests.options('https://httpbin.org/get')
#For each method, you can inspect their responses in the same way you did before


#The Message Body

# According to the HTTP specification, POST,
# PUT, and the less common PATCH requests pass
# their data through the message body rather than
# through parameters in the query string. Using requests
# , you’ll pass the payload to the corresponding function’s data parameter.

# data takes a dictionary, a list of tuples, bytes,
#  or a file-like object. You’ll want to adapt the data you send 
#  in the body of your request to the
#  specific needs of the service you’re interacting with.

#send data as  dictionary
requests.post('https://httpbin.org/post', data={'key':'value'})

#send data as a list of tuples
requests.post('https://httpbin.org/post', data=[('key', 'value')])

#send JSON data
response = requests.post('https://httpbin.org/post', json={'key':'value'})


# httpbin.org is a great resource created by the author of requests, Kenneth Reitz. It’s a service that accepts test requests and responds with data about the requests. For instance, you can use it to inspect a basic POST request: