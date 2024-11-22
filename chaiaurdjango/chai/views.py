
from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety

def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'all_chai.html',{ 'chais':chais})

def chai_detail(request, chai_id):
  chai = get_object_or_404(ChaiVariety, pk=chai_id)
  return render(request, 'chai_detail.html', {'chai': chai})