from django.shortcuts import render, redirect
from django.views.generic import TemplateView, RedirectView

# 함수 기반 뷰 
# def myview(request):
#     context = {
#         'hello': 'world',
#         'ip': request.META['REMOTE_ADDR'],
#     }
#     return render(request, 'myapp/myview.html', context)

# 클래스 기반 뷰 (Base View 중 TemplateView)
class MyTemplateView(TemplateView):
    template_name = 'myapp/myview.html'

    # ContextMixin의 get_context_data 함수 재정의
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'hello': 'world',
            'ip': self.request.META['REMOTE_ADDR']
        })
        return context

# MyTemplateView의 인스턴스 myview
myview = MyTemplateView.as_view()


# 함수 기반 뷰
# def myview2(request):
#     return redirect('https://m.naver.com')

myview2 = RedirectView.as_view(
    url='https://m.naver.com',
)