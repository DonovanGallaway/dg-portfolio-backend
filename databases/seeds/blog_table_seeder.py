"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog

class BlogTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Blog.create({"title":"Litany Against Fear", "imgurl":"https://ichef.bbci.co.uk/news/976/cpsprodpb/13F00/production/_95146618_bills.jpg","body":"I must not fear. Fear is the mind-killer"})
        Blog.create({"title":"Laughing Man","imgurl":"https://ichef.bbci.co.uk/news/976/cpsprodpb/13F00/production/_95146618_bills.jpg", "body":"What I thought I'd do is I'd pretend I was one of those deaf-mutes"})
        Blog.create({"title":"Firefly","imgurl":"https://ichef.bbci.co.uk/news/976/cpsprodpb/13F00/production/_95146618_bills.jpg", "body":"If this is showing, your seed route was gorram shiny"})