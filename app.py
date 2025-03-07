from flask import Flask, request
import requests
from waitress import serve

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    # Extracting 'uid' parameter from the query string
    uid = request.args.get('uid')
    if not uid:
        return "Error: UID not provided", 400, {'Content-Type': 'text/plain; charset=utf-8'}
    
    url = f"https://freefire-virusteam.vercel.app/glfflike?uid={uid}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if "status" in data and data["status"] == "Success":
            # Extracting Player-related information
            player_name = data.get("Name", "Not available")
            last_login = data.get("Account Last Login", "Not available")
            
            return f"""PLAYER NAME : {player_name}
PLAYER LAST LOGIN : {last_login}""", 200, {'Content-Type': 'text/plain; charset=utf-8'}
        
        else:
            return "Error: Status is not Success or Data not found!", 404, {'Content-Type': 'text/plain; charset=utf-8'}
    
    except Exception as e:
        return f"Error: Server Error\nMessage: {str(e)}", 500, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    print("API is running 🔥")
    serve(app, host='0.0.0.0', port=8080)  # Use this for deployment
