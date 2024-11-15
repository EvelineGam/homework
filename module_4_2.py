def test_function():
    def inner_function():
        print('I am in function "test function" visual scope')
    inner_function()


inner_function()