FILE MANAGEMENT DAEMON
This program provides the base to demonize processes of
hashing and uploading, downloading, and deleting files from HTTP API.


HowTo

To use it, you must have Python3. Download the project from GitHub page,
then write in console:
cd path-to-download-folder

Now create and activate the environment:
pipenv install
pipenv shell

And connect to the server via:
gunicorn --bind 0.0.0.0 wsgi:app --daemon

To exit write:
exit

To test this, run file test.py in the folder test. 
