import subprocess

class CompileRepo():
    def compile_repo(url, destination):
        subprocess.run("git clone {url} {destination}", "cd {destination}", "make -j4")
