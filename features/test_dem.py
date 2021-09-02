
from pytest_bdd import given,when,then,scenario,scenarios

scenarios("../features")

@given('when i open the app')
def step_impl():
    print('when i open the app')


@then('user will start doing something')
def step_impl():
    print('user will start doing something')


@given('open app')
def step_impl():
    print("open app")


@when('user is pointing url abcde')
def step_imp():
    print("user is pointing url abcde")


@then('user opens the app')
def step_impl():
    print('user opens the app')



@given('open app again')
def step_impl():
    print("open app again")


@when('user logs in')
def step_imp():
    print("user logs in")


@then('user is logged in')
def step_impl():
    print('user is logged in')


@given('user do something')
def step_impl():
    print('user do something')


@when('user see something')
def step_impl():
    print('user see something')


@then('user completes this')
def step_impl():
    print('user completes this')


@given('user comes in')
def step_impl():
    print('user comes in')


@when('user sees something')
def step_impl():
    print('user sees something')


@then('user do something')
def step_impl():
    print('user do something')

