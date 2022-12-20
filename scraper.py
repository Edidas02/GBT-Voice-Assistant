from selenium import webdriver

def find_best_price(item):
    # Create a list to store the prices
    prices = []
    # Set the URL for the first website
    url1 = "https://www.website1.com/search?q={}".format(item)
    
    # Set the URL for the second website
    url2 = "https://www.website2.com/search?q={}".format(item)
    
    # Set the URL for the third website
    url3 = "https://www.website3.com/search?q={}".format(item)
    
    # Create a webdriver object
    driver = webdriver.Firefox()
    
    # Scrape the prices from the first website
    driver.get(url1)
    elements = driver.find_elements_by_css_selector('.price')
    for element in elements:
        price = element.text
        prices.append(price)
    
    # Scrape the prices from the second website
    driver.get(url2)
    elements = driver.find_elements_by_css_selector('.price')
    for element in elements:
        price = element.text
        prices.append(price)
    
    # Scrape the prices from the third website
    driver.get(url3)
    elements = driver.find_elements_by_css_selector('.price')
    for element in elements:
        price = element.text
        prices.append(price)
    
    # Close the webdriver
    driver.close()
    
    # Find the lowest price in the list of prices
    lowest_price = min(prices)
    
    # Return the lowest price
    return lowest_price

# Test the function
print(find_best_price("iphone 12"))
