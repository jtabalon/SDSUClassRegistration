import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def element_exists(xpath):
    try:
        driver.find_element_by_xpath('//*[@id="bodySections"]/div[5]')
    except:
        return False
    return True

email = 'jtabalon@sdsu.edu'
password = 'Maple2019!'
classnum = '20023'
#20123, 20122
#waitlist: 20052, 38114, 20016

n = int(input("How many classes would you like to add? "))

first_class = input("Please enter schedule number: ")

classes = [input("Please enter schedule number: ") for i in range(0, n - 1)]

driver = webdriver.Chrome(executable_path = '/Users/josephtabalon/Desktop/chromedriver')

driver.get('https://sunspot.sdsu.edu/pls/webapp/web_menu.login')

loginbutton = driver.find_element_by_xpath('//*[@id="btn_log_in"]/p/a')
loginbutton.click()

webuser = driver.find_element_by_xpath('//*[@id="mySdsuId"]')
webuser.send_keys(email)

loginbutton2 = driver.find_element_by_xpath('//*[@id="initiateIDMLogin"]')
loginbutton2.click()

enterpassword = driver.find_element_by_xpath('//*[@id="i0118"]')
enterpassword.send_keys(password)

loginbutton3 = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
loginbutton3.click()

no = driver.find_element_by_xpath('//*[@id="idBtn_Back"]')
no.click()

registration = driver.find_element_by_xpath('//*[@id="navMenuMain"]/ul/li[16]/a')
registration.click()

summer = driver.find_element_by_xpath('//*[@id="period"]/option[2]')
summer.click()

update = driver.find_element_by_xpath('//*[@id="settingsForm"]/div[2]/input')
update.click()

addclass = driver.find_element_by_xpath('//*[@id="leftNav"]/div[3]/a[1]')
addclass.click()

inputnumber = driver.find_element_by_xpath('//*[@id="scheduleNumber"]')
inputnumber.send_keys(first_class)

continue_button = driver.find_element_by_xpath('//*[@id="bodySections"]/form/table/tbody/tr[2]/td/input')
continue_button.click()

enroll = driver.find_element_by_xpath('//*[@id="submitAddID"]')
enroll.click()

if element_exists('//*[@id="bodySections"]/div[5]') == True:
    wait = driver.find_element_by_xpath('//*[@id="bodySections"]/div[5]')
    #wait.text == "Do you want to add this class to your wait list?"
    wait_submit = driver.find_element_by_xpath('//*[@id="submitID"]')
    wait_submit.click()

    check1 = driver.find_element_by_xpath('//*[@id="term1ID"]')
    check1.click()

    check2 = driver.find_element_by_xpath('//*[@id="term2ID"]')
    check2.click()

    check3 = driver.find_element_by_xpath('//*[@id="term3ID"]')
    check3.click()

    check4 = driver.find_element_by_xpath('//*[@id="term4ID"]')
    check4.click()

    add_wait = driver.find_element_by_xpath('//*[@id="submitID"]')
    add_wait.click()

#let's add another class

for i in classes:
    addclass1 = driver.find_element_by_xpath('//*[@id="leftNav"]/div[3]/a[1]')
    addclass1.click()

    inputnumber1 = driver.find_element_by_xpath('//*[@id="scheduleNumber"]')
    inputnumber1.send_keys(i)

    continue_button1 = driver.find_element_by_xpath('//*[@id="bodySections"]/form/table/tbody/tr[2]/td/input')
    continue_button1.click()

    enroll1 = driver.find_element_by_xpath('//*[@id="submitAddID"]')
    enroll1.click()
    
    if element_exists('//*[@id="bodySections"]/div[5]') == True:
        waitlist = driver.find_element_by_xpath('//*[@id="bodySections"]/div[5]')
        #waitlist.text == "Do you want to add this class to your wait list?"
        wait_submit = driver.find_element_by_xpath('//*[@id="submitID"]')
        wait_submit.click()

        check1 = driver.find_element_by_xpath('//*[@id="term1ID"]')
        check1.click()

        check2 = driver.find_element_by_xpath('//*[@id="term2ID"]')
        check2.click()

        check3 = driver.find_element_by_xpath('//*[@id="term3ID"]')
        check3.click()

        check4 = driver.find_element_by_xpath('//*[@id="term4ID"]')
        check4.click()

        add_wait = driver.find_element_by_xpath('//*[@id="submitID"]')
        add_wait.click()


print('Enjoy :)')

