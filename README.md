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

### Base Views
- CBV의 기본 클래스 View, TemplateView, RedirectView 클래스
- 위치: django/views/generic/base.py
- https://github.com/django/django/blob/2.1/django/views/generic/base.py
- View
- TemplateView (TemplateView는 아래 목록 클래스를 상속받아 추가적인 로직 구현)
  - TemplateResponseMixin
  - ContextMixin
  - View
- RedirectView (RedirectView는 View 클래스를 상속받아 추가적인 로직 구현)
  - View

#### View
- 모든 CBV의 모체 (이 CBV를 직접 사용할 일은 거의 없음)
- http method 별로 지정 이름의 멤버 함수를 호출하도록 구현됨
- CBV.as_view(**initkwargs)
  - initkwargs 인자는 그대로 CBV 생성자로 전달됨
- as_view
  - 함수를 만들어 주는 클래스 메소드
  - as_view 함수는 내부적으로 view란 이름을 갖고 있는 함수를 생성하여 리턴

### Generic display views
- 기본 조회 View인 DetailView, ListView

#### DetailView 상속 관계
- SingleObjectTemplateResponseMixin 상속: Teamplate 경로 생성 이후 작업은 TemplateTrsponseMixin에서 마저 처리
  - TemplateResponseMixin 상속: template이 지정되면, view응답 생성
- BaseDetailView 상속
  - SingleObjectMixin 상속: 오브젝트 획득 지원
  - View 상속: Http Method에 따라 관련 멤버 함수 호출
#### DetailView
- 1개 모델의 1개 Object에 대한 템플릿 처리
- 모델명 소문자 이름의 Model Instance를 템플릿에 전달
  - 지정 pk 혹은 slug에 대응하는 Model Instance

#### ListView 상속 관계
- MultipleObjectTemplateResponseMixin 상속: Teamplate 경로 생성 이후 작업은 TemplateTrsponseMixin에서 마저 처리
  - TemplateTrsponseMixin 상속: template이 지정되면, view응답 생성
- BaseListView
  - MultipleObjectMixin상속 (ContextMixin 상속): 다수의 오브젝트 획득 지원
  - View 상속: Http Method에 따라 관련 멤버 함수 호출
#### ListView
- 1개 모델에 대한 List 템플릿 처리
  - '모델명 소문자_list' 이름의 QuerySet을 템플릿에 전달
- 페이징 처리 지원
```
post_list2 = ListView.as_view(model=Post, paginate_by=10)
```
#
```
class PostListView(ListView):
    model = Post
    paginate_by = 10

post_list3 = PostListView.as_view()
```