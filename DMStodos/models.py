from django.db import models
from datetime import date


class Todo(models.Model):
    title = models.CharField(
        verbose_name="Título", max_length=120, null=False, blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de Entrega", null=False, blank=False)
    finished_at = models.DateField(null=True, blank=True)
    description = models.TextField(verbose_name="Descrição")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["deadline"]

    def mark_as_finished(self):
        if not self.completed:
            self.finished_at = date.today()
            self.save()
