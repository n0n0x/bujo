from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    event_text = models.CharField(max_length=100)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.event_text


class Appointment(models.Model):
    appointment_text = models.CharField(max_length=100)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.appointment_text


class Task(models.Model):
    task_text = models.CharField(max_length=100)
    date_scheduled = models.DateField()
    date_completed = models.DateField()
    completed = models.BooleanField()

    def __str__(self):
        return self.task_text


class Deadline(models.Model):
    deadline_text = models.CharField(max_length=100)
    date_scheduled = models.DateTimeField()

    def __str__(self):
        return self.deadline_text


class Expense(models.Model):
    ARS = 'ARS'
    BRL = 'BRL'
    USD = 'USD'
    UYU = 'UYU'
    CURRENCY = (
        (ARS, 'Argentina Peso'),
        (BRL, 'Brazil Real'),
        (USD, 'United States Dollar'),
        (UYU, 'Uruguay Peso')
    )
    expense_text = models.CharField(max_length=255)
    date_scheduled = models.DateField()
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY, default=ARS)

    def __str__(self):
        return self.expense_text


class Note(models.Model):
    note_text = models.CharField(max_length=500)
    date_scheduled = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.note_text
