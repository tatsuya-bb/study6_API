from search_item import search_items
from item_info import item_info
from ranking import ranking
from common import execute_api


def test_execute_api():
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    params = {
        "keyword": "PS5",
        "format": "json",
        "applicationId": "1019079537947262807"
    }
    res = execute_api(url=url, params=params)
    
    # チェック
    # 正常系　→　うまくいった時の処理
    assert len(res["Items"]) >= 1
    assert res["Items"][0]["Item"]["itemCode"]
    

def test_search_items():
    keyword = "PS5"
    res = search_items(keyword)
    
    assert res["Items"]
    assert res["Items"][0]["Item"]["itemName"]
    assert res["Items"][0]["Item"]["itemPrice"]
    
    
def test_item_info():
    keyword = "PS5"
    res = item_info(keyword)
    
    assert res["Products"]
    assert res["Products"][0]["Product"]["minPrice"]
    assert res["Products"][0]["Product"]["maxPrice"]
    

def test_ranking():
    genere_id = "100283"
    res = ranking(genere_id)
    
    assert res["Items"]
    assert res["Items"][0]["Item"]["itemName"]
    assert res["Items"][0]["Item"]["itemPrice"]