# coding: utf-8

"""
MoneyKit API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 2023-02-18
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import json
import re  # noqa: F401
from enum import Enum


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class BudSubcategory(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    ACCOUNT_FEES_AND_OTHER_BANK_CHARGES = "account_fees_and_other_bank_charges"
    ATM_FEES = "atm_fees"
    CASH_WITHDRAWALS = "cash_withdrawals"
    CURRENCY_EXCHANGE_AND_FEES = "currency_exchange_and_fees"
    INTEREST = "interest"
    NSF_AND_OVERDRAFT_FEES = "nsf_and_overdraft_fees"
    OTHER_BANKING = "other_banking"
    OUTGOING_CHECKS = "outgoing_checks"
    OVERDRAFT_PROTECTION = "overdraft_protection"
    REFUNDS_AND_REVERSALS = "refunds_and_reversals"
    UNPAID_TRANSACTIONS = "unpaid_transactions"
    BUY_NOW_PAY_LATER = "buy_now_pay_later"
    CAR_PAYMENT = "car_payment"
    CASH_ADVANCE_LOANS = "cash_advance_loans"
    CREDIT_CARDS = "credit_cards"
    DEBT_MANAGEMENT = "debt_management"
    LOAN_INCOMING = "loan_incoming"
    LOAN_REPAYMENT = "loan_repayment"
    OTHER_BORROWING_AND_LOANS = "other_borrowing_and_loans"
    STUDENT_LOAN = "student_loan"
    VEHICLE_LOAN = "vehicle_loan"
    CHARITY = "charity"
    OTHER_CHARITY = "other_charity"
    CHILD_SUPPORT = "child_support"
    CHILDCARE = "childcare"
    CHILDRENS_EXPENSES = "childrens_expenses"
    OTHER_DEPENDENT_COSTS = "other_dependent_costs"
    DRIVING_LESSONS = "driving_lessons"
    OTHER_EDUCATION = "other_education"
    UNIVERSITY_AND_TUITION = "university_and_tuition"
    BOOKS_AND_READING = "books_and_reading"
    CINEMA = "cinema"
    GAMING = "gaming"
    LEISURE_AND_AMUSEMENT_ACTIVITIES = "leisure_and_amusement_activities"
    OTHER_ENTERTAINMENT = "other_entertainment"
    OTHER_EVENTS = "other_events"
    SPORT_EVENTS = "sport_events"
    THEATRE_CONCERTS_AND_TICKETS = "theatre_concerts_and_tickets"
    BUSINESS_EXPENSES = "business_expenses"
    FINANCIAL_AND_LEGAL_EXPENSES = "financial_and_legal_expenses"
    OTHER_EXPENSES = "other_expenses"
    OTHER_MEMBERSHIPS_AND_SERVICES = "other_memberships_and_services"
    POSTAGE_AND_OFFICE_SUPPLIES = "postage_and_office_supplies"
    BARS_AND_PUBS = "bars_and_pubs"
    COFFEE = "coffee"
    CONVENIENCE_STORES = "convenience_stores"
    EATING_OUT_AND_TAKEAWAYS = "eating_out_and_takeaways"
    GROCERIES = "groceries"
    OTHER_EATING_OUT = "other_eating_out"
    OTHER_FOOD_AND_DRINK = "other_food_and_drink"
    SPECIALITY_FOOD_AND_DRINK = "speciality_food_and_drink"
    GAMBLING_AND_BETTING = "gambling_and_betting"
    LOTTERIES_AND_SWEEPSTAKES = "lotteries_and_sweepstakes"
    OTHER_GAMBLING_AND_LOTTERIES = "other_gambling_and_lotteries"
    OTHER_GENERAL = "other_general"
    BEAUTY = "beauty"
    DENTAL = "dental"
    GYM_AND_FITNESS = "gym_and_fitness"
    HEALTHCARE = "healthcare"
    OTHER_HEALTH_AND_PERSONAL_CARE = "other_health_and_personal_care"
    OPTICAL = "optical"
    PHARMACIES_AND_HEALTH_PRODUCTS = "pharmacies_and_health_products"
    SPORT_ACCESSORIES_AND_EQUIPMENT = "sport_accessories_and_equipment"
    FURNITURE = "furniture"
    GARDENING = "gardening"
    HOME_MAINTENANCE = "home_maintenance"
    HOUSEHOLD_GOODS = "household_goods"
    LAUNDRY = "laundry"
    OTHER_HOME = "other_home"
    PETS = "pets"
    BENEFITS_AND_SOCIAL_SECURITY = "benefits_and_social_security"
    CHILD_SUPPORT_INCOME = "child_support_income"
    CRYPTO_PLATFORM_INCOMING = "crypto_platform_incoming"
    DEPOSITS = "deposits"
    EMPLOYMENT_INCOME = "employment_income"
    INVESTMENT_INCOME = "investment_income"
    OTHER_INCOME = "other_income"
    PENSION_INCOME = "pension_income"
    RENTAL_INCOME = "rental_income"
    BUSINESS_INSURANCE = "business_insurance"
    HEALTH_AND_LIFE_INSURANCE = "health_and_life_insurance"
    HOME_INSURANCE = "home_insurance"
    OTHER_INSURANCE = "other_insurance"
    PET_INSURANCE = "pet_insurance"
    TRAVEL_INSURANCE = "travel_insurance"
    VEHICLE_INSURANCE = "vehicle_insurance"
    BROADBAND_PHONE_TV = "broadband_phone_tv"
    DIGITAL_MEDIA_AND_SOFTWARE = "digital_media_and_software"
    OTHER_MEDIA_AND_TELECOMS = "other_media_and_telecoms"
    TV_STREAMING_SERVICES = "tv_streaming_services"
    MORTGAGE = "mortgage"
    OTHER_MORTGAGE_AND_RENT = "other_mortgage_and_rent"
    RENT = "rent"
    CRYPTO_PLATFORM_OUTGOING = "crypto_platform_outgoing"
    INVESTMENTS = "investments"
    PENSIONS = "pensions"
    OTHER_PENSIONS_SAVINGS_AND_INVESTMENTS = "other_pensions_savings_and_investments"
    SAVINGS = "savings"
    CLOTHING_AND_ACCESSORIES = "clothing_and_accessories"
    DEPARTMENT_STORES = "department_stores"
    ELECTRONICS_APPLIANCES_AND_TECHNOLOGY = "electronics_appliances_and_technology"
    FLOWERS_AND_GIFTS = "flowers_and_gifts"
    GENERAL_ONLINE_SHOPPING = "general_online_shopping"
    HOBBIES = "hobbies"
    OTHER_SHOPPING = "other_shopping"
    SMOKING_AND_VAPING = "smoking_and_vaping"
    FEDERAL_TAX = "federal_tax"
    OTHER_TAXES = "other_taxes"
    INTERNAL_TRANSFERS = "internal_transfers"
    OTHER_TRANSFERS = "other_transfers"
    TRANSFERS_IN = "transfers_in"
    TRANSFERS_OUT = "transfers_out"
    OTHER_TRANSPORT = "other_transport"
    PARKING_AND_TOLLS = "parking_and_tolls"
    PUBLIC_TRANSPORT = "public_transport"
    TAXI = "taxi"
    VEHICLE = "vehicle"
    VEHICLE_FUEL_AND_CHARGING = "vehicle_fuel_and_charging"
    VEHICLE_RENTAL = "vehicle_rental"
    PETROL_AND_VEHICLE_CHARGING = "petrol_and_vehicle_charging"
    FLIGHTS_AND_AIRPORT_EXPENSES = "flights_and_airport_expenses"
    HOLIDAY_AND_TRAVEL_EXPENSES = "holiday_and_travel_expenses"
    OTHER_TRAVEL = "other_travel"
    OTHER_UTILITIES = "other_utilities"
    UTILITIES_ENERGY = "utilities_energy"
    UTILITIES_WATER_AND_SEWAGE = "utilities_water_and_sewage"
    WASTE_AND_RECYCLING = "waste_and_recycling"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of BudSubcategory from a JSON string"""
        return cls(json.loads(json_str))
