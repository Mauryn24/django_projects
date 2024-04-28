import requests
from django.shortcuts import render



def home(request):
  # USING APIS => Example 1
  response = requests.get('https://api.github.com/events')
  data = response.json()
  result = data[0]["repo"]

  # Example 2
  reponse2 = requests.get('https://dog.ceo/api/breeds/image/random')
  data2 = reponse2.json()
  result2 = data2["message"]

  # Third Api
  response3 = requests.get(' https://emojihub.yurace.pro/api/random')
  data3 = response3.json()
  result3 = data3['htmlCode']

  # Fourth Api
  # response4 = requests.get('https://coffee.alexflipnote.dev/random')
  # data4 = response4.json()
  # result4 = data4['file']


  response4 = requests.get('https://official-joke-api.appspot.com/random_joke')
  data4 = response4.json()
  setup = data4['setup']
  punchline = data4['punchline']
  
  # response5 = requests.get('https://api-server.dataquest.io/economic_data/countries')
  # data5 = response5.json()
  # cc = data5.get('country_code')
  # sn = data5.get('short_name')
  # spv = data5.get('sna_price_valuation')
  
  
  cc = 'N/a'
  sn = 'N/A'
  spv = 'N/A'
  error_message = None  # Initialize error message variable
  
  # Make the HTTP request
  response5 = requests.get('https://api-server.dataquest.io/economic_data/countries')
  data5 = response5.json()
  
  # Check if data5 is a list and is not empty
  if isinstance(data5, list) and data5:
  # Access the first dictionary in the list (assuming there's only one)
    country_data = data5[0]
    
    # Access country information
    cc = country_data.get('country_code')
    sn = country_data.get('short_name')
    spv = country_data.get('sna_price_valuation')
  else:
    # Handle the case where data5 is empty or not a list
    error_message = 'No country data available or invalid response format'
  # Pass the country information or error message to the template
  
  response6 = requests.get('https://api.openbrewerydb.org/v1/breweries/random')
  data6 = response6.json()
  id = data6[0]['id']
  name = data6[0]['name']
  website_url = data6[0]['website_url']
  

  return render(request, 'home.html', {'result': result, 'result2': result2, 'result3': result3, 'setup': setup, 'punchline': punchline, 'cc': cc, 'sn': sn, 'spv': spv, 'error_message': error_message, 'id': id, 'name': name, 'website_url': website_url})
