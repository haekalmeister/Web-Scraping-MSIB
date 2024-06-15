Web-Scraping-MSIB
![msib picc](https://github.com/haekalmeister/Web-Scraping-MSIB/assets/119827103/6883fb11-c54f-4f2a-a8fa-11cb80b66a23)
I pulled data from the MSIB website to get 7000+ job lists using Selenium and BeautifulSoup. MSIB website (https://kampusmerdeka.kemdikbud.go.id/program/magang/browse/) requires me to use automated scrolling with selenium because the data is not loaded all at once and also there is no hyperlink for pagination. Because of the memory usage problem that is caused by the size of this data (it keeps crashing), I can't scroll all at once. That is why I partitioned the task by city search which I automated the iteration. It reduced memory usage from 13 GB+ to 200 MB. I managed to pull 7000+ data which I loaded into a CSV file.
