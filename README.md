Web Scraping MSIB

![msib picc](https://github.com/haekalmeister/Web-Scraping-MSIB/assets/119827103/6883fb11-c54f-4f2a-a8fa-11cb80b66a23)

The MSIB (Merdeka Student Internship Program) is an initiative under the Merdeka Belajar Kampus Merdeka (MBKM) program launched by the Indonesian Ministry of Education and Culture. The MSIB program aims to provide students with hands-on professional experience through internships in various industries. This initiative is designed to bridge the gap between academic learning and real-world applications, preparing students for the workforce by offering practical experience and industry exposure.

I pulled 7000+ data each which is a list of jobs containing name of the role, company, and location using Selenium and BeautifulSoup. MSIB website (https://kampusmerdeka.kemdikbud.go.id/program/magang/browse/) requires me to use automated scrolling with selenium because the data is not loaded all at once and also there is no hyperlink for pagination. Because of the memory usage problem that is caused by the size of this data (it keeps crashing), I can't scroll all at once. That is why I partitioned the task by city search which I automated with selenium. It reduced memory usage from 13 GB+ to 200 MB. I managed to pull 7000+ data which I loaded into a CSV file.
