class Customer:
  

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        matching_customers = []
        for customer in cls.all_customers:
            if customer.given_name == name:
                matching_customers.append(customer)
        return matching_customers


class Restaurant:
    

    def average_star_rating(self):
        total_ratings = sum(review.rating for review in self.reviews)
        num_reviews = len(self.reviews)
        if num_reviews > 0:
            return total_ratings / num_reviews
        else:
            return 0
