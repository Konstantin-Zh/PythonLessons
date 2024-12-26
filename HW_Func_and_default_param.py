
def is_valid_email(email):
    semail = str(email).lower()
    return semail.count('@') == 1 and (semail.endswith('.com') or semail.endswith('.ru') or semail.endswith('.net'))

def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    srecipient = str(recipient).lower()
    ssender = str(sender).lower()
    if is_valid_email(srecipient) and is_valid_email(ssender):
        if srecipient == ssender:
            return str("Нельзя отправить письмо самому себе!")
        elif ssender == "university.help@gmail.com":
            return str(f'Письмо успешно отправлено с адреса "{str(sender)}" на адрес "{str(recipient)}".')
        else:
            return str(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса "{str(sender)}" на адрес "{str(recipient)}".')
    else:
        return str(f'Невозможно отправить письмо с адреса "{str(sender)}" на адрес "{str(recipient)}".')



print(send_email('Это сообщение для проверки связи', 'Vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))

