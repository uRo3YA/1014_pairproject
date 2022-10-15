# 1014_project

## 프로젝트 기간

2022.10.14

## 사용 기술

- 언어: HTML, CSS, JavaScript, Python
- 라이브러리: urllib, re, request, bs4
- 프레임워크: Django

## 개발 내용

1. 회원 가입
   
   1. CustomUserCreationForm를 이용한 회원 가입
   2. CustomUserChangeForm를 이용한 회원 정보 수정
   3. AuthenticationForm을 통한 로그인 기능

2. 영화 정보 크롤링
   
   1. 네이버 영화 정보를 크롤링
   
   2. 제목과 썸네일은 긁어오지만 내용은 동작안함
      
      - 각 영화별로 태그가 통일이 안된 상태
   
   3. 영화 세부 페이지, 리뷰 작성 기능 구현

3. 리뷰 작성
   
   1. 크롤링한 각 영화별 리뷰 생성   
   2. accouts앱에서 생성한 유저 정보를 같이 기록
   3. 로그인 여부, 작성자와 일치한 경우에 따라 리뷰 수정 및 삭제 기능

## 배운 점

- 크롤링한 데이터를 DB에 저장하고 활용하는 방법
- Django Model에서 Foreign Key를 활용하는 방법
- ModelForm에서 별점 기능을 구현하는 방법 등

## 미흡한 점

- 각 기능별 페이지 이동 방식에 대한 기획 필요
