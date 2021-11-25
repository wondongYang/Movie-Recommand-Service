# Movie-Recommend-Service
영화 추천, 리뷰 서비스 제작

# 팀원 정보

양원동 (ehd8331@gmail.com)

- django 초기 설정 구현
- tmdb DB 데이터 수집 및 전처리
- vue carousel, pagination, navbar toggler 등 추가 기능 구현

조성한 (chosnhn1@gmail.com / toor21@naver.com)

- vue 초기 설정 구현

- django 알고리즘 구현(home, recommend)
- 로그인 기능 구현 (jwt토큰, 경고문구, 제한조건)
- search 기능 구현



# 목표 서비스 구현

## 기획 단계 ERD

![initial-Movie App drawio](https://user-images.githubusercontent.com/55439547/143378494-7257384e-cb9d-4226-b587-d197d1c2551f.png)

## 영화 정보 탑재

- TMDB Popular 데이터 이용
- 영화 배우 정보를 통한 추천 알고리즘 구현 계획 (미구현)

## 커뮤니티 서비스

- 영화 리뷰 작성, 리뷰 좋아요 기능, 리뷰 댓글 작성 구현
- 커뮤니티 서비스 정보를 통한 추천 알고리즘 구현

# ERD

![after-Movie App drawio](https://user-images.githubusercontent.com/55439547/143378525-57376966-110b-4bdd-9166-81e1271d0549.png)



# 기능

## 메인 Page
![메인 page](https://user-images.githubusercontent.com/66405226/143386381-cab724e9-5f8b-489f-b494-19bee409f420.JPG)

## 커뮤니티 기능

SoySource에서는 모든 사용자들이 리뷰와 댓글을 읽을 수 있습니다. 서비스에 가입한 사용자들은 리뷰를 작성하고, 리뷰에 대한 댓글을 작성하며 영화와 리뷰에 '좋아요'를 표현할 수 있습니다. 

### 리뷰 작성 기능

인증된 사용자는 SoySource의 각 영화별 상세 정보 페이지를 통해 리뷰 작성 기능에 접근할 수 있으며, 각 리뷰는 기본적으로 영화별 상세 페이지에 노출됩니다. 리뷰를 작성한 사용자는 자신의 리뷰를 수정하고 삭제할 수 있습니다.

![리뷰작성기능](https://user-images.githubusercontent.com/66405226/143386504-b459b37d-41b8-4b08-8d01-5a8023a4ce5c.JPG)

### 댓글 작성 기능

인증된 사용자는 SoySource에 탑재된 리뷰에 댓글을 작성할 수 있습니다. 댓글을 작성한 사용자는 자신의 댓글을 수정하거나 삭제할 수 있습니다.

### 영화 / 리뷰 '좋아요' 기능

인증된 사용자들은 SoySource의 영화와 리뷰에 '좋아요'를 표시할 수 있습니다. '좋아요'는 영화 한 편 / 리뷰 한 건 당 한 번 표시할 수 있으며, 사용자는 자신이 표시한 '좋아요'를 기반으로 영화 추천을 받을 수 있습니다.

![댓글작성기능](https://user-images.githubusercontent.com/66405226/143386521-31e0f59f-0aac-4655-b63f-ab307517a32f.JPG)

### 프로필 기능

SoySource에서 인증된 사용자들은 각자의 프로필 페이지를 갖게 됩니다. 사용자는 프로필 페이지에서 자신이 '좋아요' 표시한 영화와 리뷰 목록, 자신이 작성한 리뷰와 댓글 목록을 확인할 수 있습니다.

![프로필기능](https://user-images.githubusercontent.com/66405226/143386540-c1c87883-ec44-4ac9-8a6d-82559a2bddd3.JPG)

## 영화 데이터베이스

### 영화 정보 기능

SoySource는 TMDB API를 사용하여 10,000여 건의 영화 정보를 데이터베이스에 탑재하고 있습니다. 해당 영화 정보에 대한 자세한 내용은 ERD란에 설명되어 있습니다.

![영화정보기능](https://user-images.githubusercontent.com/66405226/143386556-d743ef51-b37d-47f7-aa8f-156ab32b17f0.JPG)

### 영화 검색 기능

모든 이용자는 TMDB에서 제공하는 인기 영화 목록을 DB에 탑재한 SoySource에서 제목에 기반하여 영화 검색 기능을 사용할 수 있습니다.

![영화검색기능](https://user-images.githubusercontent.com/66405226/143386568-0b77a802-d44e-4dbe-9c99-4cdc9535fb94.JPG)

### 영화 추천 기능

SoySource는 사용자가 '좋아요'를 표시한 영화 정보를 기반으로 영화 데이터베이스의 장르 정보를 활용하여 사용자에게 개인화된 영화 추천 기능을 제공합니다.

![영화추천기능](https://user-images.githubusercontent.com/66405226/143386573-4ba22851-44dd-442f-8f48-47fd79a0af98.JPG)


# 배포
django server: http://3.19.70.45/
vue client: https://tender-bell-02c22f.netlify.app/

