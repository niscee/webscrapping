from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source,'lxml')

csv_file = open('cms_scrap.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['HEADER','SUMMARY','LINK'])

for i,article in enumerate(soup.find_all('article'),start=1):

  print(f'{i}...')
  HEADER = article.h2.a.text
  print(f'heading: {HEADER}')

  SUMMARY = article.find('div',class_='entry-content').p.text
  print(f'summary: {SUMMARY}')


  try:
    video_src = article.find('iframe',class_='youtube-player')['src']
    video_id = video_src.split('/')[4]
    video_id = video_id.split('?')[0]
    LINK = f'https://youtube.com/watch?v={video_id}'
    print(f'Link: {LINK}')

  except Exception as e:
      youtube_link = 'NULL'
      print(f'Link: {youtube_link}')
  print('')

  csv_writer.writerow([HEADER,SUMMARY,LINK])

csv_file.close()