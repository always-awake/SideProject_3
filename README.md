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

### CBV를 위한 Decorators
- 파이썬의 장식자(Decorators)를 통해 View에 대양한 기능을 더해줄 수 있음
- Decorator 문법은 기본적으로 함수에 대해 동작하지만 클래스에 대해 동작할 수 있게끔 할 수 있음

#### 장식자 (Decorators)
- 어떤 함수를 감싸는(Wrapping) 함수
- 함수 기반 뷰에 장식자를 사용하는 방식 2가지 (두 가지는 동일하게 동작함, 그러나 첫번째 방식을 하용하는 것을 추천)
```
@login_required
def protected_view1(request):
    return render(request, 'myapp/secret.html)
```
#
```
def protected_view2(request):
    return render(request, 'myapp/secret.html)

protected_view2 = login_required(protexted_view2)
```
#### 장고 기본 Decorators 일부
- django.views.decorators.http: 지정 method가 아닐 경우, HttpResponseNotAllowed 응답 반환
  - require_http_method
  - require_GET
  - require_POST
  - require_safe
- django.contrib.auth.decorators
  - user_passes_test: 지정 함수가 False를 반환하면 login_url 로 redirect
  - login_required: 로그아웃 상황에서 login_url로 redirect
  - permission_required: 지정 퍼미션이 없을 때, login_url로 redirect
- django.contrib.admin.views.decorators
  - staff_member_required: staff member가 아닐 경우 login_url로 이동
#### CBV에 장식자 입히기
- @ 를 이용한 장식자 사용 불가
- CBV에 장식자 입히는 방법 1: 가독성이 좋지 않음
```
view_fn = SecretView.as_view()
secret_view = login_required(view_fn)
```
- CBV에 장식자 입히는 방법 2: CBV의 멤버 함수 중 항상 호출되는 dispatch 함수 재정의
```
class SecretView(TemplateView): 
    template_name = 'myapp/secret.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwsrgs):
        return super().dispatch(*args, **kwargs)

secret_view = SecretView.as_view()
```
- (가장 추천)CBV에 장식자 입히는 방법 3: CBV의 멤버 함수 중 항상 호출되는 dispatch 함수에 장식자 적용
```
@method_decorator(login_required, name='dispatch)
class SecretView(TemplateView):
    template_name='myapp/secret.html'

secret_view = SecretView.as_view()
```