from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

#a = TextNode("sample a", TextType.BOLD)
#a_copy = TextNode("sample a", TextType.BOLD)
#b = TextNode("sample b", TextType.LINK, "http:www.text.com")


props = {
"href": "https://www.google.com",
"target": "_blank",
}
#node = HTMLNode(props=props)
leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()

print(leaf)