from flask import Flask, request, send_from_directory
import os


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def manage_files():
    '''
    Function that implements uploading, downloading and
    deleting files.
    '''
    if request.method == 'POST':
        # Check if there an input file. If it is, do hash
        # and upload a file to the specific directory with
        # its hash as the name. 
        if request.files:
            uploaded_file = request.files['uploaded_file'] 
            file_type = uploaded_file.filename.split('.')[-1]
            http_response = hash(uploaded_file) 
            if 'store' not in os.listdir():
                os.mkdir('store')
            folder = str(http_response)[:2]
            if folder not in os.listdir('store'):
                os.mkdir(os.sep.join(['store', folder]))
            if uploaded_file.filename != '':
                uploaded_file.save(
                    os.sep.join(['store', folder, str(http_response)]) + '.' + file_type)
            return str(http_response)
        
        # Check if there a 'delete_filename' input parameter. 
        # If it is, search for it and delete.
        # FileNotFoundError raises if file not found.
        if 'delete_filename' in request.args:
            path, fullFilename = _find_path_and_fullFilename('delete_filename')
            os.remove(path + fullFilename)
            return ''

    # Check if there a 'download_filename' input parameter. 
    # If it is, search for it and send.
    # FileNotFoundError raises if file not found.
    if 'download_filename' in request.args:
        path, fullFilename = _find_path_and_fullFilename('download_filename')
        return send_from_directory(path, fullFilename, as_attachment=True)


def _find_path_and_fullFilename(arg_name):
    get_clear_name = lambda filename: os.path.splitext(filename)[0]
    delete_filename = get_clear_name(request.args.get(arg_name))
    folder = delete_filename[:2]
    path = os.sep.join(['store', folder, ''])
    dir_filenames = os.listdir(path)
    ind = list(map(get_clear_name, dir_filenames)).index(delete_filename)
    fullFilename = dir_filenames[ind]
    return path, fullFilename
    


if __name__ == "__main__":
    app.run(host='127.0.0.1')