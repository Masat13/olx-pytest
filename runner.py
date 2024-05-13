import subprocess
import os

s = subprocess.run(f'python -m pytest -s -v --alluredir=allure_report tests', shell=True, check=False)


s = subprocess.run(f'docker ps', shell=True, check=False)
s = subprocess.run(f'allure serve allure_report --port 8001', shell=True, check=False)

