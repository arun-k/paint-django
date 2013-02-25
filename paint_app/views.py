# Create your views here.
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from models import Image
def paintapp(request):
    if request.method == 'GET':
        py_all = {}
        all_data = Image.objects.all()
        for each in all_data:
            py_all[each.name] = each.data
        t = get_template('paint.html')
	html = t.render(Context({'py_all':py_all}))
        return HttpResponse(html)
    elif request.method == 'POST':
        file_name = request.POST.get('fname')
        data = request.POST.get('whole_data')
        try:
  	    p = Image.objects.get(name=file_name)
	except Image.DoesNotExist:
    	    p=Image(name=file_name,data=data)
	    p.save()
	else:
    	    p.data=data
	    p.save()
        return redirect('/')
