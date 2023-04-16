import shutil

def Cleaner():
    """
    Deletes directories "resources/Mp4" and "resources/Mp3" and all their contents.
    """
    shutil.rmtree("resources/Mp4")
    shutil.rmtree("resources/Mp3")