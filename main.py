import subprocess
import os
from time import sleep
if any(x.__contains__('statsmodels-HC-cov') for x in os.popen('pip freeze | grep statsmodels').read().split(' ')):
    print("Если вы хотите это удалить, запустите:\npip uninstall statsmodels-hc-cov")
    raise SystemExit
iters = 1
print("Вы хотите установить эту хрень с ковариациями?[y/N]")
if input().lower().strip() in ['y', 'да', 'yes', 'д']:
    subprocess.Popen(["python", "setup.py", "bdist_wheel"])
    sleep(2)
    iters = 0
    wheel = [i for i in os.listdir("dist/") if i.endswith(".whl")][0]
    subprocess.Popen(['pip', 'install', f"dist/{wheel}"])
    print(f"running: pip install dist/{wheel}")
    print(f"Installed!\nTo uninstall:  statsmodels-hc-cov")
