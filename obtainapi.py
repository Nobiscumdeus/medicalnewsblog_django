'''
import requests

from decouple import config 


token="99cce0001d214c7ae97db5f83c284f56dc37751b"

protected_url='http://localhost:8000/doctorapi/doctors'


headers={
    "Authorization":f'Bearer{token}'
}

#Making a get response to the doctor api
response=requests.get(protected_url,headers=headers)
try:
    response.raise_for_status() #Raises an exception for HTTP errors 
    #We print the response here if successfulprint
    print("Request was successful.")
    print("Request data:")
    print(response.text)  #This prints the response as a string 
except requests.exceptions.HTTPError as e :
    #Request failed with an Http Error 
    print(f"Request failed with status code {response.status_code}")
    print(f"Error details : {e}")
except requests.exceptions.RequestException as e :
    #Other request-related errors e.g., network errors
    print(f"Request encountered an exception : {e}")
 
'''
from decouple import config
SECRET_KEY=config('SECRET_KEY')
print(SECRET_KEY)
 

   
 

    
   
   
   
   