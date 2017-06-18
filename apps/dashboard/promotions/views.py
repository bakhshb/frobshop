from oscar.apps.dashboard.promotions.views import PageDetailView as CorePageDetailView
from django.shortcuts import HttpResponse

class PageDetailView (CorePageDetailView):
	def post(self, request, **kwargs):
		data = dict(request.POST).get('promo')
		self._save_page_order(data)
		return HttpResponse(status=200) 