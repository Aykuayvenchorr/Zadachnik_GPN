from django.db import models
from django.db.models import CASCADE, SET_NULL
from month.models import MonthField
from phonenumber_field.modelfields import PhoneNumberField


class Company(models.Model):
    parent = models.ForeignKey('Company', on_delete=CASCADE)
    name = models.CharField(max_length=77, verbose_name='Наименование компании')
    name_full = models.CharField(max_length=255, verbose_name='Полное наименование')
    contact = models.TextField(verbose_name='Контакты')
    phone = PhoneNumberField(verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='E-mail')
    note = models.TextField(verbose_name='Примечания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Subdivision(models.Model):
    parent = models.ForeignKey('Subdivision', on_delete=CASCADE)
    company = models.ForeignKey('Company', on_delete=CASCADE, verbose_name='Компания')
    name = models.CharField(max_length=77, verbose_name='Наименование подразделения')
    name_full = models.CharField(max_length=255, verbose_name='Полное наименование')
    contact = models.TextField(verbose_name='Контакты')
    phone = PhoneNumberField(verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='E-mail')
    note = models.TextField(verbose_name='Примечания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Project(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class LicArea(models.Model):
    title = models.CharField(max_length=50)
    project = models.ManyToManyField(Project)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Лицензионный участок'
        verbose_name_plural = 'Лицензионные участки'


class Deposit(models.Model):
    title = models.CharField(max_length=50)
    lic_area = models.ManyToManyField(LicArea)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Месторождение'
        verbose_name_plural = 'Месторождения'


class Object(models.Model):
    title = models.CharField(max_length=50)
    parent = models.ForeignKey('Object', on_delete=CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class NDFL(models.Model):
    rate = models.FloatField()

    class Meta:
        verbose_name = 'НДФЛ'
        verbose_name_plural = 'НДФЛ'


class NDS(models.Model):
    rate = models.FloatField()

    class Meta:
        verbose_name = 'НДС'
        verbose_name_plural = 'НДС'


class PayTerm(models.Model):
    condition = models.TextField()

    class Meta:
        verbose_name = 'Условие платежа'
        verbose_name_plural = 'Условия платежа'


class ContractLease(models.Model):
    number = models.CharField(max_length=70, verbose_name='Номер договора')
    counter_party = models.ForeignKey('CounterParty', blank=True, null=True, on_delete=SET_NULL, verbose_name='Контрагент')
    date_begin = models.DateField(verbose_name='Дата начала договора')
    date_end = models.DateField(verbose_name='Дата окончания договора')
    term = models.CharField(max_length=30, verbose_name='Срок действия договора')
    total_sum = models.FloatField(verbose_name='Общая сумма договора')
    ndfl = models.ForeignKey(NDFL, blank=True, null=True, on_delete=SET_NULL, verbose_name='НДФЛ')
    nds = models.ForeignKey(NDS, blank=True, null=True, on_delete=SET_NULL, verbose_name='НДС')
    pay_f_month = models.FloatField(verbose_name='Платеж в месяц')
    pay_f_day = models.FloatField(verbose_name='Платеж в день')
    relevant = models.BooleanField(verbose_name='Актуальность')
    payment_terms = models.ForeignKey(PayTerm, blank=True, null=True, on_delete=SET_NULL, verbose_name='Условие платежа')  # Пока так, мб надо исправить

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Договор аренды/субаренды'
        verbose_name_plural = 'Договоры аренды/субаренды'


class CounterParty(models.Model):
    name = models.CharField(max_length=70)
    esk = models.CharField(max_length=10)
    inn = models.CharField(max_length=20)
    kpp = models.CharField(max_length=20)
    kd = models.CharField(max_length=100)
    mm_contract = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'


class EBK(models.Model):
    number = models.CharField(max_length=20)
    article = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'ЕБК'
        verbose_name_plural = 'ЕБК'


class RentPayment(models.Model):
    """Платеж по аренде (Задание на платеж - ZADANL_V3)"""

    contract = models.ForeignKey(ContractLease, blank=True, null=True, on_delete=SET_NULL)  # Скорее всего on_delete нужно будет изменить
    ebk = models.ForeignKey(EBK, blank=True, null=True, on_delete=SET_NULL)
    counter_party = models.ForeignKey(CounterParty, blank=True, null=True, on_delete=SET_NULL)
    note = models.TextField()
    period = MonthField("Month Value", help_text="Выберите месяц")
    # pay_date = вытаскивать из договора
    # pay_sum = тоже из договора
    pay_day = models.DateField()  # Надо проверять, чтобы дата платежа была не позднее чем в договоре
    pfm = models.CharField(max_length=30, default='Главный маркшейдер')

    class Meta:
        verbose_name = 'Платеж по аренде'
        verbose_name_plural = 'Платежи по аренде'





    



