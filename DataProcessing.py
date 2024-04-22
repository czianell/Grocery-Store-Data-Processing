import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.figure

class DataProcess:
  """Calculate the total sales of each item.
  """
  @staticmethod
  def calc_total_sales(df):
    df['total_sales'] = df['item_price'] * df['num_of_purchases']
    
    return df
  
  """Find the most purchased item.
  """
  @staticmethod
  def most_popular(df):
    highest_num = df['num_of_purchases'].max()
    
    return highest_num
  
class Visualization:
  """Create a chart with each item and their total sales.
  """
  @staticmethod
  def sales_chart(df, total_sales):
    plt.figure(figsize=(8, 6))
    plt.bar(df['item_name'], df['total_sales'], color='skyblue')
    plt.xlabel('Items')
    plt.ylabel('Total Sales')
    plt.title('Total Sales of Grocery Store Items')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()