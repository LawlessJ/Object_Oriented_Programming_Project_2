class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  def __repr__(self):
    return "{name}. \"{title}\". {year}, {medium}. {ownername}, {ownerlocation}.".format(name = self.artist, title= self.title, year = self.year, medium = self.medium, ownername= self.owner.name, ownerlocation = self.owner.location)
  
class Marketplace:
  def __init__(self):
    self.listings = []
  
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  def remove_listing(self,expired_listing):
    self.listings.remove(expired_listing)
  def take_listing(self, taken_listing):
    self.listing.pop(taken_listing)
  def show_listings(self):
    for listing in self.listings:
      print(listing)
 
veneer = Marketplace()

class Client:
  def __init__(self, name, location, is_museum = False): #is_museum =True means museum, False = collector
  # location = museum name if museum or "Private Collector" if collector
    self.name = name
    self.location = location
    self.is_museum = is_museum
    
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      newlist = Listing(artwork,price, self)
      veneer.add_listing(newlist)
      
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          break
      if art_listing != None:
        art_listing.art.owner = self
        veneer.remove_listing(art_listing)
         
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  def __repr__(self):
    return "{artist}'s \"{title}\":listed at the price {price}.".format(artist = self.art.artist, title= self.art.title, price = self.price)

edytta = Client("Edytta Halpirt","Private Collector")

moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)
#print(girl_with_mandolin)

edytta.sell_artwork(girl_with_mandolin, "6M (USD)")
#veneer.show_listings()
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
veneer.show_listings()
