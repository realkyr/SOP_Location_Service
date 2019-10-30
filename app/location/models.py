from django.db import models

# Create your models here.
class Location(models.Model):
    """
        ข้อมูลของสถานที่ประกอบด้วย ชื่อ คำอธิบาย วันที่สร้าง(อัตโนมัติ) ละติจูด ลองจิจูด
    """
    name = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Contract(models.Model):
    """
        ช่องทางการติดต่อ ผูกกับสถานที่ (location) แบบ One to Many

        type ประเภทของช่องทางการติดต่อ เช่น ['facebook', 'phone']
    """
    detail = models.CharField(max_length=50)
    type = models.CharField(max_length=2)
    location = models.ForeignKey(
        Location,
        null=True,
        on_delete=models.CASCADE,
        related_name="contracts"
    )