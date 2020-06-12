from django.contrib import admin
from groups.models import Group,GroupMember
# Register your models here.
admin.site.register(Group)

class GroupMemberInLine(admin.TabularInline):
    model=models.GroupMember
