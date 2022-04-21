import pyautogui as pag
import webbrowser as web
import time

start_time = time.time()

# open new tab for doordash
web.open_new_tab("doordash.com")
time.sleep(10)

# go to sign in page
pag.typewrite(["tab"])
pag.typewrite(["enter"])
time.sleep(10)

# print login info
pag.typewrite("austin.j.gain@gmail.com")  
pag.typewrite(["tab"])
pag.typewrite("Applejuice33!")
for x in range(2):
    pag.typewrite(["tab"])
pag.typewrite(["enter"])
time.sleep(10)

# search for poke bowl
for x in range(3):
    pag.typewrite(["tab"])
pag.typewrite("poke bowl")
pag.typewrite(["down"])
pag.typewrite(["enter"])
time.sleep(10)

# go to poke bowl page
for x in range(11):
    pag.typewrite(["tab"])
pag.typewrite(["enter"])
time.sleep(10)

# go to usual order
for x in range(9):
    pag.typewrite(["tab"])
pag.typewrite(["enter"])

# enter order data
pag.moveTo(649, 568, duration = 0)
time.sleep(5)
pag.scroll(-200)
time.sleep(5)                                                                                                                                                                                                                                                   
pag.click()
time.sleep(5)
for x in range(61):
    pag.typewrite(["tab"])
pag.typewrite(["enter"])
pag.typewrite(["down"])
pag.typewrite(["enter"])
for x in range(3):
    pag.typewrite(["tab"])
pag.typewrite(["enter"])

# go to checkout
pag.moveTo(1077, 202, duration = 0)
time.sleep(5)
pag.click()
time.sleep(5)
for x in range(2):
    pag.typewrite(["tab"])
pag.typewrite(["enter"])
time.sleep(10)

# place order
pag.scroll(-1000)
pag.moveTo(375, 817, duration = 0)
time.sleep(5)
pag.click()
pag.moveTo(698, 1092, duration = 0)
time.sleep(5)
pag.click()

print(pag.position())
print("DONE")

print("%.2f seconds" % (time.time() - start_time))










