from django.test import TestCase
from registration.users import UserModel


class TestLoginRememberMeFunctionality(TestCase):
    """Tests for authentication related views."""

    def setUp(self):
        self.user = UserModel()(username='test', email='test@email.com')


    def test_login_remember(self):

        # Log a user in with the remember-me checkbox checked.
        form = self.app.get(reverse('login')).form
        form['username'] = self.user.username
        form['password'] = TEST_PASSWORD
        form['remember'] = 'checked'
        response_main_page = form.submit().follow()

        # This takes you to the main page.
        self.assertEqual(response_main_page.context['user'].username,
                         self.user.username)

        # Because they're logged in, the main page contains a link to their
        # profile page.
        user_prfl_url = reverse('user_profile')
        self.assertIn(user_prfl_url, str(response_main_page.content))

        # Restart the browser,
        http.StopableWSGIServer.shutdown()
        time.sleep(2)  # Two seconds
        http.StopableWSGIServer.run()

        # and the session should still be active.
        self.assertFalse(
            response_login_page.context['user'].is_authenticated())

        # Therefore, the link to their profile should still be there.
        response_main_page = self.app.get(reverse('main_page'))
        assert user_prfl_url in response_main_page


