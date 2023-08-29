class Review:


    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant


class Restaurant:


    def reviews(self):
        return self.reviews

    def customers(self):
        customer_list = []
        for review in self.reviews:
            customer_list.append(review.customer)
        return list(set(customer_list))


class Customer:

    def restaurants(self):
        restaurant_list = []
        for review in self.reviews:
            restaurant_list.append(review.restaurant)
        return list(set(restaurant_list))


    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.add_review(review)
