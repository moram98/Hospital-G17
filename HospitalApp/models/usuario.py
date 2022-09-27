from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password



class Usuario(AbstractBaseUser,PermissionsMixin):
            username=models.CharField('Username',primary_key=True, max_length=15, unique=True)
            password=models.CharField('Password', max_length=256)
            perfil=models.CharField('Perfil', max_length=30)
            nombre=models.CharField('Nombre', max_length=35)
            apellido=models.CharField('Apellido', max_length=35)
            telefono=models.CharField('Telefono', max_length=35)
            genero=models.CharField('Genero', max_length=35)

           

