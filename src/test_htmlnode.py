import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_print(self):
        props = {
        "href": "https://www.google.com",
        "target": "_blank",
        }
        node = HTMLNode()
        
        output = (
            "Tag: None \nValue: None \nChildren: None \nProps: None"
        )
        self.assertEqual(output, node.__repr__())


    def test_props_to_html(self):
        props = {
        "href": "https://www.google.com",
        "target": "_blank",
        }  
        node = HTMLNode(props=props)
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(expected, node.props_to_html())      

    def test_props_to_html_None(self):
        node = HTMLNode()
        expected = ""
        self.assertEqual(expected, node.props_to_html())    
    
    