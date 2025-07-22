import pytest
from pytest_metadata.plugin import metadata, metadata_key
from selenium import  webdriver
driver=webdriver.Chrome()
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver


#hooks for adding env info into html report
from pytest_metadata.plugin import metadata_key
def pytest_configure(config):
    config.stash[metadata_key] ['Project Name']='Ecommerce Project,nopcommerce'
    config.stash[metadata_key]['Tester Name'] = 'Usha'