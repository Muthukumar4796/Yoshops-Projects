import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
import warnings
warnings.filterwarnings('ignore')


order=pd.read_csv("orders_2016-2020_Dataset.csv")
review=pd.read_csv("review_dataset.csv")

# 1. Analysis of Reviews given by Customers

def visualize_review_data():
    #     # Check for missing values and replace with "Not reviewed"
    #     review.fillna('Not reviewed', inplace=True)

    # Count the number of reviews for each star rating
    stars_count = review['stars'].value_counts()

    # Create a pie chart of star ratings
    plt.figure(figsize=(8, 6))
    stars_count[0:4].plot(kind='pie', autopct='%1.1f%%', startangle=0)
    plt.title('Star Ratings for Reviews')
    plt.axis('equal')

    # Save the plot as a PDF file
    with PdfPages('1.pdf') as pdf:
        pdf.savefig()

    # Save the star count as an Excel file
    stars_count.to_excel('1.xlsx')


# visualize_review_data()

# 2. Analysis of different payment methods used by the Customers

order[['method','amount']]=order['Payment Method'].str.split('₹',1,expand=True)
order.method.unique()


def visualize_payment_data():
    order[['method', 'amount']] = order['Payment Method'].str.split('₹', 1, expand=True)
    order.method.unique()
    method_count = order.method.value_counts()

    # Create bar plot of payment method counts
    plt.figure(figsize=(20, 7))
    #     sns.barplot(x=method_count.index, y=method_count.values)
    method_count.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Payment Method Counts")

    # Save the plot as a PDF file
    with PdfPages('2.pdf') as pdf:
        pdf.savefig()

    # Excel
    method_count.to_excel('2.xlsx')
# visualize_payment_data()

# 3. Analysis of Top Consumer States of India
def visualize_top_state():
    state_count = order['Shipping State'].value_counts()

    # Create bar plot of payment method counts
    plt.figure(figsize=(20, 7))
    #     sns.barplot(x=method_count.index, y=method_count.values)
    state_count[0:5].plot(kind='pie', autopct='%1.1f%%')
    plt.title("Top Consumer States of India")

    # Save the plot as a PDF file
    with PdfPages('3.pdf') as pdf:
        pdf.savefig()

    # Excel file
    state_count.to_excel('3.xlsx')
# visualize_top_state()

# 4. Analysis of Top Consumer Cities of India
city_count = order['Shipping City'].value_counts()


def visualize_top_city():
    city_count = order['Shipping City'].value_counts()

    # Create bar plot of payment method counts
    plt.figure(figsize=(20, 7))
    #     sns.barplot(x=method_count.index, y=method_count.values)
    city_count[0:5].plot(kind='pie', autopct='%1.1f%%')
    plt.title("Top Consumer Cities of India")

    # Save the plot as a PDF file
    with PdfPages('4.pdf') as pdf:
        pdf.savefig()

    # Excel file
    city_count.to_excel('4.xlsx')
# visualize_top_city()

# 5. Analysis of Top Selling Product Categories
def visualize_top_categories():
    # Group orders by product category and get count of orders for each category
    category_counts = review.groupby('category')['stars'].nunique()

    # Sort categories by order count and get top 10
    top_categories = category_counts.sort_values(ascending=False).head(10)

    # Create horizontal bar plot of top categories
    plt.figure(figsize=(8, 6))
    sns.barplot(x=top_categories.values, y=top_categories.index)
    plt.title("Top 10 Selling Product Categories")
    plt.xlabel("Number of Orders")
    plt.ylabel("Product Category")

    # Save the plot as a PDF file
    with PdfPages('5.pdf') as pdf:
        pdf.savefig()

    # Excel file
    top_categories.to_excel('5.xlsx')
# visualize_top_categories()

# 6. Analysis of Reviews for All Product Categories
status=review['status']
status.fillna('not reviewed',inplace=True)
status.value_counts()
def reviews_all_category():
    status = review['status']
    status.fillna('not reviewed', inplace=True)
    status_count = status.value_counts()
    # Create bar plot of payment method counts
    plt.figure(figsize=(20, 7))
    status_count.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Reviews for All Categories")

    # Save the plot as a PDF file
    with PdfPages('6.pdf') as pdf:
        pdf.savefig()

    # Excel file
    status_count.to_excel('6.xlsx')


# reviews_all_category()

# 7. Analysis of Number of Orders Per Month Per Year
date=order[order['Fulfillment Status']=='Fulfilled']
date['Fulfillment Date and Time Stamp']=pd.to_datetime(date['Fulfillment Date and Time Stamp'])

date['month']=date['Fulfillment Date and Time Stamp'].dt.strftime('%B')
date['year']=date['Fulfillment Date and Time Stamp'].dt.strftime('%Y')

date['month'].value_counts()
date['year'].value_counts()
date.head()


def order_per_month_year():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))

    month_count = date['month'].value_counts()
    year_count = date['year'].value_counts()
    # Plot pie chart for distribution of months
    month_count.plot(kind='pie', autopct='%1.1f%%', ax=ax1)
    ax1.set_title('orders per month')

    # Plot pie chart for distribution of years
    year_count.plot(kind='pie', autopct='%1.1f%%', ax=ax2)
    ax2.set_title('orders per year')

    # Save the plot as a PDF file
    with PdfPages('7.pdf') as pdf:
        pdf.savefig()

    # Excel file
    month_count.to_excel('7-1.xlsx')
    year_count.to_excel('7-2.xlsx')


# order_per_month_year()


# 8. analysis of Reviews for Number of Orders Per Month Per Year

df1=order
df2=review
df1.rename(columns={'LineItem Name':'product_name'},inplace=True)
merge=pd.merge(df1,df2,on='product_name')

merge['Fulfillment Date and Time Stamp']=pd.to_datetime(merge['Fulfillment Date and Time Stamp'])
merge['month']=merge['Fulfillment Date and Time Stamp'].dt.strftime('%B')
merge['year']=merge['Fulfillment Date and Time Stamp'].dt.strftime('%Y')
merge.head()

month_counts = merge.groupby('month')['stars'].value_counts()
year_counts = merge.groupby('year')['stars'].value_counts()


def reviews_order_per_month_year():
    month_counts = merge.groupby('month')['stars'].value_counts()
    year_counts = merge.groupby('year')['stars'].value_counts()
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

    # Plot pie chart for distribution of months
    month_counts[:4].plot(kind='pie', autopct='%1.1f%%', ax=ax1)
    ax1.set_title('reviews of orders per month')

    # Plot pie chart for distribution of years
    year_counts[:6].plot(kind='pie', autopct='%1.1f%%', ax=ax2)
    ax2.set_title(' reviews of orders per year')

    # Save the plot as a PDF file
    with PdfPages('8.pdf') as pdf:
        pdf.savefig()

    # Excel file
    month_counts.to_excel('8-1.xlsx')
    year_counts.to_excel('8-2.xlsx')


# reviews_order_per_month_year()

# 9. analysis of Number of Orders Across Parts of a Day
date['hour']=date['Fulfillment Date and Time Stamp'].dt.strftime('%H')


def order_per_parts_of_day():
    hour_count = date.hour.value_counts()
    # Create bar plot of payment method counts
    plt.figure(figsize=(20, 7))
    hour_count[:10].plot(kind='pie', autopct='%1.1f%%')
    plt.title("order per parts of day")

    # Save the plot as a PDF file
    with PdfPages('9.pdf') as pdf:
        pdf.savefig()

    # Excel file
    hour_count.to_excel('9.xlsx')


# order_per_parts_of_day()

# 10.Full report

def all_report():
    with PdfPages('report.pdf') as pdf_output:
        # Visualize Review Data
        plt.figure(figsize=(8, 6))
        visualize_review_data()
        pdf_output.savefig()
        #         plt.close()

        # Visualize Payment Data
        plt.figure(figsize=(8, 6))
        visualize_payment_data()
        pdf_output.savefig()
        #         plt.close()

        # Visualize Top State
        plt.figure(figsize=(8, 6))
        visualize_top_state()
        pdf_output.savefig()
        #         plt.close()

        # Visualize Top City
        plt.figure(figsize=(8, 6))
        visualize_top_city()
        pdf_output.savefig()
        #         plt.close()

        # Visualize Top Categories
        plt.figure(figsize=(8, 6))
        visualize_top_categories()
        pdf_output.savefig()
        #         plt.close()

        # Visualize reviews all category
        plt.figure(figsize=(8, 6))
        reviews_all_category()
        pdf_output.savefig()
        #         plt.close()

        # Visualize order per month and year
        plt.figure(figsize=(8, 6))
        order_per_month_year()
        pdf_output.savefig()
        #         plt.close()

        # Visualize reviews of order per month and year
        plt.figure(figsize=(8, 6))
        reviews_order_per_month_year()
        pdf_output.savefig()
        #         plt.close()

        # Visualize order per part of day
        plt.figure(figsize=(8, 6))
        order_per_parts_of_day()
        pdf_output.savefig()


#         plt.close()

# all_report()

a=int(input('Enter the value: '))
if a==1:
    visualize_review_data()
elif a==2:
    visualize_payment_data()
elif a==3:
    visualize_top_state()
elif a==4:
    visualize_top_city()
elif a==5:
    visualize_top_categories()
elif a==6:
    reviews_all_category()
elif a==7:
    order_per_month_year()
elif a==8:
    reviews_order_per_month_year()
elif a==9:
    order_per_parts_of_day()
else:
    all_report()