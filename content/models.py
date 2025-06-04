from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    @property
    def stock(self):
        inbound = self.movements.filter(movement_type=Movement.IN).aggregate(models.Sum('quantity'))['quantity__sum'] or 0
        outbound = self.movements.filter(movement_type=Movement.OUT).aggregate(models.Sum('quantity'))['quantity__sum'] or 0
        return inbound - outbound

class Movement(models.Model):
    IN = 'IN'
    OUT = 'OUT'
    MOVEMENT_TYPES = [
        (IN, 'Inbound'),
        (OUT, 'Outbound'),
    ]

    material = models.ForeignKey(Material, related_name='movements', on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPES)
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.material.name} {self.movement_type} {self.quantity}"
