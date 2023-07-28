from django.contrib import admin
from .models import User, UserManager, Test, TesterResult, TestRequirements, Result

# Register your models here.
admin.site.register(User)
admin.site.register(Test)
admin.site.register(TesterResult)
admin.site.register(TestRequirements)
admin.site.register(Result)
