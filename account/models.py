from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(verbose_name='用户', to=User, to_field='id', on_delete=False)
    avatar = models.ImageField(
        verbose_name='头像',
        upload_to='static/avatar/',
        default='static/avatar/avatar_default.jpeg',
        null=True,
        blank=True
    )
    nickname = models.CharField(verbose_name='昵称', max_length=64, unique=True, null=True, blank=True)
    telephone = models.CharField(verbose_name='手机号码', max_length=32, unique=True)

    def __str__(self):
        return '%s-%s-%s-%s' % (self.user_id, self.user.username, self.nickname, self.telephone)


class App(models.Model):
    apkname = models.CharField(verbose_name='包名', max_length=64, unique=True)
    title = models.CharField(verbose_name='应用名', max_length=64, unique=True)
    publisher = models.CharField(verbose_name='发行商', max_length=64, unique=True, null=True, blank=True)
    icon = models.ImageField(
        verbose_name='图标',
        upload_to='static/app/icon/',
        default='static/app/icon/icon_default.jpeg',
        null=True,
        blank=True
    )

    def __str__(self):
        return '%s-%s-%s-%s' % (self.id, self.title, self.apkname, self.publisher)


class Market(models.Model):
    title = models.CharField(verbose_name='应用市场名', max_length=64, unique=True)
    href = models.URLField(verbose_name='官网链接')

    def __str__(self):
        return '%s-%s-%s' % (self.id, self.title, self.href)


class AppVersion(models.Model):
    app = models.ForeignKey(verbose_name='所属应用',to='App', to_field='id', on_delete=False)
    title = models.CharField(verbose_name='版本名', max_length=32)

    # YYYY-MM-DD
    date = models.DateField(verbose_name='发布日期')
    market = models.ForeignKey(verbose_name='所属市场', to='Market', on_delete=False, to_field='id')

    def __str__(self):
        return '%s-%s-%s-%s' % (self.date, self.title, self.app.title, self.market.title)


class Downloads(models.Model):
    market = models.ForeignKey(verbose_name='所属市场', to='Market', on_delete=False, to_field='id')
    app = models.ForeignKey(verbose_name='所属应用', to='App', to_field='id', on_delete=False)
    daily = models.IntegerField(verbose_name='日下载量', null=True, blank=True)
    subtotal = models.IntegerField(verbose_name='日累计总量', null=True, blank=True)
    date = models.DateField(verbose_name='日期')

    def __str__(self):
        return '%s-%s-%s-%s-%s' % (self.date, self.app.title, self.market.title, self.daily, self.subtotal)


class AppDownloadLink(models.Model):
    market = models.ForeignKey(verbose_name='所属市场', to='Market', on_delete=False, to_field='id')
    app = models.ForeignKey(verbose_name='所属应用', to='App', to_field='id', on_delete=False)
    href = models.URLField(verbose_name='下载链接')

    def __str__(self):
        return '%s-%s-%s' % (self.app.title, self.market.title, self.href)


class AppRank(models.Model):
    market = models.ForeignKey(verbose_name='所属市场', to='Market', on_delete=False, to_field='id')
    app = models.ForeignKey(verbose_name='所属应用', to='App', to_field='id', on_delete=False)
    rank = models.IntegerField(verbose_name='排名', null=True, blank=True)
    date = models.DateField(verbose_name='日期')

    span_choice = [
        (1, '天'),
        (7, '周'),
        (30, '月'),
        (90, '季度'),
        (180, '半年'),
        (365, '年度'),
    ]
    span = models.IntegerField(verbose_name='排名', null=True, blank=True, choices=span_choice)

    def __str__(self):
        span = '无排名'
        for i in self.span_choice:
            if self.span == i[0]:
                span = i[1]
                break
        return '%s-%s-%s-%s-%s' % (self.rank, self.app.title, self.market.title, self.date, span)


class AppCategory(models.Model):
    app = models.ForeignKey(verbose_name='所属应用', to='App', to_field='id', on_delete=False)
    title = models.CharField(verbose_name='分类名', max_length=32)
    market = models.ForeignKey(verbose_name='所属市场', to='Market', on_delete=False, to_field='id')

    def __str__(self):
        return '%s-%s-%s' % (self.title, self.app.title, self.market.title)


class AppID(models.Model):
    market = models.ForeignKey(verbose_name='所属市场', to='Market', on_delete=False, to_field='id')
    app = models.ForeignKey(verbose_name='所属应用', to='App', to_field='id', on_delete=False)
    market_identify = models.CharField(verbose_name='应用ID', max_length=64)

    def __str__(self):
        return '%s-%s-%s' % (self.market_identify, self.app.title, self.market.title)