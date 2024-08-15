from django.shortcuts import render, redirect, get_object_or_404
from books.models import Book
from .models import BorrowBook
from accounts.models import UserAccount
from django.contrib import messages

# Create your views here.
try:

    def borrow_now(request, book_id):
        book = get_object_or_404(Book, id=book_id)
        user_account = getattr(
            request.user, "account", None
        )  # Adjust based on actual relationship

        if user_account is None:
            return redirect("user_login")

        if book.stk_quantity > 0:
            user_balance = user_account.balance
            if user_balance >= book.price:  # Use >= to handle exact matches
                borrow = BorrowBook.objects.create(
                    user=request.user,
                    book=book,
                    quantity=1,
                    total_price=book.price,
                )
                book.stk_quantity -= 1
                user_account.balance -= book.price
                book.save()
                user_account.save(update_fields=["balance"])

                messages.success(
                    request,
                    f'Successfully withdrew {"{:,.2f}".format(float(book.price))}$ from your account',
                )
                return redirect("borrow_conf", order_id=borrow.id)
            else:
                messages.error(
                    request,
                    "Insufficient balance to borrow this book.",
                )
                return redirect("book_detail", book_id=book.id)
        else:
            messages.error(
                request,
                "The book is out of stock.",
            )
            return redirect("book_detail", book_id=book.id)

    def borrow_confirmation(request, order_id):
        borrow = get_object_or_404(BorrowBook, id=order_id, user=request.user)
        return render(request, "borrow_conf.html", {"borrow": borrow})

except Exception as e:
    print(e)
