import hashlib
import os


def allowed_file(filename):
    """
    Checks if the format for the file received is acceptable. For this
    particular case, it accepts only image files. This means, files with
    extension ".png", ".jpg", ".jpeg" or ".gif".

    Parameters
    ----------
    filename : str
        Filename from werkzeug.datastructures.FileStorage file.

    Returns
    -------
    bool
        True if the file is an image, False otherwise.
    """
    # Current implementation will allow any kind of file.
    ### f_ext = os.path.splitext(filename)[1].lower()
    ### if f_ext == '.png' or f_ext == '.jpg' or f_ext == '.jpeg' or f_ext == '.gif':
    if filename.lower().endswith(('.png', '.jpg', '.jpeg','.gif')):    
        return True
    else: 
        return False
    

def get_file_hash(file):
    """
    Returns a new filename based on the file content using MD5 hashing.
    It uses hashlib.md5() function from Python standard library to get
    the hash.

    Parameters
    ----------
    file : werkzeug.datastructures.FileStorage
        File sent by user.

    Returns
    -------
    str
        New filename based in md5 file hash.
    """
    # Current implementation will return the original file name.
    h = hashlib.md5(file.read()).hexdigest()
    file.seek(0)
    f_ext = os.path.splitext(file.filename)[1]
    file.filename = h+f_ext    
    return os.path.basename(file.filename)
