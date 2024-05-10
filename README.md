Some new super test

pip install --no-cache-dir -r requirments.txt
playwright install

run test - pytest tests -s -v  

To get allure report on Windows: 

install JAVA somehow

in powershell run:
- Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
- Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression   
- scoop install allure  

Then:
- pytest tests --alluredir=report
- allure serve report  

If tests has some marker like '@marker.smoke' e.g., you can use 'pytest -m smoke' to run selected tests

For parallel tests run 'pytest -s -v -n auto --dist=loadscope'

docker build -t custom_framework .
docker run custom_framework