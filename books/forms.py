from django import forms
from .models import Book


class AddBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == "book_image":
                self.fields[field].widget.attrs.update(
                    {
                        "class": "file-input file-input-bordered file-input-primary w-full max-w-xs",
                        "type": "file",
                    }
                )
            if field == "is_available":
                self.fields[field].widget.attrs.update(
                    {
                        "class": "toggle toggle-primary",
                        "type": "checkbox",
                    }
                )
            if field == "categories":
                self.fields[field].widget.attrs.update(
                    {
                        "class": "select w-full max-w-xs",
                    }
                )
            if field == "author":
                self.fields[field].widget.attrs.update(
                    {
                        "class": "select select-bordered w-full max-w-xs",
                    }
                )
            else:
                self.fields[field].widget.attrs.update(
                    {
                        "class": ("input input-bordered w-full max-w-xs"),
                        "placeholder": ("Type here"),
                    }
                )

    class Meta:
        model = Book
        fields = [
            "book_image",
            "title",
            "author",
            "categories",
            "book_content",
            "description",
            "isbn_number",
            "borrow_price",
            "stk_quantity",
            "is_available",
            "discount_price",
        ]
