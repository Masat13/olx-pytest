import subprocess
import shutil

s = subprocess.run(f'python -m pytest -s -v --alluredir=allure_report', shell=True, check=False)
# local report
# s = subprocess.run(f'allure serve allure_report --port 8001', shell=True, check=False)
# docker jenkins report generate and copy to jenkins
subprocess.run('allure generate allure_report -o allure_report_html', shell=True, check=False)
shutil.copytree('allure_report', 'C:\Users\imasa\.jenkins\workspace\docker job', dirs_exist_ok=True)
