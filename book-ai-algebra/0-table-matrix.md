- 정보를 담은 데이터는 결국 “행 × 열”의 행렬 구조로 저장됨
 - 사칙연산을 이용하기 위해, 정보를 **표 형태** (DB table, Excel, JSON 등)에서, **행렬 형태**로 변환하여 해석
	 - 평균, 합산 → 행렬 연산
	 - 유사도 비교 → 내적
	 - 정렬 → 고유값, 특이값
	 - 차원축소 → PCA

### 표 형태

- SQL table → 행: 데이터 레코드 (record), 열: 속성 (feature)
```sql
 SELECT * FROM Students;
```

|id|name|math|english|
|---|---|---|---|
|1|John|85|90|
|2|Alice|92|88|

- JSON (NoSQL) object array → nested → 펼치면 행렬
```json
[
  {"id": 1, "scores": {"math": 85, "english": 90}},
  {"id": 2, "scores": {"math": 92, "english": 88}}
]
```

- Vector DB (embedding 형태): 벡터 집합 = 행렬

```json
[
  {"id": 1, "embedding": [0.11, 0.98, -0.52, ...]},
  {"id": 2, "embedding": [0.43, -0.12, 0.77, ...]}
]
```

