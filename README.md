# coffee-shop-challenge

A Python object-oriented programming project that models a coffee shop domain with customers, coffees, and orders.
Project Overview
This project implements a simple domain model for a coffee shop with three main classes:

Coffee: Represents a type of coffee available in the shop
Customer: Represents a customer who can order coffees
Order: Represents an order placed by a customer for a specific coffee

The relationships between these classes are:

Coffee - Customer: Many-to-many relationship (through orders)
Coffee - Order: One-to-many relationship
Customer - Order: One-to-many relationship

Features

Type checking and validation for all inputs
Immutable properties (Coffee name and Order price)
Object relationships that allow easy navigation between related objects
Aggregate functions for calculating statistics about orders and customers
Class methods for finding the most loyal customer for each coffee