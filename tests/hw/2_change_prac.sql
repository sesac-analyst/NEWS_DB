ALTER TABLE {테이블명}
CHANGE COLUMN {기존 컬럼명} {바꿀 컬럼명} {컬럼 타입};

ALTER TABLE {테이블명}
ADD CONSTRAINT {제약조건 이름} UNIQUE {컬럼명};

ALTER TABLE {테이블명}
MODIFY COLUMN {컬럼명} {컬럼타입} NOT NULL;

1. tbr_publisher의 pub_name -> name으로 수정
ALTER TABLE tbr_publisher
CHANGE COLUMN pub_name name VARCHAR(8); #컬럼타입 추가?

2. tbr_article의 article_url -> NOT NULL UNIQUE 제약조건 추가
ALTER TABLE tbr_article
ADD CONSTRAINT unique_article_url UNIQUE (article_url);

ALTER TABLE tbr_article
MODIFY COLUMN article_url VARCHAR(255) NOT NULL;

3. tbr_user의 user_unique -> NOT NULL UNIQUE 제약조건 추가
ALTER TABLE tbr_user
ADD CONSTRAINT unique_user UNIQUE (user_unique);

ALTER TABLE tbr_user
MODIFY COLUMN user_unique VARCHAR(255) NOT NULL;