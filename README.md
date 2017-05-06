## Integrating Stripe Payment with Django

Educational django project with Stripe integration
---

### Initial setup
* Create repo
* Add db, Python & Emacs files

### Create users
* Setup `BaseUser` with email & password
* You'll need a manager
* Change `AUTH_USER_MODEL`
* Create your users
* Register everything in Django Admin

### Create magazine
* Create `Magazine` & `Article` models. Register in admin
* Create magazine & article list views
* Create urls. Register them
* Create templates outside apps. Add settings

### Add LoginRequiredMixin
* Add `/login` url. Add template
* Add `/logout` url
* Add `LoginRequiredMixin`

### Setup Celery
* Create `celery.py`
* Import app in `__init__.py`
* Create dummy task
* Run celery in separate terminal
* Create `BuyArticleView`
