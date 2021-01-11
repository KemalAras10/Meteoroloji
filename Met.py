from selenium import webdriver
import time
driver_path = "chromedriver.exe"
browser =webdriver.Chrome(driver_path)
meteoroloji_sitesi = ("https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=Istanbul")
saat_sitesi = ("https://www.timeanddate.com/worldclock/turkey/istanbul")
zaman1 = input("İlk olarak saat kaçta kontrol yapılsın? ")
zaman2 = input("İkinci olarak saat kaçta kontrol yapılsın? ")
browser.get(saat_sitesi)
calisma_durumu = 0
def hava_durumu():
	global calisma_durumu,zaman1,zaman2
	while(True):
		if(calisma_durumu == 0):
			try:
				zaman = browser.find_element_by_id("ct").text
			except:
				pass
			if(zaman.find(zaman1) !=-1):
				browser.get(meteoroloji_sitesi)
				time.sleep(1)
				anlik_durum = browser.find_element_by_class_name("anlik-sicaklik-deger.ng-binding").text
				anlik_durum = float(anlik_durum.replace(",","."))
				sicaklik(anlik_durum)
				print("zaman:",zaman,"Durum:",anlik_durum)
				browser.get(saat_sitesi)
				calisma_durumu = 1
		else:
			try:
				zaman = browser.find_element_by_id("ct").text
			except:
				pass
			if(zaman.find(zaman2) !=-1):
				browser.get(meteoroloji_sitesi)
				time.sleep(1)
				anlik_durum = browser.find_element_by_class_name("anlik-sicaklik-deger.ng-binding").text
				anlik_durum = float(anlik_durum.replace(",","."))
				sicaklik(anlik_durum)
				browser.get(saat_sitesi)
				print("zaman:",zaman,"Durum:",anlik_durum)
				break
def sicaklik(a):
	if(a<20):
		print("sicaklik 20 den az,ortam sicakliği 25 e ayarlanıyor")
	elif(a<10):
		print("sicaklik 10 den az,ortam sicakliği 35 e ayarlanıyor")
	else:
		print("sicaklik normal")
hava_durumu()
