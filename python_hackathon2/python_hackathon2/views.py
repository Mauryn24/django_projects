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

  try:
    response4 = requests.get('https://emojihub.yurace.pro/api/random')
    response4.raise_for_status()  # Raise an exception for HTTP errors
    data4 = response.json()
    result4 = data.get('emoji', 'No emoji found')  # Get the emoji from the response data
  except requests.RequestException as e:
    result4 = f'Error: {e}'  # Handle request exceptions
  except ValueError as e:
      result4 = f'Error decoding JSON: {e}'  # Handle JSON decode errors

  
  return render(request, 'home.html', {'result': result, 'result2': result2, 'result3': result3, 'result4': result4})