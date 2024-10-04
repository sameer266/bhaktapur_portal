from django.contrib import admin

# Register your models here.


from ward.models import Ward
from .models import Content,Category
from user.models import MyUser

# Register your models here.
@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display=('name','category','title','body','image','slug','date_created')

    
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
class UserAdmin(admin.ModelAdmin):
    list_display=('username','email','role','ward','is_staff','is_active')
    
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Role and Ward', {'fields': ('role', 'ward')}),  # Custom fields
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # This controls the fields displayed when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'ward', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    