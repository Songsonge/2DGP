# 2DGP
## 쿠키런[CookieRun]

![CookieRun_image](https://thumb.mt.co.kr/06/2013/07/2013071215201596920_1.jpg/dims/optimize/)
- 점프와 슬라이드로 조작을 하며 스크린의 장애물들을 피해 달리면서 젤리를 먹어 점수를 올리는 게임

### GameState
GameScene 4개
1) 로고 화면
2) 타이틀 화면
3) 플레이 화면
4) 점수 화면

#### GameScene 설명

1. 로고화면
- 쿠키런 로고 생성
- 스페이스 입력으로 타이틀 화면으로 전환
2. 타이틀 화면
- 쿠키(캐릭터) 설정 화면
- 구성: 게임 시작 버튼, 게임 종료 버튼
- 게임 시작 버튼을 마우스 클릭으로 플레이 화면으로 전환
3. 플레이 화면
- 쿠키가 달리면서 젤리를 얻는다.
- 구성: 쿠키(캐릭터), 젤리(점수), hp바, 맵, 장애물, 점수표, 배경
- 달리기: 자동, 스페이스바: 점프, s: 슬라이딩
- hp가 0이 되거나 맵이 끝나면 점수 화면으로 전환
4. 점수 화면
- 플레이해서 얻은 점수 띄워줌
- 스페이스 입력으로 타이틀 화면으로 전환

### 필요한 기술
- 캐릭터 포커싱되어 그려지는 x좌표 고정
- 캐릭터 움직임에 따른 배경 변화
- 날아오는 장애물 구현
- 장애물 충돌체크
