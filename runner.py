import subprocess

s = subprocess.run(f'python -m pytest -s -v', shell=True, check=False)
