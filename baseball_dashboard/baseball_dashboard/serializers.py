from rest_framework import serializers
from .models import Batting

class BattingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batting
        fields = ["playerid", "yearid", "teamid", "g", "ab", "r", "h", "number_2b", "number_3b", "hr", "rbi", "sb", "cs", "bb", "so", "ibb", "hbp", "sh", "sf", "gidp"]