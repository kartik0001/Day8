# Q4.

class MovieDetails:

	def __init__(self,movie,artist,year,rating):
		self.movie=movie
		self.artist=artist
		self.year=year
		self.rating=rating
	def display(self):
		print("Movie Name:", self.movie)
		print("Artist Name:", self.artist)
		print("Year of Release:", self.year)
		print("Ratings:", self.rating)
	def addDeatils(self,producer):
		self.producer=producer
		print("Producer:", self.producer)
md=MovieDetails('3 Idiots','Aamir Khan',2009,8.4)
md.display()
md.addDeatils('RajKumar Hirani')

'''
OUTPUT:
Movie Name: 3 Idiots
Artist Name: Aamir Khan
Year of Release: 2009
Ratings: 8.4
Producer: RajKumar Hirani

'''