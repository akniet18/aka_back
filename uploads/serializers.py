from rest_framework import serializers
from .models import *
from users.serializers import *


class UploadSer(serializers.ModelSerializer):
	file = serializers.FileField(use_url=True)
	class Meta:
		model = Uploads
		fields = "__all__"