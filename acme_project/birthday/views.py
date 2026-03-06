from django.shortcuts import render
# Импортируем форму
from .forms import BirthdayForm
# Импортируем функцию подсчёта дней
from .utils import calculate_birthday_countdown


def birthday(request):

    # Создаём форму
    # если есть GET параметры → форма получит данные
    # если нет → получит None
    form = BirthdayForm(request.GET or None)

    # Переменная для результата
    birthday_countdown = None

    # Проверяем валидность формы
    if form.is_valid():

        # Берём дату из очищенных данных формы
        birthday = form.cleaned_data['birthday']

        # Вызываем функцию из utils.py
        birthday_countdown = calculate_birthday_countdown(birthday)

    # Создаём словарь контекста
    context = {
        'form': form,
        'birthday_countdown': birthday_countdown
    }

    # Рендерим страницу
    return render(request, 'birthday/birthday.html', context)