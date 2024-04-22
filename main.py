from db_config import get_redis_connection
import json
import requests
import pandas as pd
from DataProcessing import DataProcess, Visualization

url = "http://localhost:5000/items"

"""Establish Redis database connection"""
r = get_redis_connection()

# Remove previous Redis DB content
# r.flushall()

"""Use cURL command to save API data into a json file"""
# curl http://localhost:5000/items grocery-items.json > grocery-items.json

if __name__ == "__main__":
    
    ## Load json file
    items = pd.read_json("./grocery-items.json")
    
    """Calculate the total sales for each product"""
    total_sales = DataProcess.calc_total_sales(items)
    print(total_sales)
    
    """Find the most popular item sold"""
    most_popular = DataProcess.most_popular(items)
    print("The most popular item had", most_popular, "sales.")
    
    """Create a chart with the total sales of each product"""
    Visualization.sales_chart(items, total_sales)