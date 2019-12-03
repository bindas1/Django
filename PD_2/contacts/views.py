from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, View

from contacts.forms import PersonForm
from contacts.models import Person


class ContactView(TemplateView):
    template_name = 'contacts/view.html'

    def get_context_data(self, **kwargs):
        return {
            'contacts': Person.objects.all()
        }


class ContactAddForm(TemplateView):
    template_name = 'contacts/form.html'

    def get_context_data(self, **kwargs):
        form = PersonForm()
        return locals()


class ContactAddFail(TemplateView):
    template_name = 'contacts/fail.html'


class ContactAddSuccess(TemplateView):
    template_name = 'contacts/success.html'


class ContactAddView(View):
    def get(self, request):
        return HttpResponseRedirect(reverse('contact-add-fail'))

    def post(self, request):
        form = PersonForm(request.POST)

        if not form.is_valid():
            return HttpResponseRedirect(reverse('contact-add-fail'))

        Person.objects.create(
            first_name=form.cleaned_data.get('first_name'),
            last_name=form.cleaned_data.get('last_name'),
            gender=form.cleaned_data.get('gender')
        )

        return HttpResponseRedirect(reverse('contact-add-success'))
