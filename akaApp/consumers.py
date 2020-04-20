from channels.db import database_sync_to_async
from channels.consumer import AsyncConsumer
import asyncio
from .models import *
from .serializers import *
import json
from django.contrib.auth import get_user_model

User = get_user_model()