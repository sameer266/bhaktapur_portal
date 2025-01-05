from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from user.models import MyUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.urls import path



# Register your models here.


from ward.models import Ward
from .models import Content,Category
from mail import views



@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ('get_user_ward', 'category', 'title', 'body', 'image', 'slug', 'date_created')

    def get_user_ward(self, obj):
        # Access the 'ward' field of the related MyUser model
        return obj.name.ward  # 'user' is the ForeignKey field in the Ward model

    # Customize the column name in the admin panel
    get_user_ward.short_description = 'User Ward'

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display=('title','truncated_body','category','date_created')
    
    def truncated_body(self, obj):
        # Limit the body text to a certain number of characters
        return obj.body[:50] + '...' if len(obj.body) > 50 else obj.body
    truncated_body.short_description = 'Body'  # This sets the column header in the admin
    
    
class ContentInline(admin.TabularInline):
    model = Content
    extra = 1  # Number of empty forms to display (optional)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)
    inlines = [ContentInline]
    


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'ward', 'is_staff', 'is_active', 'send_email_link')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Role and Ward', {'fields': ('role', 'ward')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'ward', 'is_staff', 'is_active')},
        ),
    )

    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

    def send_email_link(self, obj):
        # Link to the custom email sending page
        if obj.role=="ward_officer":
            url = reverse('admin:send_email_view')
            return format_html('<a href="{}">Send Email</a>', url)

    send_email_link.short_description = 'Send Email'

    # Add custom URL for the email sending view
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('send-email/', self.admin_site.admin_view(views.send_email_view), name='send_email_view'),
        ]
        return custom_urls + urls
    
#-------------------
#----When the MyUserCreationForm is used to create a new user, Django will automatically call the set_password method to hash the password before saving it to the database.
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'role', 'ward', 'is_staff', 'is_active')
        


