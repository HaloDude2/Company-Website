from django.views.genaric import View
from django.shortcuts import render
from .forms import AppointmentForm

class AppointmentView(View):

    def get(self, request):
        form = AppointmentForm()

        return render(request, "appointments.html", {
            "form": form
        })

    def post(self, request):
        form = AppointmentForm(request.POST)

        if form.is_valid():
            instance = form.save()

            return render(request, "appointments.html", {
                "form": form
                "submitted": instance.__str__()
            })
        else:
            return render(request, "appointments.html", {
                "form": form,
                "errors": form.errors
            })


# Create your views here.
