from django.contrib import admin
from catalog.models import Category, Subcategory, Product, Brand, Slider, Image, Product_Image



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_category','description_category','banner_category','sort_order_category','status_category',
        'slug_category','created_at_category','updated_at_category',)
    #list_filter = ('owner','active')
    # list_search = ('name',)


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name_subcategory','category_subcategory','icon_subcategory','sort_order_subcategory','status_subcategory','slug_subcategory',
        'created_at_subcategory','updated_at_subcategory',)
    # list_filter = ('owner','active')
    # list_search = ('name',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name_brand','banner_brand','created_at_brand','updated_at_brand',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_product','brand_product','extract_product','description_product',
        'slug_product','sku_product','price_product','rating_product','subcategory_product','status_product',
        'created_at_product','updated_at_product',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name_image', 'sort_order_image','image_image','created_at_image','updated_at_image',)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product_pi','image_pi','created_at_pi','updated_at_pi',)

class SliderAdmin(admin.ModelAdmin):
    list_display = ('title_slider','image_slider','description_slider','sort_order_slider','status_slider','created_at_slider','updated_at_slider',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Product_Image, ProductImageAdmin)
admin.site.register(Slider, SliderAdmin)


