from django.contrib import admin
from .models import Member, Transaction, Planting, Event, Document, Expense, Sale


# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        'membership_id', 'first_name', 'second_name', 'other_name', 'gender', 'phone',
        'designation','registration_date', 'status'
    ]
    list_filter = [
        'gender', 'registration_date', 'status'
    ]
    search_fields = ['membership_id', 'first_name', 'second_name', 'other_name']
    # raw_id_fields = ['membership_id']
    # date_hierarchy = ['registration_date']
    # ordering = ['subscription_status', 'subscription_date']
    show_facets = admin.ShowFacets.ALWAYS

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['member', 'amount', 'transaction_type', 'description', 'transaction_date']
    list_filter = ['transaction_type', 'transaction_date']
    search_fields = ['memmber', 'transaction_type']
    # date_hierarchy = ['transaction_date']
    show_facets = admin.ShowFacets.ALWAYS

@admin.register(Planting)
class PlantingAdmin(admin.ModelAdmin):
    list_display = ['date', 'seedlings']
    list_filter = ['date']
    search_fields = ['date']
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'start_date', 'end_date', 'location', 'status','created_by', 'date_created']
    list_filter = ['start_date', 'status', 'date_created']
    search_fields = ['title', 'location', 'status', 'created_by']
    show_facets = admin.ShowFacets.ALWAYS

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['description', 'category', 'amount', 'date_incurred', 'incurred_by', 'date_logged']
    list_filter = ['category', 'date_incurred', 'incurred_by']
    search_fields = ['description', 'category', 'incurred_by']
    show_facets = admin.ShowFacets.ALWAYS

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'file_path', 'uploaded_by', 'date_uploaded', 'access_level']
    list_filter = ['date_uploaded', 'access_level']
    search_fields = ['title']
    # list_display_links = ['file_path']
    show_facets = admin.ShowFacets.ALWAYS

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'unit_price', 'buyer', 'sale_date']
    list_filter = ['sale_date']
    search_fields = ['product', 'buyer']
    # list_display_links = ['file_path']
    show_facets = admin.ShowFacets.ALWAYS