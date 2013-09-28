from django.views.generic import DetailView
from songs.models import Song


class SongView(DetailView):
    model = Song

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()

        artist_slug = self.kwargs['artist_slug']
        song_slug = self.kwargs['song_slug']

        return queryset.get(slug=song_slug, artist__slug=artist_slug)
