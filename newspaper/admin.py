from django.contrib import admin
from newspaper.models import Post,Tag,Category,Advertisement,OurTeam,Contact,ContactInformation,Comment,Newsletter
from django_summernote.admin import SummernoteModelAdmin

# admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Advertisement)
admin.site.register(OurTeam)
admin.site.register(Contact)
admin.site.register(ContactInformation)
admin.site.register(Comment)
admin.site.register(Newsletter)




class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)