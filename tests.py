import requests


headers = {
    "Authorization": "Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTcxMDEzNzUsInVzZXJfaWQiOiIxNjE4MDkzNCIsInR5cGUiOiJwdXBpbCJ9.lNNEzOHPiMMG8WQRUIpe5SwdrjJH0cgRIh8YdTKKp2M"
}


response = requests.get("http://localhost:8008/api/v1/schools/my-school", headers=headers)
print(response)
print(response.json())

