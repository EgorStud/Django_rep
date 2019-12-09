# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Album(models.Model):
    a_id = models.IntegerField(db_column='A_ID', primary_key=True)  # Field name made lowercase.
    z = models.ForeignKey('Zapisi', models.DO_NOTHING, db_column='Z_ID', blank=True, null=True)  # Field name made lowercase.
    album_name = models.CharField(db_column='Album_name', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'album'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Manager(models.Model):
    m_id = models.IntegerField(db_column='M_ID', primary_key=True)  # Field name made lowercase.
    fisrt_name = models.CharField(db_column='Fisrt_name', max_length=15)  # Field name made lowercase.
    sec_name = models.CharField(db_column='Sec_name', max_length=15)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=15, blank=True, null=True)  # Field name made lowercase.
    birth = models.DateField(db_column='Birth')  # Field name made lowercase.
    date_start_work = models.DateField(db_column='Date_start_work')  # Field name made lowercase.
    stag = models.IntegerField(db_column='Stag')  # Field name made lowercase.

    def __str__(self):
        return self.fisrt_name

    class Meta:
        managed = False
        db_table = 'manager'


class Singer(models.Model):
    s_id = models.IntegerField(db_column='S_ID', primary_key=True)  # Field name made lowercase.
    m = models.ForeignKey(Manager, models.DO_NOTHING, db_column='M_ID', blank=True, null=True)  # Field name made lowercase.
    name_kollect = models.CharField(db_column='Name_kollect', max_length=40)  # Field name made lowercase.
    date_start = models.DateField(db_column='Date_start')  # Field name made lowercase.
    date_start_label = models.DateField(db_column='Date_start_label')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'singer'


class SingerZap(models.Model):
    s_z_id = models.IntegerField(db_column='S_Z_ID', primary_key=True)  # Field name made lowercase.
    z = models.ForeignKey('Zapisi', models.DO_NOTHING, db_column='Z_ID', blank=True, null=True)  # Field name made lowercase.
    s = models.ForeignKey(Singer, models.DO_NOTHING, db_column='S_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'singer_zap'


class Zapisi(models.Model):
    z_id = models.IntegerField(db_column='Z_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    date_vip = models.DateField(db_column='Date_vip')  # Field name made lowercase.
    format = models.CharField(db_column='Format', max_length=10)  # Field name made lowercase.
    kol_sail = models.IntegerField(db_column='Kol_sail')  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'zapisi'
