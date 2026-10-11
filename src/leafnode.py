from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        value: str,
        props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError
        if not self.tag:
            return self.value
        props_string = ""
        if self.props:
            for k, v in self.props.items():
                props_string += f' {k}="{v}"'
        result = f'<{self.tag}{props_string}>'
        void_tags = {"img", "br", "hr",}
        if self.tag not in void_tags:
            result += f'{self.value}</{self.tag}>'
        return result

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
