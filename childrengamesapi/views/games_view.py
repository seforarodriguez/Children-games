"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from childrengamesapi.models import Game, Adult


class GameView(ViewSet):
    """Level up game view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game
         """
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all 

        Returns:a
            Response -- JSON serialized list of games
        """
       

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """

        message = ""

        asked_age = request.data["kids_age"]

        message_list = [
            {"role": "assistant","content": "You are a helpful early childhood educator"},
            {"role": "user", "content": f"I want 5 educational games for {asked_age} year olds"}
        ]


        adult = Adult.objects.get(user=request.auth.user)

        game = Game.objects.create(
            name=request.data["game_name"],
            description=request.data["game_description"],
            requested_by=adult
        )
        serializer = GameSerializer(game)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        return Response(None, status=status.HTTP_204_NO_CONTENT)

      
class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Game
        fields = ('id', "name", "description")