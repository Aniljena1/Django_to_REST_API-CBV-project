
from django.shortcuts import render
from django.views import generic
from .models import Employee

class EmployeeListView(generic.ListView):
    model = Employee
    # template_name = 'employee_list.html'
    # context_object_name = 'employee_list'

class EmployeeDetailView(generic.DetailView):
    model = Employee
    # template_name = 'employee_detail.html'
    # context_object_name = 'object or employee'

class EmployeeCreateView(generic.CreateView):
    model = Employee
    fields = '__all__'

    # template_name = 'employee_form.html'
    # context_object_name = 'form'

class EmployeeUpdateView(generic.UpdateView):
    model = Employee
    fields = '__all__'

    # template_name = 'employee_form.html'
    # context_object_name = 'form'

class EmployeeDeleteView(generic.DeleteView):
    model = Employee
    success_url = '/employee'
    # template_name = 'employee_confirm_delete.html'
    # context_object_name = 'object'

# ============   ***********     **********  ===========





# from django.http import HttpResponse
# import requests
# def ContactListView(request):
#     response = requests.get('http://127.0.0.1:9944/api/emp/')
#     return HttpResponse('<h1><font color="blue">' + response.text + '</font>'
#                         + '<br><font color="red"> Status code is :'
#                         + str(response.status_code) + '<br> Data Displayed</h1>')



from django.http import HttpResponse
import json
import requests

# getting all records from partner app
def ContactListView(request):
    response = requests.get('http://127.0.0.1:9944/api/emp/')
    if response.status_code==200:
        context = {
            'contacts_list':json.loads(response.text)
        }
        return render(request, 'contacts/contact_list.html',context )







# getting id based record from partner app
def ContactDetailView(request,pk):
    response = requests.get('http://127.0.0.1:9944/api/emp/'+ str(pk))

    if response.status_code == 200:
        context = {
            'contact': json.loads(response.text)
        }
        return render(request, 'contacts/contact_detail.html', context)

    else:
        context = {
            'nocontact': json.loads(response.text)
        }
        return render(request, 'contacts/contact_detail.html', context)



# Deleting id based record from partner app
def ContactDeleteView(request,pk):
    response = requests.delete('http://127.0.0.1:9944/api/emp/'+ str(pk))

    if response.status_code == 204:
        context = {
            'contact': 'Record deleted Succesfully'
        }
        return render(request, 'contacts/contact_confirm_delete.html', context)

    else:
        context = {
            'nocontact': 'Record not available to delete'
        }
        return render(request, 'contacts/contact_confirm_delete.html', context)









from .models import Employee
from .forms import ContactForm

def ContactCreateView(request):
    if request.method=='POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            eid = request.POST.get('eid','')
            ename = request.POST.get('ename','')
            eemail = request.POST.get('eemail','')
            econtact = request.POST.get('econtact','')

            payload ={
                'eid' : eid,
                'ename':ename,
                'eemail':eemail,
                'econtact':econtact
            }
            response = requests.post('http://127.0.0.1:9944/api/emp/',data=payload)
            if response.status_code==201:
                context = {
                    'form':json.loads(response.text)
                }
                return render(request,'contacts/contact_form.html',context)
            else:
                context = {
                    'notcreated': json.loads(response.text)
                }
                return render(request, 'contacts/contact_form.html', context)


        else:
            return HttpResponse('not valid')
    else:
        form = ContactForm()
        return render(request,'contacts/contact_form.html',{'form':form})



def ContactUpdateView(request,pk):
    if request.method=='POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            eid = request.POST.get('eid', '')
            ename = request.POST.get('ename', '')
            eemail = request.POST.get('eemail', '')
            econtact = request.POST.get('econtact', '')

            payload = {
                'eid': eid,
                'ename': ename,
                'eemail': eemail,
                'econtact': econtact
            }
            response = requests.put('http://127.0.0.1:9944/api/emp/' + str(pk) + '/', data=payload)

            if response.status_code == 200:
                context = {
                    'updated': json.loads(response.text)
                }
                return render(request, 'contacts/contact_update_confirm.html', context)
            else:
                context = {
                    'notupdated': json.loads(response.text)
                }
                return render(request, 'contacts/contact_update_confirm.html', context)

        else:
            return HttpResponse('Not valid')


    else:
        response = requests.get('http://127.0.0.1:9944/api/emp/'+ str(pk))
        if response.status_code==200:
            context = {
                'form' : json.loads(response.text)
            }
            return render(request,'contacts/contact_update.html',context)
        else:
            context = {
                'nodata': json.loads(response.text)
            }
            return render(request, 'contacts/contact_update.html', context)

















# def ContactCreateView(request):
#     if request.method=='POST':
#         form = ContactForm(request.POST)
#
#         if form.is_valid():
#             eid = request.POST.get('eid','')
#             ename = request.POST.get('ename','')
#             eemail = request.POST.get('eemail','')
#             econtact = request.POST.get('econtact','')
#
#             payload = {
#                 'eid': eid,
#                 'ename':ename,
#                 'eemail':eemail,
#                 'econtact':econtact
#             }
#             response = requests.post('http://127.0.0.1:9944/api/emp/', data=payload)
#
#             if response.status_code==201:
#                 context = {
#                     'created' : json.loads(response.text)
#                 }
#                 return render(request,'contacts/create.html',context)
#             else:
#                 context = {
#                     'notcreated' : json.loads(response.text)
#                 }
#                 return render(request,'contacts/create.html',context)
#
#         else:
#             return HttpResponse('data not saved')
#     else:
#         form = ContactForm()
#         return render(request,'contacts/contact_form.html',{'form':form})
#











# def ContactUpdateView(request,pk):
#     if request.method=='POST':
#         print('h1')
#         form = ContactForm(request.POST)
#         print('h2')
#
#         if form.is_valid():
#             print('h3')
#             eid = request.POST.get('eid','')
#             ename = request.POST.get('ename','')
#             eemail = request.POST.get('eemail','')
#             econtact = request.POST.get('econtact','')
#
#             payload = {
#                 'eid': eid,
#                 'ename':ename,
#                 'eemail':eemail,
#                 'econtact':econtact
#             }
#             print('h4')
#             response = requests.put('http://127.0.0.1:9944/api/emp/'+ str(pk)+'/', data=payload)
#             print('h5')
#
#             if response.status_code==200:
#                 print('h6')
#                 context = {
#                     'form' : json.loads(response.text)
#                 }
#                 return render(request,'contacts/contact_update_confirm.html',context)
#             else:
#                 print('status code :' , response.status_code)
#                 print('h7')
#                 context = {
#                     'noform' : json.loads(response.text)
#                 }
#                 return render(request,'contacts/contact_update_confirm.html',context)
#
#         else:
#             return HttpResponse('data not saved')
#
#     else:
#         response = requests.get('http://127.0.0.1:9944/api/emp/'+ str(pk))
#         if response.status_code==200:
#             context = {
#                 'form': json.loads(response.text)
#             }
#             return render(request,'contacts/contact_update.html',context)
#         else:
#             context = {
#                 'noform' : 'Data not available to Update.'
#             }
#             return render(request,'contacts/contact_update.html',context)





