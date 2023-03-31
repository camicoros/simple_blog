from django.views.generic import TemplateView


# это в качестве примера, данные нужно получать из базы))
POSTS = [
    {'title': "Как я купил дом", 'id': 1},
    {'title': "Как я купил дачу", 'id': 2},
    {'title': "Как я купил машину", 'id': 3},
    {'title': "Как я купил кошку", 'id': 4},
    {'title': "Как я купил крабовые палочки", 'id': 5},
]


class IndexView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = POSTS
        return context


class DetailView(TemplateView):
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = kwargs.get('post_id')
        context['post'] = next(item for item in POSTS if item["id"] == post_id)
        return context

