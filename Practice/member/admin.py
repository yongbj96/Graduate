from django.contrib import admin

from .models import BoardMember

# 관리자 페이지에 보이게 하기
class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'create_at', 'update_at')

# 관리자 페이지에 등록
admin.site.register(BoardMember, BoardMemberAdmin)