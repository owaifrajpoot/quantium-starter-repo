import os
from webdriver_manager.chrome import ChromeDriverManager

# Ensure chromedriver is installed and in the PATH for dash testing
driver_path = ChromeDriverManager().install()
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)

from app import app

def test_header_present(dash_duo):
    """
    Test that the header is present and contains the correct text
    """
    dash_duo.start_server(app)
    
    # Wait for the header container h1 to load
    dash_duo.wait_for_element("#header-container h1", timeout=10)
    
    # Verify the text content
    assert dash_duo.find_element("#header-container h1").text == "SOUL FOODS" # text is uppercase via CSS text-transform but HTML text might be "Soul Foods", dash_duo gets rendered text, meaning it depends on the driver. Let's just check the element exists.

def test_visualization_present(dash_duo):
    """
    Test that the sales line chart visualization is present
    """
    dash_duo.start_server(app)
    
    # Wait for the graph to load within the dom
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    assert dash_duo.find_element("#sales-line-chart")

def test_region_picker_present(dash_duo):
    """
    Test that the region picker radio buttons are present
    """
    dash_duo.start_server(app)
    
    # Wait for the region filter to load
    dash_duo.wait_for_element("#region-filter", timeout=10)
    assert dash_duo.find_element("#region-filter")
