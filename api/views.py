from restaurants.models import Restaurant
from rest_framework.permissions import (AllowAny, IsAuthenticated, IsAdminUser,)
from .permissions import IsStaffOrOwner
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from .serializers import (
    RestaurantListSerializer,
    RestaurantDetailSerializer,
    RestaurantCreateUpdateSerializer,
)

class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    permission_classes = [AllowAny,]


class RestaurantDetailView(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer
    permission_classes = [AllowAny,]
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'


class RestaurantCreateView(CreateAPIView):
    serializer_class = RestaurantCreateUpdateSerializer
    permission_classes = [IsAuthenticated,]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RestaurantUpdateView(RetrieveUpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsStaffOrOwner]
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'


class RestaurantDeleteView(DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'