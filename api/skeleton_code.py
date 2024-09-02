from typing import Dict, Optional, Union

import pymysql
from pymysql.connections import Connection
from pymysql.cursors import Cursor, DictCursor

import pandas as pd

"""
사용할 라이브러리 : pymysql, pandas

요구사항
1. 클래스 내 insert, select 함수 구현
2. 삽입에 대한 테스트 케이스 커버

참고할 코드 (insert_many, select 부분)
https://github.com/devsosin/sosin/blob/main/sosin/databases/rdb/maria.py
"""

class ColumnNotMatchException(BaseException):
    ...

class NewsDB:
    """
    클래스 설명
    """

    DB: Connection
    cursor: Union[Cursor, DictCursor] = Cursor

    def __init__(self, db_config: Dict[str, str], cursor_type:Optional[DictCursor]=None) -> None:
        """
        데이터베이스 접속
        
        **db_config**
            host=database host (localhost)
            port=port (3306)
            user=username (root)
            password=password (1q2w3e)
            database=database name (testdb)
            charset=charcter encoding (utf8mb4)
        """
        self.db_config = {**db_config, 
                          'port': int(db_config.get('port', 3306))}
        self.cursor_type = cursor_type

        # 플랫폼 정보
        self.PLATFORM_DICT = {
            '네이버': 1,
            '다음': 2
        }
        
        # main_category
        self.MAIN_CATEGORY_DICT = {

        }

        # sub_category
        self.SUB_CATEGORY_DICT = {

        }

    def __enter__(self) -> Connection:
        """
        Usage:
        ```py
        db = Database(config)
        with db: # as db_object
            ...
        ```
        """
        return self.connect()
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.disconnect()
    
    def connect(self):
        """
        데이터베이스 접속
        """
        self.DB = pymysql.connect(**self.db_config)
        self.cursor = self.DB.cursor(cursor=self.cursor_type)
        return self

    def __del__(self) -> None:
        """
        데이터베이스 연결 해제
        """
        try:
            self.disconnect()
        except:
            ...
            
    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        self.DB.close()

    def insert_news(self, news_df: pd.DataFrame) -> bool:
        """
        news_df : 뉴스기사 데이터프레임
        
        예외 처리사항
        1. 데이터프레임의 column명이 News 테이블의 **필수** 칼럼들과 일치하지 않을 경우 에러
            - ColumnNotMatchException을 발생시키면 됩니다. 메시지는 자유

        insert SQL문 생성
        execute 대신 execute_many 메서드로 한번에 삽입

        1. 플랫폼 정보 id로 변환
        2. 메인카테고리 숫자로 변환
        3. 서브카테고리 숫자로 변환
        4. DB에 적재

        반환 값 : 성공 True, 실패 False

        """
        pass

    def insert_comment(self, comment_df) -> bool:
        """
        comment_df : 댓글 데이터프레임

        예외 처리사항
        1. 데이터프레임의 column명이 News 테이블의 **필수** 칼럼들과 일치하지 않을 경우 에러
            - ColumnNotMatchException을 발생시키면 됩니다. 메시지는 자유

        댓글을 삽입하는 로직은 좀 더 복잡함.
        1. 대체를 위한 pk 값 가져오기
            1. 뉴스기사 존재여부 체크 (url, 플랫폼이 부여한 id, 테이블에 있는 것과 비교)
                - 기사 url을 데이터베이스상의 id로 변환
                - 해당 딕셔너리를 통해 column 대체
            2. 유저 존재여부 체크
                - 없다면, 새로 insert
                - user를 고유하게 분류할 수 있는 값을 통해 id로 변환
                - 해당 딕셔너리를 통해 column 대체

        2. DB에 적재

        반환 값 : 성공 True, 실패 False
        """

    def select_news(self) -> pd.DataFrame:
        """
        인자 : 직접 설정 (select 할 때 필터링, 정렬, 페이징 할 때 필요한 것들)
        (어떻게 검색(필터)해서 뉴스기사를 가져올 것인지)

        DB에 들어있는 데이터를 꺼내올 것인데, 어떻게 꺼내올지를 고민

        인자로 받은 파라미터 별 조건을 넣은 select SQL문 작성

        SQL문에 추가할 내용들
        1. 가져올 칼럼
        2. JOIN할 경우 JOIN문 (플랫폼, 카테고리)
        3. WHERE 조건문
        4. LIMIT, OFFSET 등 처리

        반환 자료형 : 데이터프레임
        """
        pass

    def select_user(self) -> pd.DataFrame:
        """
        인자 : 데이터를 꺼내올 때 사용할 parameters
        (어떻게 검색(필터)해서 유저를 가져올 것인지)

        SQL문에 추가할 내용들
        1. 가져올 칼럼
        2. JOIN할 경우 JOIN문
        3. WHERE 조건문
        4. LIMIT, OFFSET 등 처리

        반환 자료형 : 데이터프레임
        """
    
    def select_comment(self) -> pd.DataFrame:
        """
        인자 : 데이터를 꺼내올 때 사용할 parameters
        (어떻게 검색(필터)해서 댓글을 가져올 것인지)

        SQL문에 추가할 내용들
        1. 가져올 칼럼
        2. JOIN할 경우 JOIN문 (유저정보를 같이 가져올 경우)
        3. WHERE 조건문
        4. LIMIT, OFFSET 등 처리

        반환 자료형 : 데이터프레임
        """

# ------------------------------------------------------------
# 테스트 코드 (수정 X)

def get_db():
    db_configs = {
        'host': 'localhost',
        'port': '3306',
        'user': 'news',
        'password': '1q2w3e',
        'database': 'newsdb',
        'charset': 'utf8mb4',
    }

    db = NewsDB(db_configs)
    return db

def reset_db():
    db = get_db()

    with db:
        db.cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        db.cursor.execute("TRUNCATE TABLE tbr_article;")
        db.cursor.execute("TRUNCATE TABLE tbr_sticker;")
        db.cursor.execute("TRUNCATE TABLE tbr_user;")
        db.cursor.execute("TRUNCATE TABLE tbr_comment;")
        db.cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
        db.DB.commit()

def test(func):
    def wrapper(*args, **kwargs):
        try:
            r = func(*args, **kwargs)
        except Exception as e:
            import traceback
            traceback.print_exc()
            r = None
        finally:
            reset_db()

        return r
    
    return wrapper

# 테스트케이스
@test
def test_connection():
    db = get_db()

    with db:
        db.cursor.execute('SELECT 1')
        result = db.cursor.fetchone()

    return result

@test
def test_news_columns():
    db = get_db()

    news_df = pd.read_excel('../tests/test_news_no_column.xlsx')
    with db:
        try:
            result = db.insert_news(news_df)
        except ColumnNotMatchException as e: 
            # 예외 발생하면 성공
            return True

    # 성공하면 안됨.
    raise Exception('칼럼 매치 검증 테스트 실패')

@test
def test_insert_news():
    db = get_db()

    news_df = pd.read_excel('../tests/test_news.xlsx')

    # 정상적 insert
    with db:
        result = db.insert_news(news_df)
        if not result:
            raise Exception('데이터 삽입 실패')
            return
        # url 등 확인할 수 있는 칼럼만 확인
        db.cursor.execute("SELECT article_url FROM TB_NEWS ORDER BY -id LIMIT {}".format(len(news_df)))
        news = [v[0] for v in db.cursor.fetchall()]

        # 데이터 삽입 여부 unique한 url로 체크
        if [url for url in news_df['article_url'] if url not in news]:
            raise Exception('삽입된 데이터가 일치하지 않습니다.')
            return

    return result


@test
def test_comment_columns():
    db = get_db()

    comment_df = pd.read_excel('../tests/test_comment_no_column.xlsx')

    try:
        result = db.insert_comment(comment_df)
    except ColumnNotMatchException as e: 
        # 예외 발생하면 성공
        return True
    
    # 성공하면 안됨.
    raise Exception('칼럼 매치 검증 테스트 실패')

@test
def test_insert_comment():
    db = get_db()

    comment_df = pd.DataFrame()

    # 정상적 insert
        # - 신규 유저 삽입여부 체크
        # 유저 셀렉트 있는지 없는지

        # - 신규 댓글 삽입여부 체크
        # 댓글 셀렉트

    with db:
        result = db.insert_comment(comment_df)
        
        if not result:
            raise Exception('데이터 삽입 실패')
        
    # 확인할 수 있는 것
    with db:
        user_unique = set(comment_df['user'].unique())
        db.cursor.execute("SELECT user_name FROM TBR_USER ORDER BY -id LIMIT {}".format(len(user_unique)))
        users = set([v[0] for v in db.cursor.fetchall()])
        if user_unique - users:
            raise Exception('삽입되지 않은 유저가 있습니다.')
        
    with db:
        db.cursor.execute("SELECT * FROM TBR_COMMENT ORDER BY -id LIMIT {}".format(len(comment_df)))
        comments = db.cursor.fetchall()
        # 삽입된 데이터 수가 맞지 않을 경우
        if len(comments) != len(comment_df):
            raise Exception('삽입된 데이터 수가 다릅니다.')
    
    return result

# SELECT 테스트는 애매

@test
def test_select_news_by_platform():
    db = get_db()

    # select 사항에 따라서 전부 작성

    # 카테고리 체크

    # 페이지네이션 체크

    # 댓글 체크

    with db:
        result = db.select_news(platform='네이버')

    expected = ''
    
    if result != expected:
        ...
    
    return expected

@test
def test_select_comment():
    db = get_db()

    # select 사항에 따라서 전부 작성

    with db:
        result = db.select_comment()

    expected = ''
    
    if result != expected:
        ...
    
    return expected

@test
def test_select_user():
    db = get_db()

    # select 사항에 따라서 전부 작성

    with db:
        result = db.select_user()

    expected = ''
    
    if result != expected:
        ...
    
    return expected

if __name__ == '__main__':
    # 테스트
    passed = 0
    failed = 0

    test_cases = [test_connection,
                  test_news_columns, 
                  test_comment_columns,
                  test_insert_news, test_insert_comment, 
                #   test_select_news_by_platform, 
                #   test_select_comment, 
                #   test_select_user
                  ]
    for test_case in test_cases:
        if test_case():
            passed += 1
        else:
            failed += 1

    print(f'Test Passed: {passed}\nTest Failed: {failed}')
