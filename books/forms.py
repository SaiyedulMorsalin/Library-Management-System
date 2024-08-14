from django import forms
from .models import Book


class AddBookForm(forms.ModelForm):

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

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["book_image"].widget.attrs.update(
    #         {
    #             "class": "file-input file-input-bordered file-input-primary w-full max-w-xs",
    #             "type": "file",
    #         }
    #     )
    #     self.fields["title"].widget.attrs.update(
    #         {
    #             "class": "input input-bordered input-primary w-full max-w-xs",
    #             "type": "text",
    #         }
    #     )
    #     self.fields["author"].widget.attrs.update(
    #         {
    #             "class": "select select-primary w-full max-w-xs",
    #             "type": "text",
    #         }
    #     )
    #     self.fields["categories"].widget.attrs.update(
    #         {
    #             "class": "select select-primary w-full max-w-xs",
    #             "type": "text",
    #         }
    #     )
    #     self.fields["book_content"].widget.attrs.update(
    #         {
    #             "class": "input input-bordered input-primary w-full max-w-xs",
    #             "type": "text",
    #         }
    #     )
    #     self.fields["description"].widget.attrs.update(
    #         {
    #             "class": "input input-bordered input-primary w-full max-w-xs",
    #             "type": "text",
    #         }
    #     )
    #     self.fields["isbn_number"].widget.attrs.update(
    #         {
    #             "class": "input input-bordered input-primary w-full max-w-xs",
    #             "type": "text",
    #         }
    #     )
    #     self.fields["borrow_price"].widget.attrs.update(
    #         {
    #             "class": "input input-bordered input-primary w-full max-w-xs",
    #             "type": "text",
    #         }
    #     )
    #     self.fields["stk_quantity"].widget.attrs.update(
    #         {
    #             "class": "input input-bordered input-primary w-full max-w-xs",
    #             "type": "text",
    #         }
    #     )
    #     self.fields["is_available"].widget.attrs.update(
    #         {
    #             "class": "toggle toggle-primary",
    #             "type": "checkbox",
    #         }
    #     )
    #     self.fields["discount_price"].widget.attrs.update(
    #         {
    #             "class": "input input-bordered input-primary w-full max-w-xs",
    #             "type": "text",
    #         }
    #     )

    # for field in self.fields:
    #     if field == "book_image":
    #         self.fields[field].widget.attrs.update(
    #             {
    #                 "class": "file-input file-input-bordered file-input-primary w-full max-w-xs",
    #                 "type": "file",
    #             }
    #         )
    #     if field == "is_available":
    #         self.fields[field].widget.attrs.update(
    #             {
    #                 "class": "toggle toggle-primary",
    #                 "type": "checkbox",
    #             }
    #         )

    #     # if field == "author":
    #     #     self.fields[field].widget.attrs.update(
    #     #         {
    #     #             "class": "select select-bordered w-full max-w-xs",
    #     #         }
    #     #     )
    #     else:
    #         self.fields[field].widget.attrs.update(
    #             {
    #                 "class": ("input input-bordered w-full max-w-xs"),
    #                 "placeholder": ("Type here"),
    #                 "type": "text",
    #             }
    #         )
