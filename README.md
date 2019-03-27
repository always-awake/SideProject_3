# SideProject_3
- Django의 View는 클라이언트로부터 요청을 처리하는 'Callable Object'
- View는 함수로 구현할 수도 있고, 클래스로도 구현할 수 있음
- API를 만들 때 주로 사용하는 'django-rest-framework' 역시 CBV의 한 종류

### 01. OverView
#### View
- 호출 가능한 객체 (Callable Object)
- 종류
  - 함수 기반 뷰 (Function Based View)
  - 클래스 기반 뷰 (Class Based View)

#### Class Based View
- View 함수를 만들어주는 클래스
  - as_view() 클래스 함수를 통해, View함수 생성
- 장고 기본 CBV 패키지
  - django.views.generic
- 써드파티 CBV
  - django-braces
- CBV가 정한 관례대로 개발할 경우, 아주 적은 양의 코드로 구현
  - 필요한 설정값을 제공하거나, 특정 함수를 재정의 하는 방식으로 커스텀 가능
  - 하지만, 그 관례를 잘 이해하지 못하고 사용하거나, 그 관례에서 벗어난 구현을 하고자 할 때에는 복잡해지는 경향이 있음
- 