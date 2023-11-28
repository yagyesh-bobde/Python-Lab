import requests 

word = input("Enter a word to search the meaning: ")
response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)

if(response.status_code == 200) : 
    try: 
        data = response.json()
        print(data)
    except: 
        try: 
            data = response.text() 
            print(data)
        except: 
            print("Invalid data!")
else: 
    print("Error Code: ", response.status_code)
