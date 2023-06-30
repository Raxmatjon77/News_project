from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin

class OnlyLoggedSuperUser(LoginRequiredMixin,UserPassesTestMixin):
    def test_func(self):

        return self.request.user.is_superuser
