from konlpy import tag
import pandas as pd


def file_open(DATA_DIR):
    title_list = None
    try:
        data = pd.read_excel(DATA_DIR, sheet_name='Sheet1')
        title_list = data['text']
    except:
        print("엑셀 파일 열기 실패. 파일을 확인해 주세요.")
    return title_list



def test(titles):
    test_title_list = titles[:20]
    okt = tag.Okt()
    for title in test_title_list:
        print(okt.pos(title))


def decompose(titles):
    okt = tag.Okt()
    for title in titles:
        print(okt.morphs(title))

if __name__ == "__main__":
    test()
