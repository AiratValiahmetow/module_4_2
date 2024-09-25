def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


inner_function()  #  (ошибка)
# Вызов функции inner_function() вне функции test_function приводит к появлению ошибики -
# NameError: name 'inner_function' is not defined
# вследствие различия пространства имён.

test_function()  # (работает)







