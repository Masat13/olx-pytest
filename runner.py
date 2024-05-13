import subprocess
import os

s = subprocess.run(f'python -m pytest -s -v --alluredir=allure_report tests', shell=True, check=False)

if os.path.exists('allure_report'):
    print("Звіти успішно згенеровані.")
else:
    print("Папка з звітами не знайдена або звіти не згенеровані.")

s = subprocess.run(f'allure serve allure_report --port 8001', shell=True, check=False)
