from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def place_impressions(request):
    context = {
        'menu': ['acquisition-menu', '新增'],
        'menu2': ['place-impressions', '渠道曝光']
    }
    return render(request, 'place-impressions.html', context)


@login_required
def place_quality(request):
    context = {
        'menu': ['acquisition-menu', '新增'],
        'menu2': ['place-quality', '渠道质量']
    }
    return render(request, 'data-not-accessed.html', context)


@login_required
def activation(request):
    context = {
        'menu': ['activation-menu', '活跃']
    }
    return render(request, 'data-not-accessed.html', context)


@login_required
def retention(request):
    context = {
        'menu': ['retention-menu', '留存']
    }
    return render(request, 'data-not-accessed.html', context)


@login_required
def revenue(request):
    context = {
        'menu': ['revenue-menu', '收入']
    }
    return render(request, 'data-not-accessed.html', context)


@login_required
def initiative_refer(request):
    context = {
        'menu': ['refer-menu', '自传播'],
        'menu2': ['initiative-refer', '主动传播'],
    }
    return render(request, 'data-not-accessed.html', context)


@login_required
def passive_refer(request):
    context = {
        'menu': ['refer-menu', '自传播'],
        'menu2': ['passive-refer', '被动传播'],
    }
    return render(request, 'data-not-accessed.html', context)