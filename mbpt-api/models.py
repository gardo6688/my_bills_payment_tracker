class PaymentItem:
    def __init__(self, category, brand_name, amount, split):
        self.category = category
        self.brand_name = brand_name
        self.amount = amount
        self.split = split

    def to_dict(self):
        return {
            "category": self.category,
            "brand_name": self.brand_name,
            "amount": self.amount,
            "split": self.split
        }

class PaymentActivity:
    def __init__(self, payment_items, payment_date, is_paid):
        self.payment_items = [item.to_dict() for item in payment_items]
        self.payment_date = payment_date
        self.is_paid = is_paid

    def to_dict(self):
        return {
            "payment_items": self.payment_items,
            "payment_date": self.payment_date,
            "is_paid": self.is_paid
        }

class Biller:
    def __init__(self, biller_type, payment_activities, remaining_payment, payee):
        self.biller_type = biller_type
        self.payment_activities = [activity.to_dict() for activity in payment_activities]
        self.remaining_payment = remaining_payment
        self.payee = payee

    def to_dict(self):
        return {
            "biller_type": self.biller_type,
            "payment_activities": self.payment_activities,
            "remaining_payment": self.remaining_payment,
            "payee": self.payee
        }
