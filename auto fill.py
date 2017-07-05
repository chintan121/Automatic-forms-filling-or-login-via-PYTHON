from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
#browser.get(('website'))
browser.get(('http://www.gujacpcadm.nic.in/Candidate/Authenticate.aspx'))


#browser.find_element_by_id("id(need basic knowledge of HTML)").send_keys("you want to enter or write");
browser.find_element_by_id("ddlCourse").send_keys("Diploma To Degree Engineering");
browser.find_element_by_id("ddlboard").send_keys("R.K. University");
browser.find_element_by_id("txtRollNo").send_keys("14SDSEE01022");
browser.find_element_by_id("txtAppNo").send_keys("CHINTAN335");
browser.find_element_by_id("txtPinNo").send_keys("Iwontsaypinokk");
browser.find_element_by_id("txtName").send_keys("MUNGRA CHINTAN NILESHBHAI");
browser.find_element_by_id("ddlDD").send_keys("27");
browser.find_element_by_id("ddlmm1").send_keys("12");
browser.find_element_by_id("ddlYY").send_keys("1998");



