from behave import given, when, then


@given("user is not logged in")
def verify_user_not_logged_in(context):
    pass


@when('When user click "My Account" and "Login" on upper panel')
def user_use_upper_panel(context):
    pass


@when('user enters email and password')
def user_enters_email_and_password(context):
    pass


@when('user clicks Login button')
def user_clicks_login_btn(context):
    pass


@then("user's profile page is launched")
def login_verifying(context):
    pass


@given('user is logged in')
def verify_user_is_logged_in(context):
    pass


@when('user click "My Account" and "Logout" on upper panel')
def user_logouts(context):
    pass


@then('"Account logout" info pops up')
def logout_verifying(context):
    pass


@when('user logins and then logouts')
def login_logout_verifying(context):
    context.execute_steps(
        """
    Given user is not logged in
    When user click "My Account" and "Login" on upper panel
    When user enters email and password
    And user clicks Login button
    Then user's profile page is launched
    Given user is logged in
    When user click "My Account" and "Logout" on upper panel
    Then "Account logout" info pops up
        """
    )
