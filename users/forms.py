from django import forms
from users.models import User

letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'"

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol'}))


class RegisterForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol'}))
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parolni tasdiqlang'}))
    first_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'}))
    last_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiyangiz'}))
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Emailingiz'}))

    def clean(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        email = self.cleaned_data['email']
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if password:
            if password != password2:
                raise forms.ValidationError("Parol bir xil bo'lishi kerak!")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bunday email bazada mavjud!")

        for i in first_name:
            if i not in letters:
                raise forms.ValidationError("Ism faqat harflardan iborat bo'lishi kerak!")
        if len(first_name)>20:
            raise forms.ValidationError("Ism noto'g'ri kiritildi. Juda uzun! ")

        for i in last_name:
            if i not in letters:
                raise forms.ValidationError("Familiya faqat harflardan iborat bo'lishi kerak!")
        if len(last_name)>30:
            raise forms.ValidationError("Familiya noto'g'ri kiritildi. Juda uzun! ")



        return self.cleaned_data

class ProfileForm(forms.ModelForm):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'}))
    last_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiyangiz'}))
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Emailingiz'}))
    phone_number = forms.CharField(required=False,label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqamingiz'}))
    bio = forms.CharField(required=False,label='',widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Bio'}))
    image = forms.ImageField(required=False,label='',widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'phone_number', 'bio', 'image']


    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        phone_number = self.cleaned_data.get('phone_number')

        for i in first_name:
            if i not in letters:
                raise forms.ValidationError("Ism faqat harflardan iborat bo'lishi kerak!")
        if len(first_name)>20:
            raise forms.ValidationError("Ism noto'g'ri kiritildi. Juda uzun! ")

        for i in last_name:
            if i not in letters:
                raise forms.ValidationError("Familiya faqat harflardan iborat bo'lishi kerak!")
        if len(last_name)>30:
            raise forms.ValidationError("Familiya noto'g'ri kiritildi. Juda uzun! ")

        if len(phone_number)!=13:
            raise forms.ValidationError("Telefon raqam xato kiritildi: Na'muna: '+998XXYYYZZAA'")
        if phone_number[:4]!='+998':
            raise forms.ValidationError("Telefon raqam faqat O'zbekistonga tegishli bo'lishi kerak")
        if not phone_number[4:].isdigit():
            raise forms.ValidationError("Telefon raqam kiritishda xatolik!")



        return self.cleaned_data

