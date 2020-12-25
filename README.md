FILE MANAGEMENT DAEMON <br>
This program provides the base to demonize processes of
hashing and uploading, downloading, and deleting files from HTTP API.

HowTo<br>
To use it, you must have Python3. Download the project from GitHub page,
then write in console: <br>
`cd path-to-download-folder`<br>
Now create and activate the environment:<br>
`pipenv install`<br>
`pipenv shell`<br>
And connect to the server via:<br>
`gunicorn --bind 127.0.0.1 wsgi:app --daemon`<br>
To exit write:<br>
`exit`<br>
To test this, run file `test.py` in the folder test. 
