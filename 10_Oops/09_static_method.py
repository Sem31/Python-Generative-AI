# Static methods are just a normal function which we're using as utility function in class or outside the class


class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]


raw = " water , milk , ginger , honey "

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)
