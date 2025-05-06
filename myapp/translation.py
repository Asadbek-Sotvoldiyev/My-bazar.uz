from modeltranslation.translator import register, TranslationOptions
from .models import Season, Collection, Category, Product, OrderItem


@register(Collection)
class CollectionTranslationOption(TranslationOptions):
    fields = ('name',)


@register(Season)
class SeasonTranslationOption(TranslationOptions):
    fields = ('name',)

@register(Category)
class CategoryTranslationOption(TranslationOptions):
    fields = ('name',)


@register(Product)
class ProductTranslationOption(TranslationOptions):
    fields = ('name', 'content')


@register(OrderItem)
class OrderTranslationOption(TranslationOptions):
    fields = ('name',)
