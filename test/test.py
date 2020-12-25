import requests


url = "http://127.0.0.1:8000"

# test uploading
files = [
    open('test_files_for_uplod/krime.jpg', 'rb'),
    open('test_files_for_uplod/river.jpg', 'rb'),
    open('test_files_for_uplod/resume.pdf', 'rb'),
    open('test_files_for_uplod/Byron.txt', 'rb'),
    ]
responses = [requests.post(url, files={'uploaded_file': file}) for file in files]
# print hash of all uploaded files
for response in responses:
    print(response.text)

# download text file and write to the test folder
file = requests.get(url, params={'download_filename': responses[-1].text}) 
downloaded_file = open('downloaded_file.txt', 'w')
downloaded_file.write(file.text)
downloaded_file.close()

# delete file
requests.post(url, params={'delete_filename': responses[0].text}) 