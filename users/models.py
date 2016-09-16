from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models




class Person(AbstractUser):
    card_id = models.IntegerField(primary_key=True)
    middle_names = models.CharField(max_length=30)
    date_joined = models.DateField(auto_now=True)
    
    
    def save(self, *args, **kwargs):
        
        if not self.username:
            initials = '%s'%(self.first_name[0].lower())
            mn = self.middle_names.split(' ') if self.middle_names else []
            for c in mn: 
                initials += c[0].lower()
            initials += self.last_name[0].lower()
            initials += '_'
            rs = Person.objects.filter(
                username__startswith=initials).order_by('-username')
            if len(rs) != 0:
                num = int(rs[0].username.split('_')[1]) + 1
            else:
                num = 0
                
            self.username = "%s%03d"%(initials, num)
            
        super(Person,self).save(*args, **kwargs)

    

    