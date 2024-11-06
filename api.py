import requests

# URL of your deployed Flask API on Render
url = "https://your-app-name.onrender.com/predict"

# Path to your local image file
file_path = "/home/sarishrv/Videos/vs-code-projects/E-WASTE/backend/SARISH.jpg"

# Open the image file in binary mode and send it in the POST request
with open(file_path, 'rb') as img_file:
    files = {'file': img_file}
    response = requests.post(url, files=files)

# Print the response from the server
print(response.json())
