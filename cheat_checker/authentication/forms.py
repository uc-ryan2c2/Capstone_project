from django import forms


class createUser(forms.Form):
    username = forms.CharField(
        label='username',
        max_length=30,
        widget=forms.TextInput(attrs={'class': "logininput100"}),
        required=True
    )
    password = forms.CharField(
        label='password',
        max_length=30,
        widget=forms.TextInput(attrs={'class': "logininput100"}),
        required=True
    )
    password2 = forms.CharField(
        label='password2',
        max_length=30,
        widget=forms.TextInput(attrs={'class': "logininput100"}),
        required=True
    )
    email = forms.CharField(
        label='email',
        max_length=50,
        widget=forms.TextInput(attrs={'class': "logininput100"}),
        required=True
    )
    canvas_token = forms.CharField(
        label='canvas_token',
        widget=forms.TextInput(attrs={'class': "logininput100"}),
        required=True
    )

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not any(char.isupper() for char in password):
            raise forms.ValidationError("This password does not contain an uppercase character")

        return password

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        print(password2)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email



    # def account_validation(self):
    #     # fetch the data from the account creation form
    #     super(createUser, self).clean()
    #
    #     # obtain the data from the html
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #     email = self.cleaned_data.get('email')
    #
    #     specialCharacters = ['$', '#', '@', '!', '*']
    #
    #     if len(username) < 5:
    #         self._errors['username'] = self.error_class([
    #             'Minimum 5 characters required.'])
    #     if len(password) < 8:
    #         self._errors['password'] = self.error_class([
    #             'password Should Contain a minimum of 8 characters.'])
    #     # Check if password contains at least one uppercase letter
    #     elif not any(char.isupper() for char in password):
    #         self._errors['password'] = self.error_class([
    #             'Password must contain at least one uppercase letter.'])
    #
    #     # Check if password contains at least one lowercase letter
    #     elif not any(char.islower() for char in password):
    #         self._errors['password'] = self.error_class([
    #             'Password must contain at least one lowercase letter.'])
    #
    #     # Check if password contains at least one digit
    #     elif not any(char.isdigit() for char in password):
    #         self._errors['password'] = self.error_class([
    #             'Password must contain at least one digit.'])
    #
    #     elif not any(c in specialCharacters for c in password):
    #         self._errors['password'] = self.error_class([
    #             'Password must contain at least one special character. The following are the allowed '
    #             'special characters. $, #, @, !, *'])
    #
    #     if '@' not in email and len(email) < 8:
    #         self._errors['email address'] = self.error_class([
    #             'Invalid email address.'])
    #
    #     return self.cleaned_data
