from Data_Preprocess.Naver_News_Title_Crawler import downloader

xls_path = '../Data/Crawldata.xlsx'
date = '20190816'
num = 500


downloader.download(num, xls_path, date)





