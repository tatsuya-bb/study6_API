import requests

def execute_api(url: str, params:dict):
    '''
    APIの実行
    (楽天APIだけではなく汎用的に活用可能)
    '''
    # APIを実行（GETリクエスト）
    res = requests.get(url, params=params)
    
    # 結果が失敗の場合はNoneを返す
    if not(300 > res.status_code >= 200):
        return None
    
    # 結果のjsonをdict化して返す
    return res.json()