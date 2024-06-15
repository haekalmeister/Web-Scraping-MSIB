from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Path to your ChromeDriver
PATH = 'C:\\Program Files (x86)\\chromedriver.exe'
url = 'https://kampusmerdeka.kemdikbud.go.id/program/magang/browse'

# Setup Chrome options
options = webdriver.ChromeOptions()
#options.add_argument("--headless")  # Run in headless mode
options.add_argument("--start-maximized")
options.page_load_strategy = 'normal'

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

# List of cities to iterate over
cities = [
    "Kota Ambon",
    "Kota Balikpapan",
    "Kota Banda Aceh",
    "Kota Bandar Lampung",
    "Kota Bandung",
    "Kota Banjar",
    "Kota Banjarbaru",
    "Kota Banjarmasin",
    "Kota Batam",
    "Kota Batu",
    "Kota Baubau",
    "Kota Bekasi",
    "Kota Bengkulu",
    "Kota Bima",
    "Kota Binjai",
    "Kota Bitung",
    "Kota Blitar",
    "Kota Bogor",
    "Kota Bontang",
    "Kota Bukittinggi",
    "Kota Cilegon",
    "Kota Cimahi",
    "Kota Cirebon",
    "Kota Denpasar",
    "Kota Depok",
    "Kota Dumai",
    "Kota Gorontalo",
    "Kota Gunungsitoli",
    "Kota Jakarta Barat",
    "Kota Jakarta Pusat",
    "Kota Jakarta Selatan",
    "Kota Jakarta Timur",
    "Kota Jakarta Utara",
    "Kota Jambi",
    "Kota Jayapura",
    "Kota Kediri",
    "Kota Kendari",
    "Kota Kotamobagu",
    "Kota Kupang",
    "Kota Langsa",
    "Kota Lhokseumawe",
    "Kota Lubuklinggau",
    "Kota Madiun",
    "Kota Magelang",
    "Kota Makassar",
    "Kota Malang",
    "Kota Manado",
    "Kota Mataram",
    "Kota Medan",
    "Kota Metro",
    "Kota Mojokerto",
    "Kota Padang",
    "Kota Padang Panjang",
    "Kota Padang Sidempuan",
    "Kota Pagar Alam",
    "Kota Palangka Raya",
    "Kota Palembang",
    "Kota Palopo",
    "Kota Palu",
    "Kota Pangkalpinang",
    "Kota Parepare",
    "Kota Pariaman",
    "Kota Pasuruan",
    "Kota Payakumbuh",
    "Kota Pekalongan",
    "Kota Pekanbaru",
    "Kota Pematangsiantar",
    "Kota Pontianak",
    "Kota Prabumulih",
    "Kota Probolinggo",
    "Kota Sabang",
    "Kota Salatiga",
    "Kota Samarinda",
    "Kota Sawahlunto",
    "Kota Semarang",
    "Kota Serang",
    "Kota Sibolga",
    "Kota Singkawang",
    "Kota Solok",
    "Kota Sorong",
    "Kota Subulussalam",
    "Kota Sukabumi",
    "Kota Sungai Penuh",
    "Kota Surabaya",
    "Kota Surakarta",
    "Kota Tangerang Selatan",
    "Kota Tangerang",
    "Kota Tanjungbalai",
    "Kota Tanjungpinang",
    "Kota Tarakan",
    "Kota Tasikmalaya",
    "Kota Tebing Tinggi",
    "Kota Tegal",
    "Kota Ternate",
    "Kota Tidore Kepulauan",
    "Kota Tomohon",
    "Kota Tual",
    "Kota Yogyakarta",
    "Kab. Aceh Barat",
  "Kab. Aceh Barat Daya",
  "Kab. Aceh Besar",
  "Kab. Aceh Jaya",
  "Kab. Aceh Selatan",
  "Kab. Aceh Singkil",
  "Kab. Aceh Tamiang",
  "Kab. Aceh Tengah",
  "Kab. Aceh Tenggara",
  "Kab. Aceh Timur",
  "Kab. Aceh Utara",
  "Kab. Administrasi Kepulauan Seribu",
  "Kab. Agam",
  "Kab. Alor",
  "Kab. Asahan",
  "Kab. Asmat",
  "Kab. Badung",
  "Kab. Balangan",
  "Kab. Bandung",
  "Kab. Bandung Barat",
  "Kab. Banggai",
  "Kab. Banggai Kepulauan",
  "Kab. Banggai Laut",
  "Kab. Bangka",
  "Kab. Bangka Barat",
  "Kab. Bangka Selatan",
  "Kab. Bangka Tengah",
  "Kab. Bangkalan",
  "Kab. Bangli",
  "Kab. Banjar",
  "Kab. Banjarnegara",
  "Kab. Bantaeng",
  "Kab. Bantul",
  "Kab. Banyuasin",
  "Kab. Banyumas",
  "Kab. Banyuwangi",
  "Kab. Barito Kuala",
  "Kab. Barito Selatan",
  "Kab. Barito Timur",
  "Kab. Barito Utara",
  "Kab. Barru",
  "Kab. Batang",
  "Kab. Batanghari",
  "Kab. Batu Bara",
  "Kab. Bekasi",
  "Kab. Belitung",
  "Kab. Belitung Timur",
  "Kab. Belu",
  "Kab. Bener Meriah",
  "Kab. Bengkalis",
  "Kab. Bengkayang",
  "Kab. Bengkulu Selatan",
  "Kab. Bengkulu Tengah",
  "Kab. Bengkulu Utara",
  "Kab. Berau",
  "Kab. Biak Numfor",
  "Kab. Bima",
  "Kab. Bintan",
  "Kab. Bireuen",
  "Kab. Blitar",
  "Kab. Blora",
  "Kab. Boalemo",
  "Kab. Bogor",
  "Kab. Bojonegoro",
  "Kab. Bolaang Mongondow",
  "Kab. Bolaang Mongondow Selatan",
  "Kab. Bolaang Mongondow Timur",
  "Kab. Bolaang Mongondow Utara",
  "Kab. Bombana",
  "Kab. Bondowoso",
  "Kab. Bone",
  "Kab. Bone Bolango",
  "Kab. Boven Digoel",
  "Kab. Boyolali",
  "Kab. Brebes",
  "Kab. Buleleng",
  "Kab. Bulukumba",
  "Kab. Bulungan",
  "Kab. Bungo",
  "Kab. Buol",
  "Kab. Buru",
  "Kab. Buru Selatan",
  "Kab. Buton",
  "Kab. Buton Selatan",
  "Kab. Buton Tengah",
  "Kab. Buton Utara",
  "Kab. Ciamis",
  "Kab. Cianjur",
  "Kab. Cilacap",
  "Kab. Cirebon",
  "Kab. Dairi",
  "Kab. Deiyai",
  "Kab. Deli Serdang",
  "Kab. Demak",
  "Kab. Dharmasraya",
  "Kab. Dogiyai",
  "Kab. Dompu",
  "Kab. Donggala",
  "Kab. Empat Lawang",
  "Kab. Ende",
  "Kab. Enrekang",
  "Kab. Fakfak",
  "Kab. Flores Timur",
  "Kab. Garut",
  "Kab. Gayo Lues",
  "Kab. Gianyar",
  "Kab. Gorontalo",
  "Kab. Gorontalo Utara",
  "Kab. Gowa",
  "Kab. Gresik",
  "Kab. Grobogan",
  "Kab. Gunungkidul",
  "Kab. Gunung Mas",
  "Kab. Halmahera Barat",
  "Kab. Halmahera Selatan",
  "Kab. Halmahera Tengah",
  "Kab. Halmahera Timur",
  "Kab. Halmahera Utara",
  "Kab. Hulu Sungai Selatan",
  "Kab. Hulu Sungai Tengah",
  "Kab. Hulu Sungai Utara",
  "Kab. Humbang Hasundutan",
  "Kab. Indragiri Hilir",
  "Kab. Indragiri Hulu",
  "Kab. Indramayu",
  "Kab. Intan Jaya",
  "Kab. Jayapura",
  "Kab. Jayawijaya",
  "Kab. Jember",
  "Kab. Jembrana",
  "Kab. Jeneponto",
  "Kab. Jepara",
  "Kab. Jombang",
  "Kab. Kaimana",
  "Kab. Kampar",
  "Kab. Kapuas",
  "Kab. Kapuas Hulu",
  "Kab. Karanganyar",
  "Kab. Karangasem",
  "Kab. Karawang",
  "Kab. Karimun",
  "Kab. Karo",
  "Kab. Katingan",
  "Kab. Kaur",
  "Kab. Kayong Utara",
  "Kab. Kebumen",
  "Kab. Kediri",
  "Kab. Keerom",
  "Kab. Kendal",
  "Kab. Kepahiang",
  "Kab. Kepulauan Anambas",
  "Kab. Kepulauan Aru",
  "Kab. Kepulauan Mentawai",
  "Kab. Kepulauan Meranti",
  "Kab. Kepulauan Sangihe",
  "Kab. Kepulauan Selayar",
  "Kab. Kepulauan Siau Tagulandang Biaro",
  "Kab. Kepulauan Sula",
  "Kab. Kepulauan Talaud",
  "Kab. Kepulauan Tanimbar",
  "Kab. Kepulauan Yapen",
  "Kab. Kerinci",
  "Kab. Ketapang",
  "Kab. Klaten",
  "Kab. Klungkung",
  "Kab. Kolaka",
  "Kab. Kolaka Timur",
  "Kab. Kolaka Utara",
  "Kab. Konawe",
  "Kab. Konawe Kepulauan",
  "Kab. Konawe Selatan",
  "Kab. Konawe Utara",
  "Kab. Kotabaru",
  "Kab. Kotawaringin Barat",
  "Kab. Kotawaringin Timur",
  "Kab. Kuantan Singingi",
  "Kab. Kubu Raya",
  "Kab. Kudus",
  "Kab. Kulon Progo",
  "Kab. Kuningan",
  "Kab. Kupang",
  "Kab. Kutai Barat",
  "Kab. Kutai Kartanegara",
  "Kab. Kutai Timur",
  "Kab. Labuhanbatu",
  "Kab. Labuhanbatu Selatan",
  "Kab. Labuhanbatu Utara",
  "Kab. Lahat",
  "Kab. Lamandau",
  "Kab. Lamongan",
  "Kab. Lampung Barat",
  "Kab. Lampung Selatan",
  "Kab. Lampung Tengah",
  "Kab. Lampung Timur",
  "Kab. Lampung Utara",
  "Kab. Landak",
  "Kab. Langkat",
  "Kab. Lanny Jaya",
  "Kab. Lebak",
  "Kab. Lebong",
  "Kab. Lembata",
  "Kab. Lima Puluh Kota",
  "Kab. Lingga",
  "Kab. Lombok Barat",
  "Kab. Lombok Tengah",
  "Kab. Lombok Timur",
"Kab. Lombok Utara",
"Kab. Lumajang",
"Kab. Luwu",
"Kab. Luwu Timur",
"Kab. Luwu Utara",
"Kab. Madiun",
"Kab. Magelang",
"Kab. Magetan",
"Kab. Mahakam Ulu",
"Kab. Majalengka",
"Kab. Majene",
"Kab. Malaka",
"Kab. Malang",
"Kab. Malinau",
"Kab. Maluku Barat Daya",
"Kab. Maluku Tengah",
"Kab. Maluku Tenggara",
"Kab. Mamasa",
"Kab. Mamberamo Raya",
"Kab. Mamberamo Tengah",
"Kab. Mamuju",
"Kab. Mamuju Tengah",
"Kab. Mandailing Natal",
"Kab. Manggarai",
"Kab. Manggarai Barat",
"Kab. Manggarai Timur",
"Kab. Manokwari",
"Kab. Manokwari Selatan",
"Kab. Mappi",
"Kab. Maros",
"Kab. Maybrat",
"Kab. Melawi",
"Kab. Mempawah",
"Kab. Merangin",
"Kab. Merauke",
"Kab. Mesuji",
"Kab. Mimika",
"Kab. Minahasa",
"Kab. Minahasa Selatan",
"Kab. Minahasa Tenggara",
"Kab. Minahasa Utara",
"Kab. Mojokerto",
"Kab. Morowali",
"Kab. Morowali Utara",
"Kab. Muara Enim",
"Kab. Muaro Jambi",
"Kab. Mukomuko",
"Kab. Muna",
"Kab. Muna Barat",
"Kab. Murung Raya",
"Kab. Musi Banyuasin",
"Kab. Musi Rawas",
"Kab. Musi Rawas Utara",
"Kab. Nabire",
"Kab. Nagan Raya",
"Kab. Nagekeo",
"Kab. Natuna",
"Kab. Nduga",
"Kab. Ngada",
"Kab. Nganjuk",
"Kab. Ngawi",
"Kab. Nias",
"Kab. Nias Barat",
"Kab. Nias Selatan",
"Kab. Nias Utara",
"Kab. Nunukan",
"Kab. Ogan Ilir",
"Kab. Ogan Komering Ilir",
"Kab. Ogan Komering Ulu",
"Kab. Ogan Komering Ulu Selatan",
"Kab. Ogan Komering Ulu Timur",
"Kab. Pacitan",
"Kab. Padang Lawas",
"Kab. Padang Lawas Utara",
"Kab. Padang Pariaman",
"Kab. Pakpak Bharat",
"Kab. Pamekasan",
"Kab. Pandeglang",
"Kab. Pangandaran",
"Kab. Pangkajene Dan Kepulauan",
"Kab. Paniai",
"Kab. Parigi Moutong",
"Kab. Pasaman",
"Kab. Pasaman Barat",
"Kab. Pasangkayu",
"Kab. Paser",
"Kab. Pasuruan",
"Kab. Pati",
"Kab. Pegunungan Arfak",
"Kab. Pegunungan Bintang",
"Kab. Pekalongan",
"Kab. Pelalawan",
"Kab. Pemalang",
"Kab. Penajam Paser Utara",
"Kab. Penukal Abab Lematang Ilir",
"Kab. Pesawaran",
"Kab. Pesisir Barat",
"Kab. Pesisir Selatan",
"Kab. Pidie",
"Kab. Pidie Jaya",
"Kab. Pinrang",
"Kab. Pohuwato",
"Kab. Polewali Mandar",
"Kab. Ponorogo",
"Kab. Poso",
"Kab. Pringsewu",
"Kab. Probolinggo",
"Kab. Pulang Pisau",
"Kab. Pulau Morotai",
"Kab. Pulau Taliabu",
"Kab. Puncak",
"Kab. Puncak Jaya",
"Kab. Purbalingga",
"Kab. Purwakarta",
"Kab. Purworejo",
"Kab. Raja Ampat",
"Kab. Rejang Lebong",
"Kab. Rembang",
"Kab. Rokan Hilir",
"Kab. Rokan Hulu",
"Kab. Rote Ndao",
"Kab. Sabu Raijua",
"Kab. Sambas",
"Kab. Samosir",
"Kab. Sampang",
"Kab. Sanggau",
"Kab. Sarmi",
"Kab. Sarolangun",
"Kab. Sekadau",
"Kab. Seluma",
"Kab. Semarang",
"Kab. Seram Bagian Barat",
"Kab. Seram Bagian Timur",
"Kab. Serang",
"Kab. Serdang Bedagai",
"Kab. Seruyan",
"Kab. Siak",
"Kab. Sidenreng Rappang",
"Kab. Sidoarjo",
"Kab. Sigi",
"Kab. Sijunjung",
"Kab. Sikka",
"Kab. Simalungun",
"Kab. Simeulue",
"Kab. Sinjai",
"Kab. Sintang",
"Kab. Situbondo",
"Kab. Sleman",
"Kab. Solok",
"Kab. Solok Selatan",
"Kab. Soppeng",
"Kab. Sorong",
"Kab. Sorong Selatan",
"Kab. Sragen",
"Kab. Subang",
"Kab. Sukabumi",
"Kab. Sukamara",
"Kab. Sukoharjo",
"Kab. Sumba Barat",
"Kab. Sumba Barat Daya",
"Kab. Sumba Tengah",
"Kab. Sumba Timur",
"Kab. Sumbawa",
"Kab. Sumbawa Barat",
"Kab. Sumedang",
"Kab. Sumenep",
"Kab. Supiori",
"Kab. Tabalong",
"Kab. Tabanan",
"Kab. Takalar",
"Kab. Tambrauw",
"Kab. Tana Tidung",
"Kab. Tana Toraja",
"Kab. Tanah Bumbu",
"Kab. Tanah Datar",
"Kab. Tanah Laut",
"Kab. Tangerang",
"Kab. Tanggamus",
"Kab. Tanjung Jabung Barat",
"Kab. Tanjung Jabung Timur",
"Kab. Tapanuli Selatan",
"Kab. Tapanuli Tengah",
"Kab. Tapanuli Utara",
"Kab. Tapin",
"Kab. Tasikmalaya",
"Kab. Tebo",
"Kab. Tegal",
"Kab. Teluk Bintuni",
"Kab. Teluk Wondama",
"Kab. Temanggung",
"Kab. Timor Tengah Selatan",
"Kab. Timor Tengah Utara",
"Kab. Toba",
"Kab. Tojo Una Una",
"Kab. Tolikara",
"Kab. Tolitoli",
"Kab. Toraja Utara",
"Kab. Trenggalek",
"Kab. Tuban",
"Kab. Tulang Bawang",
"Kab. Tulang Bawang Barat",
"Kab. Tulungagung",
"Kab. Wajo",
"Kab. Wakatobi",
"Kab. Waropen",
"Kab. Way Kanan",
"Kab. Wonogiri",
"Kab. Wonosobo",
"Kab. Yahukimo",
"Kab. Yalimo"
]

def load_page_with_retry(url, max_retry_attempts=3):
    retry_attempts = 0
    while retry_attempts < max_retry_attempts:
        try:
            driver.get(url)
            time.sleep(5)
            return True
        except Exception as e:
            print(f"Retrying ({retry_attempts + 1}/{max_retry_attempts})")
            retry_attempts += 1
    return False

def scroll_div_until_items_loaded(driver, scrollable_div, target_item_count, current_item_count=0, scroll_pause_time=1, max_scroll_attempts=2000):
    scroll_attempts = 0
    last_item_count = 0
    
    while current_item_count < target_item_count and scroll_attempts < max_scroll_attempts:
        
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
        
        
        time.sleep(scroll_pause_time)
        
        
        scroll_attempts += 1
        
        
        current_item_count = len(driver.find_elements(By.CSS_SELECTOR, "div.box-0-0-1.flex-0-0-2.description-0-0-811"))
        print(f"Scrolled to bottom - Attempt {scroll_attempts + 1}, items count: {current_item_count}")
        
        
        if current_item_count == last_item_count:
            print("No new items loaded. Stopping scroll.")
            break
        
        last_item_count = current_item_count
    
    print(f"Total scroll attempts: {scroll_attempts}, items count: {current_item_count}")
    return current_item_count


with open('job_data_test.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['City', 'Job Name', 'Company', 'Location']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    
    for city in cities:
        print(f"Processing city: {city}")

        
        if not load_page_with_retry(url):
            print("Failed to load page after multiple attempts. Exiting...")
            driver.quit()
            exit()
        
        
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.input-0-0-44.input-valid-0-0-55.inputBox-0-0-265[placeholder='Semua Lokasi']"))
        )
        search_input.clear()
        search_input.send_keys(city)
        search_input.send_keys(Keys.RETURN)
        
        
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.box-0-0-1.clickable-0-0-8.container-0-0-277.transition-0-0-41.primary-0-0-281.primary-normal-0-0-282"))
        )
        search_button.click()
        
        
        time.sleep(8)  
        
        
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        try:
            target_item_text = soup.find('p', class_='text-0-0-56 sans-0-0-70 italic-0-0-65').text
            target_item_count = int(target_item_text.split()[-1])  # Extract the last word and convert to integer
            print(f"Target item count for {city}: {target_item_count}")
        except Exception as e:
            print(f"Error extracting target item count: {e}")
            target_item_count = 0
        
        if target_item_count == 0:
            print(f"No job listings found for {city}. Moving to the next city.")
            continue

        items_processed = 0
        chunk_size = 2000
        scroll_pause_time = 1

        
        try:
            scrollable_div = driver.find_element(By.CSS_SELECTOR, "div.box-0-0-1.flex-0-0-2.container-0-0-187.scroll-0-0-855")
            scrollable = True
        except:
            scrollable = False

        if scrollable:
            while items_processed < target_item_count:
               
                items_loaded = scroll_div_until_items_loaded(driver, scrollable_div, items_processed + chunk_size, items_processed)
                
                
                html_doc = driver.page_source
                soup = BeautifulSoup(html_doc, 'html.parser')
                
                
                desc_list = soup.find('div', class_='box-0-0-1 content-0-0-189')
                if not desc_list:
                    print(f"No job listings found for {city}. Moving to the next city.")
                    break
                
                descriptions = desc_list.find_all('div', class_='box-0-0-1 flex-0-0-2 description-0-0-811')
                for job in descriptions[items_processed:]:
                    job_name = job.find('p', class_='text-0-0-56 sans-0-0-70 heading-5-0-0-77 pad-0-0-812 ellipsis-0-0-817').text.strip()
                    company = job.find('p', class_='text-0-0-56 sans-0-0-70 tiny-0-0-72 ellipsis-0-0-59 pad-0-0-812').text.strip()
                    location = job.find('span', class_='text-0-0-56 sans-0-0-70').text.strip()
                    
                    
                    writer.writerow({'City': city, 'Job Name': job_name, 'Company': company, 'Location': location})
                    
                    items_processed += 1
                
                print(f"Items processed for {city}: {items_processed}")

        else:
            
            html_doc = driver.page_source
            soup = BeautifulSoup(html_doc, 'html.parser')
            
            
            desc_list = soup.find('div', class_='box-0-0-1 content-0-0-189')
            if not desc_list:
                print(f"No job listings found for {city}. Moving to the next city.")
                continue
            
            descriptions = desc_list.find_all('div', class_='box-0-0-1 flex-0-0-2 description-0-0-811')
            for job in descriptions:
                job_name = job.find('p', class_='text-0-0-56 sans-0-0-70 heading-5-0-0-77 pad-0-0-812 ellipsis-0-0-817').text.strip()
                company = job.find('p', class_='text-0-0-56 sans-0-0-70 tiny-0-0-72 ellipsis-0-0-59 pad-0-0-812').text.strip()
                location = job.find('span', class_='text-0-0-56 sans-0-0-70').text.strip()
                
                
                writer.writerow({'Job Name': job_name, 'Company': company, 'Location': location})
                
                items_processed += 1
            
            print(f"Items processed for {city}: {items_processed}")

print("Data saved to job_data_test.csv")


driver.quit()
