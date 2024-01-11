import csv
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import RoomsCategory, Room, RoomTableInline


class RoomTableInlineAdmin(admin.TabularInline):
    model = RoomTableInline
    
    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="rooms.csv"'

        writer = csv.writer(response)
        writer.writerow(['Name', 'Category', 'User'])

        for room in queryset:
            writer.writerow([smart_str(room.name), smart_str(room.category), smart_str(room.user)])

        return response

    export_to_csv.short_description = "Export selected rooms to CSV"


@admin.register(RoomsCategory)
class RoomsCategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'name', 'slug')
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug')


@admin.register(Room)
class RoomAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'name')
    search_fields = ['name']
    inlines = [RoomTableInlineAdmin]
    fields = ('name',)

    actions = ['export_rooms_to_csv']

    def export_rooms_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="rooms.csv"'

        writer = csv.writer(response)
        writer.writerow(['Xona', 'Inventar'])

        for room in queryset:
            for room_table_inline in room.roomtableinline_set.all():
                writer.writerow([
                    smart_str(room_table_inline.category),
                    smart_str(room_table_inline.products)
                ])

        return response

    export_rooms_to_csv.short_description = "Export selected rooms to CSV"




