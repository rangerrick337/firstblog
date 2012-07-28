# Create your views here.

from django.shortcuts import render_to_response

from blog.models import posts

def home(request):
	entries = posts.objects.all()[:10]		# returns the most recent 10 entries added to the database
	return render_to_response('index.html', {'posts' : entries})
