class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Child classes must implement this method")
    
    def props_to_html(self):
        final = ""
        if self.props is None:
            return ""
        for item in self.props:
            final += f' {item}="{self.props[item]}"'
        return final

    def __repr__(self):
        return f"Tag: {self.tag} \nValue: {self.value} \nChildren: {self.children} \nProps: {self.props}"
