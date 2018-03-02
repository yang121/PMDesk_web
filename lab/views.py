from django.shortcuts import render

def market_competitor(request):
    context = {
        'menu': ['market-menu', '市场研究'],
        'menu2': ['market-competitor', '竞品分析'],
    }
    return render(request, 'data-not-accessed.html', context)


def market_ranking(request):
    context = {
        'menu': ['market-menu', '市场研究'],
        'menu2': ['market-ranking', '排行榜'],
    }
    return render(request, 'data-not-accessed.html', context)


def user_portrait(request):
    context = {
        'menu': ['user-menu', '用户研究'],
        'menu2': ['user-portrait', '用户画像'],
    }
    return render(request, 'data-not-accessed.html', context)


def user_behavior(request):
    context = {
        'menu': ['user-menu', '用户研究'],
        'menu2': ['user-behavior', '行为分析'],
    }
    return render(request, 'data-not-accessed.html', context)


def user_group(request):
    context = {
        'menu': ['user-menu', '用户研究'],
        'menu2': ['user-group', '用户分群'],
    }
    return render(request, 'data-not-accessed.html', context)


def event_performance(request):
    context = {
        'menu': ['event-menu', '事件分析'],
        'menu2': ['event-performance', '数据表现'],
    }
    return render(request, 'data-not-accessed.html', context)


def event_behavior_path(request):
    context = {
        'menu': ['event-menu', '事件分析'],
        'menu2': ['event-behavior-path', '行为路径'],
    }
    return render(request, 'data-not-accessed.html', context)


def event_relation(request):
    context = {
        'menu': ['event-menu', '事件分析'],
        'menu2': ['event-relation', '关联分析'],
    }
    return render(request, 'data-not-accessed.html', context)


def version_info(request):
    context = {
        'menu': ['version-menu', '事件分析'],
        'menu2': ['version-info', '版本信息'],
    }
    return render(request, 'data-not-accessed.html', context)


def version_effect(request):
    context = {
        'menu': ['version-menu', '事件分析'],
        'menu2': ['version-effect', '成效分析'],
    }
    return render(request, 'data-not-accessed.html', context)