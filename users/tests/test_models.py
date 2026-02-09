from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test that a user is created successfully with an email and password."""
        email = "test@example.com"
        password = "patel123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_is_normalized(self):
        """Test that the email domain is normalized to lowercase."""
     
        email = "test@Example.COM"

        user = get_user_model().objects.create_user(
            email=email,
            password="dishank123"
        )

        self.assertEqual(user.email, email.lower())

    def test_user_without_email_fails(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="",
                password="pass"
            )
