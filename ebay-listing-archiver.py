from ebay.utils import set_config_file
from ebay.shopping import FindProducts

set_config_file("ebay.apikey")
print FindProducts("pen", "false", "10", "JSON")