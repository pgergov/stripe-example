from django.contrib.auth.base_user import BaseUserManager


class BaseUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Email field is required.')

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.is_staff = kwargs.get('is_superuser', False)

        if password is None or password.strip() == '':
            user.set_unusable_password()
        else:
            user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **kwargs):
        kwargs.setdefault('is_superuser', False)

        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **kwargs)
