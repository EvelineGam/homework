def test_function():
    def inner_function():
        print('I am in function "test function" visual scope')
    inner_function()


inner_function() # выдаст ошибку, так как функция inner_function не существует вне функции test_function
