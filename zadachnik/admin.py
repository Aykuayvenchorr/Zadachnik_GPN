from django.contrib import admin

from zadachnik.models import Company, Subdivision, Object, Deposit, Project, LicArea, NDFL, NDS, PayTerm, ContractLease, \
    CounterParty, EBK, RentPayment

# Register your models here.
admin.site.register(Company)
admin.site.register(Subdivision)
admin.site.register(Project)
admin.site.register(LicArea)
admin.site.register(Deposit)
admin.site.register(Object)
admin.site.register(NDFL)
admin.site.register(NDS)
admin.site.register(PayTerm)
admin.site.register(ContractLease)
admin.site.register(CounterParty)
admin.site.register(EBK)
admin.site.register(RentPayment)


