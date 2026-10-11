from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list[HTMLNode],
        props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("missing tag")
        if self.children is None:
            raise ValueError("missing children")
        result = f'<{self.tag}'
        if self.props:
            for k, v in self.props.items():
                result += f' {k}="{v}"'
        result += '>'
        for child in self.children:
            result += child.to_html()
        result += f'</{self.tag}>'
        return result

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
