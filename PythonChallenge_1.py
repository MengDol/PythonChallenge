import requests
import pandas as pd

# API URL
url = "https://steamspy.com/api.php"

# 요청 파라미터
params = {"request": "top100in2weeks"}

# API 호출
response = requests.get(url, params=params)

# 데이터 처리
data = response.json()
df = pd.DataFrame(data).T  # 전치(transpose)
df = df.reset_index(drop=True)  # 인덱스 재설정

# 데이터프레임 출력
data = pd.DataFrame(df)

data.head(5)
