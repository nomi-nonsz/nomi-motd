import time
import sys
import os

time.sleep(.2)
print("""Traceback (most recent call last):
  File "/home/normanandrians/Documents/libdan/main.py", line 267, in <module>
    predict(img)
  File "/home/normanandrians/Documents/libdan/main.py", line 262, in predict
    output = trained_model(img)
TypeError: 'NoneType' object is not callable


""")
time.sleep(50/1000)
print("""File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/h11_impl.py", line 428, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 78, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 276, in __call__
    await super().__call__(scope, receive, send)
  File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
    raise exc
  File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
    await self.app(scope, receive, _send)
  File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
    raise exc
  File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
    await self.app(scope, receive, sender)
  File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 21, in __call__
    raise e
  File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
    await self.app(scope, receive, send)
  File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
    await route.handle(scope, receive, send)
  File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
    await self.app(scope, receive, send)
  File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
    response = await func(request)
""")
      
time.sleep(.1)

print("""File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 237, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 163, in run_endpoint_function
    return await dependant.call(**values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/web/scb_getstatement_api/main.py", line 162, in get_statement
    resault = get_statementscb(session, username, password,login)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/web/scb_getstatement_api/main.py", line 106, in get_statementscb
    session = getscb_session(username, password)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/web/scb_getstatement_api/main.py", line 23, in getscb_session
    driver = webdriver.Chrome(options=chrome_options)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/selenium/webdriver/chrome/webdriver.py", line 84, in __init__
    super().__init__(
  File "/usr/local/lib/python3.11/site-packages/selenium/webdriver/chromium/webdriver.py", line 104, in __init__
    super().__init__(
  File "/usr/local/lib/python3.11/site-packages/selenium/webdriver/remote/webdriver.py", line 286, in __init__
    self.start_session(capabilities, browser_profile)
  File "/usr/local/lib/python3.11/site-packages/selenium/webdriver/remote/webdriver.py", line 378, in start_session
    response = self.execute(Command.NEW_SESSION, parameters)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/selenium/webdriver/remote/webdriver.py", line 440, in execute
    self.error_handler.check_response(response)
  File "/usr/local/lib/python3.11/site-packages/selenium/webdriver/remote/errorhandler.py", line 245, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: unknown error: Chrome failed to start: exited abnormally.
  (unknown error: DevToolsActivePort file doesn't exist)
  (The process started from chrome location /usr/bin/google-chrome is no longer running, so ChromeDriver is assuming that Chrome has crashed.)

""")
time.sleep(.2)

os.system("clear");

print("Processing Norman's interface...")
time.sleep(50/1000)
print("NDbug[0x00a] Starting Nanilux server")
time.sleep(100/1000)
print("NDbug[0x00b] Ubuntu bash integration")
time.sleep(20/1000)
print("NDbug[0x00c] Nanilux integration running...")
time.sleep(200/1000)
print("NDbug[2x00h] Start session")
time.sleep(50/1000)
print("NDbug[2x00m] Printing Message Of The Day (MOTD)")
time.sleep(5/1000)
print("Welcome")

os.system("clear");


motd = """
\033[1;35m

          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠶⠶⠿⠿⢶⣶⠶⠶⠿⠛⠻⠷⠶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀
          ⠀⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀
          ⠀⠀⠀⠀⣾⠇⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀
          ⠀⠀⠀⢠⡿⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⢠⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣆⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀
          ⠀⠀⠀⣾⠇⠀⠀⠀⠀⢰⣿⠀⠀⢀⣀⣤⣿⣧⠀⠀⠀⠀⠀⢠⡄⠀⣤⣤⣤⣤⣤⡹⣧⡀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀
          ⠀⠀⢰⡿⠀⠀⠀⠀⠀⢸⣿⣤⣾⠛⠋⠁⢙⣿⣧⣀⡀⠀⠀⢸⣷⡀⠀⠀⠀⠀⠈⣹⡿⣧⠀⠀⠀⢻⣆⠀⠀⠘⣿⡀⠀
          ⠀⠀⣾⠃⠀⠀⠀⠀⠀⢸⣿⠉⠙⠛⠛⠛⠛⢉⣈⡉⠛⠛⠿⠿⠛⠛⠛⠛⠛⠛⠛⠋⠀⢻⡆⠀⠀⠀⢿⡆⠀⠀⠘⣷⠀
          ⠀⣸⡏⠀⠀⢠⡦⠀⠀⢸⣿⠀⠀⢀⣤⣶⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠄⠘⣷⠀⠀⠀⠈⣿⡀⠀⠀⢹⡇
          ⢠⡿⠀⠀⠀⣼⠇⠀⠀⢸⣿⠀⠾⠛⠁⢿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢤⣤⠴⠶⠛⠉⠀⠀⣿⡄⠀⠀⠀⢸⡇⠀⠀⠈⣿
          ⢸⡇⠀⠀⠀⣿⠀⠀⠀⠈⣿⠀⠀⠀⠀⠘⠿⠿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠘⣿⠀⠀⢠⡿
          ⠘⣷⠀⠀⠀⣿⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣠⣶⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⣿⠀⣀⣾⠃
          ⠀⠹⣧⠀⠀⣿⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠻⠷⠿⠛⠉⠉⠉⠉⠀⠀⠀⢀⣀⣤⡾⣿⡇⠀⠀⠀⢰⣿⡾⠛⠁⠀
          ⠀⠀⠙⣷⡄⢹⡇⠀⠀⠀⠀⢿⣶⣦⣤⣀⣀⣀⣀⣀⣀⣀⣀⣤⣤⣤⣴⠶⠶⠿⠛⠋⠁⠀⣿⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀
          ⠀⠀⠀⠈⠻⣾⣿⡀⠀⠀⠀⠘⣷⡀⠉⠉⠉⠛⠛⠛⠋⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⣀⣴⠟⠁⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠈⠙⢷⡄⠀⠀⠀⠹⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠷⣦⣤⣤⣽⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;36m
 .__   __.      ___      .__   __.  __   __       __    __  ___   ___
 |  \ |  |     /   \     |  \ |  | |  | |  |     |  |  |  | \  \ /  /
 |   \|  |    /  ^  \    |   \|  | |  | |  |     |  |  |  |  \  V  /
 |  . `  |   /  /_\  \   |  . `  | |  | |  |     |  |  |  |   >   <
 |  |\   |  /  _____  \  |  |\   | |  | |  `----.|  `--'  |  /  .  \\
 |__| \__| /__/     \__\ |__| \__| |__| |_______| \______/  /  / \__\\
        \__________________________________________________/__/
\033[0;29m
  _____________________________________________________________________
 /                                                                     \ 
  Start to run Nanilux server and devtools
  clone repo  : git clone \033[4;36mhttps://github.com/norman-andrians/nanilux.git\033[0;29m
  change perm : chmod +x nilux.sh
  run         : ./nilux.sh
 \_____________________________________________________________________/

"""

for p in motd:
   print(p, end='')
   sys.stdout.flush()
   time.sleep(0.00004)