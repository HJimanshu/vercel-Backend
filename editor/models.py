from django.db import models

class CodeExecution(models.Model):
    code = models.TextField()
    input_data = models.TextField(blank=True, null=True)
    output_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Execution {self.id} - Created at {self.created_at}"