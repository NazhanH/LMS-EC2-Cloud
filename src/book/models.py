from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication = models.CharField(max_length=100)
    year = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return (str(self.id) + self.title)
    
class BorrowList(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    expected_return_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    fine = models.FloatField(default=0)

    def __str__(self):
        return (self.borrower.username + self.book.title + self.borrow_date.strftime('%Y%m%d'))