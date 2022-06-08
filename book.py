class book:
    def __init__(self,authorlast,authorfirst,title,place,publisher,year):
        self.authorlast=authorlast
        self.authorfirst=authorfirst
        self.tit=title
        self.year=year
        self.place=place
        self.publisher=publisher
    def write_bib_entry(self):
        return (self.authorlast +" ,"+self.authorfirst+", "+self.tit,self.year+ " ,"+self.place+", "+self.publisher)
beauty=book("Dubay", "Thomas", "The Evidential Power of Beauty", "San Francisco", "Ignatius Press", "1999", )
pynut = book( "Martelli", "Alex", "Python in a Nutshell", "Sebastopol, CA", "O'Reilly Media, Inc.", "2003" )

print(pynut.write_bib_entry())
print(beauty.write_bib_entry())
beauty.year='2021'
print(beauty.write_bib_entry())

