from django.shortcuts import render, redirect, get_object_or_404
from books.models import Book
from .models import BorrowBook

# Create your views here.
try:

    def borrow_now(request, book_id):
        book = get_object_or_404(Book, id=book_id)
        if book.stk_quantity > 0:
            borrow = BorrowBook.objects.create(
                user=request.user, book=book, quantity=1, total_price=book.borrow_price
            )
            book.stk_quantity -= 1
            book.save()
            return redirect(
                "borrow_conf", order_id=borrow.id
            )  # use correct URL name and parameter
        else:
            return redirect("book_detail", book_id=book.id)

    def borrow_confirmation(request, order_id):
        borrow = get_object_or_404(
            BorrowBook, id=order_id, user=request.user
        )  # use order_id here
        return render(request, "borrow_conf.html", {"borrow": borrow})

except Exception as e:
    print(e)
