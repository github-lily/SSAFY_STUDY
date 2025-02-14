import random
from faker import Faker

# Faker 객체 생성
fake = Faker("ko_KR")

# 더미 데이터 개수
num_vendors = 60

# user_id 범위 (예: 기존 데이터에서 user_id 16~75 사용)
user_ids = list(range(16, 76))

# 카테고리 ID (웨딩홀, 스튜디오, 드레스, 메이크업)
category_ids = [1, 2, 3, 4]

# 실제 do_id와 sigungu_code 매핑 (시/도와 시/군/구 관계 유지)
do_sigungu_mapping = {
    1: list(range(1, 26)),   # 서울 (강남구 ~ 중랑구)
    2: list(range(1, 11)),   # 인천 (강화군 ~ 중구)
    3: list(range(1, 6)),    # 대전 (대덕구 ~ 중구)
    4: list(range(1, 9)),    # 대구 (남구 ~ 중구)
    5: list(range(1, 6)),    # 광주 (광산구 ~ 서구)
    6: list(range(1, 17)),   # 부산 (강서구 ~ 해운대구)
    7: list(range(1, 6)),    # 울산 (중구 ~ 울주군)
    8: [1],                  # 세종특별자치시
    31: list(range(1, 32)),  # 경기도 (가평군 ~ 화성시)
    32: list(range(1, 19)),  # 강원도 (강릉시 ~ 횡성군)
    39: list(range(1, 5)),   # 제주도 (남제주군 ~ 제주시)
}

# 사업자 등록번호 생성 함수
def generate_registration_number():
    return f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(10000, 99999)}"

# vendors 테이블의 데이터 생성
vendors = []

for _ in range(num_vendors):
    category_id = random.choice(category_ids)
    do_id = random.choice(list(do_sigungu_mapping.keys()))
    sigungu_code = random.choice(do_sigungu_mapping[do_id])  # do_id에 맞는 sigungu_code 선택
    user_id = random.choice(user_ids)  # 기존 사용자와 연관

    min_price = random.randint(100000, 1500000)
    address_detail = f"{random.randint(1, 10)}층"
    auto_road_address = f"{fake.street_address()}, {fake.city()} {fake.postcode()}"  # 주소 생성
    business_hour = f"{random.randint(8, 11)}:00 - {random.randint(18, 23)}:00"
    details = fake.sentence()

    homepage = f"http://www.{fake.domain_word()}.com"
    name = fake.company()
    owner_name = fake.name()
    owner_phone = f"010-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
    parkinglot = f"주차 가능 {random.randint(10, 100)}대"
    phone = f"0{random.randint(2, 6)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
    price = f"홀 대여 {random.randint(500000, 2000000)}원, 식대 {random.randint(30000, 80000)}원"
    registration_number = generate_registration_number()
    subway = f"{fake.city()}역 {random.randint(1, 5)}호선"
    zonecode = random.randint(10000, 99999)

    vendors.append(
        (
            category_id, do_id, "_binary '\\0'", min_price, sigungu_code, user_id, address_detail,
            auto_road_address, business_hour, details, homepage, name, owner_name, owner_phone,
            parkinglot, phone, price, registration_number, subway, zonecode
        )
    )

# SQL INSERT 문 생성
insert_sql = "INSERT INTO vendors (\n" \
             "    category_id, do_id, is_indoor, min_price, sigungu_code, user_id, address_detail, auto_road_address,\n" \
             "    business_hour, details, homepage, name, owner_name, owner_phone, parkinglot, phone, price,\n" \
             "    registration_number, subway, zonecode\n) VALUES\n"

values_sql = ",\n".join(str(record) for record in vendors)

insert_sql += values_sql + ";"

# SQL 출력
print(insert_sql)
