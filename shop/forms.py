from django import forms

from shop.models import Product, Comment, Order


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ['name', 'description', 'price', 'rating', 'discount', 'quantity']
        exclude = ()


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    search = forms.CharField(label='Search',max_length=100)


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email']
